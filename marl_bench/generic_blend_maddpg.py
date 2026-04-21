import copy
import random
from dataclasses import dataclass
from typing import Dict, Optional

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


class ReplayBuffer:
    def __init__(self, obs_dim: int, act_dim: int, n_agents: int, capacity: int) -> None:
        self.obs = np.zeros((capacity, n_agents, obs_dim), dtype=np.float32)
        self.next_obs = np.zeros((capacity, n_agents, obs_dim), dtype=np.float32)
        self.actions = np.zeros((capacity, n_agents, act_dim), dtype=np.float32)
        self.reward_local = np.zeros((capacity, n_agents), dtype=np.float32)
        self.reward_global = np.zeros((capacity, 1), dtype=np.float32)
        self.done = np.zeros((capacity, n_agents), dtype=np.float32)
        self.capacity = int(capacity)
        self.size = 0
        self.ptr = 0

    def add(self, obs, next_obs, actions, reward_local, reward_global, done) -> None:
        self.obs[self.ptr] = obs
        self.next_obs[self.ptr] = next_obs
        self.actions[self.ptr] = actions
        self.reward_local[self.ptr] = reward_local
        self.reward_global[self.ptr] = reward_global
        self.done[self.ptr] = done
        self.ptr = (self.ptr + 1) % self.capacity
        self.size = min(self.size + 1, self.capacity)

    def sample(self, batch_size: int):
        idx = np.random.randint(0, self.size, size=batch_size)
        return (
            torch.as_tensor(self.obs[idx], dtype=torch.float32, device=device),
            torch.as_tensor(self.next_obs[idx], dtype=torch.float32, device=device),
            torch.as_tensor(self.actions[idx], dtype=torch.float32, device=device),
            torch.as_tensor(self.reward_local[idx], dtype=torch.float32, device=device),
            torch.as_tensor(self.reward_global[idx], dtype=torch.float32, device=device),
            torch.as_tensor(self.done[idx], dtype=torch.float32, device=device),
        )


class MLPActor(nn.Module):
    def __init__(self, obs_dim: int, act_dim: int, hidden_dim: int) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(obs_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, act_dim),
            nn.Tanh(),
        )

    def forward(self, obs: torch.Tensor) -> torch.Tensor:
        return self.net(obs)


class LocalCritic(nn.Module):
    def __init__(self, obs_dim: int, act_dim: int, hidden_dim: int) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(obs_dim + act_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1),
        )

    def forward(self, obs: torch.Tensor, act: torch.Tensor) -> torch.Tensor:
        return self.net(torch.cat([obs, act], dim=-1))


class JointCritic(nn.Module):
    def __init__(self, joint_obs_dim: int, joint_act_dim: int, hidden_dim: int) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(joint_obs_dim + joint_act_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1),
        )

    def forward(self, joint_obs: torch.Tensor, joint_act: torch.Tensor) -> torch.Tensor:
        return self.net(torch.cat([joint_obs, joint_act], dim=-1))


@dataclass
class UpdateStats:
    local_critic_loss: float = 0.0
    global_critic_loss: float = 0.0
    actor_loss: float = 0.0
    actor_source_local_grad_norm: float = 0.0
    actor_source_global_grad_norm: float = 0.0
    actor_source_global_ratio: float = 0.0
    actor_source_cos: float = 0.0


class GenericBlendMADDPG:
    def __init__(
        self,
        obs_dim: int,
        act_dim: int,
        n_agents: int,
        hidden_dim: int = 256,
        gamma: float = 0.99,
        tau: float = 0.01,
        lr_actor: float = 3e-4,
        lr_critic: float = 3e-4,
        buffer_size: int = 200000,
        batch_size: int = 256,
        warmup_steps: int = 5000,
        policy_delay: int = 2,
        target_noise_std: float = 0.2,
        target_noise_clip: float = 0.5,
        blend_weight: float = 0.5,
        grad_clip: float = 5.0,
        seed: int = 0,
    ) -> None:
        random.seed(seed)
        np.random.seed(seed)
        torch.manual_seed(seed)

        self.obs_dim = int(obs_dim)
        self.act_dim = int(act_dim)
        self.n_agents = int(n_agents)
        self.gamma = float(gamma)
        self.tau = float(tau)
        self.batch_size = int(batch_size)
        self.warmup_steps = int(warmup_steps)
        self.policy_delay = max(1, int(policy_delay))
        self.target_noise_std = float(target_noise_std)
        self.target_noise_clip = float(target_noise_clip)
        self.blend_weight = float(blend_weight)
        self.grad_clip = float(grad_clip)
        self.total_updates = 0

        self.buffer = ReplayBuffer(obs_dim, act_dim, n_agents, buffer_size)

        self.actors = [MLPActor(obs_dim, act_dim, hidden_dim).to(device) for _ in range(n_agents)]
        self.target_actors = [copy.deepcopy(actor).to(device) for actor in self.actors]

        self.local_critics1 = [LocalCritic(obs_dim, act_dim, hidden_dim).to(device) for _ in range(n_agents)]
        self.local_critics2 = [LocalCritic(obs_dim, act_dim, hidden_dim).to(device) for _ in range(n_agents)]
        self.target_local_critics1 = [copy.deepcopy(c).to(device) for c in self.local_critics1]
        self.target_local_critics2 = [copy.deepcopy(c).to(device) for c in self.local_critics2]

        joint_obs_dim = n_agents * obs_dim
        joint_act_dim = n_agents * act_dim
        self.global_critic1 = JointCritic(joint_obs_dim, joint_act_dim, hidden_dim).to(device)
        self.global_critic2 = JointCritic(joint_obs_dim, joint_act_dim, hidden_dim).to(device)
        self.target_global_critic1 = copy.deepcopy(self.global_critic1).to(device)
        self.target_global_critic2 = copy.deepcopy(self.global_critic2).to(device)

        self.actor_opts = [torch.optim.Adam(actor.parameters(), lr=lr_actor) for actor in self.actors]
        self.local_critic_opts1 = [torch.optim.Adam(c.parameters(), lr=lr_critic) for c in self.local_critics1]
        self.local_critic_opts2 = [torch.optim.Adam(c.parameters(), lr=lr_critic) for c in self.local_critics2]
        self.global_critic_opt1 = torch.optim.Adam(self.global_critic1.parameters(), lr=lr_critic)
        self.global_critic_opt2 = torch.optim.Adam(self.global_critic2.parameters(), lr=lr_critic)

        self.last_stats = UpdateStats()

    def act(self, obs: np.ndarray, explore: bool = True, noise_scale: float = 0.1) -> np.ndarray:
        obs_t = torch.as_tensor(obs, dtype=torch.float32, device=device)
        with torch.no_grad():
            actions = torch.stack([self.actors[i](obs_t[i : i + 1]).squeeze(0) for i in range(self.n_agents)], dim=0)
        if explore and noise_scale > 0.0:
            actions = actions + noise_scale * torch.randn_like(actions)
        return torch.clamp(actions, -1.0, 1.0).cpu().numpy()

    def store_transition(self, obs, next_obs, actions, reward_local, reward_global, done) -> None:
        self.buffer.add(obs, next_obs, actions, reward_local, reward_global, done)

    def _soft_update(self, target: nn.Module, source: nn.Module) -> None:
        for tp, p in zip(target.parameters(), source.parameters()):
            tp.data.mul_(1.0 - self.tau).add_(p.data, alpha=self.tau)

    def update(self) -> Optional[Dict[str, float]]:
        if self.buffer.size < max(self.batch_size, self.warmup_steps):
            return None

        self.total_updates += 1
        obs, next_obs, actions, reward_local, reward_global, done = self.buffer.sample(self.batch_size)
        bsz = obs.size(0)
        joint_obs = obs.reshape(bsz, -1)
        next_joint_obs = next_obs.reshape(bsz, -1)
        joint_actions = actions.reshape(bsz, -1)
        done_global = done.max(dim=1, keepdim=True).values

        with torch.no_grad():
            next_actions = torch.stack([self.target_actors[i](next_obs[:, i, :]) for i in range(self.n_agents)], dim=1)
            noise = torch.randn_like(next_actions) * self.target_noise_std
            noise = torch.clamp(noise, -self.target_noise_clip, self.target_noise_clip)
            next_actions = torch.clamp(next_actions + noise, -1.0, 1.0)
            next_joint_actions = next_actions.reshape(bsz, -1)

        local_losses = []
        for i in range(self.n_agents):
            with torch.no_grad():
                tq1 = self.target_local_critics1[i](next_obs[:, i, :], next_actions[:, i, :])
                tq2 = self.target_local_critics2[i](next_obs[:, i, :], next_actions[:, i, :])
                target_q = torch.min(tq1, tq2)
                y = reward_local[:, i : i + 1] + self.gamma * (1.0 - done[:, i : i + 1]) * target_q

            q1 = self.local_critics1[i](obs[:, i, :], actions[:, i, :])
            q2 = self.local_critics2[i](obs[:, i, :], actions[:, i, :])
            loss1 = F.mse_loss(q1, y)
            loss2 = F.mse_loss(q2, y)

            self.local_critic_opts1[i].zero_grad()
            loss1.backward()
            torch.nn.utils.clip_grad_norm_(self.local_critics1[i].parameters(), self.grad_clip)
            self.local_critic_opts1[i].step()

            self.local_critic_opts2[i].zero_grad()
            loss2.backward()
            torch.nn.utils.clip_grad_norm_(self.local_critics2[i].parameters(), self.grad_clip)
            self.local_critic_opts2[i].step()
            local_losses.append(float((loss1 + loss2).item()))

        with torch.no_grad():
            tgq1 = self.target_global_critic1(next_joint_obs, next_joint_actions)
            tgq2 = self.target_global_critic2(next_joint_obs, next_joint_actions)
            target_global_q = torch.min(tgq1, tgq2)
            y_global = reward_global + self.gamma * (1.0 - done_global) * target_global_q

        gq1 = self.global_critic1(joint_obs, joint_actions)
        gq2 = self.global_critic2(joint_obs, joint_actions)
        global_loss1 = F.mse_loss(gq1, y_global)
        global_loss2 = F.mse_loss(gq2, y_global)

        self.global_critic_opt1.zero_grad()
        global_loss1.backward()
        torch.nn.utils.clip_grad_norm_(self.global_critic1.parameters(), self.grad_clip)
        self.global_critic_opt1.step()

        self.global_critic_opt2.zero_grad()
        global_loss2.backward()
        torch.nn.utils.clip_grad_norm_(self.global_critic2.parameters(), self.grad_clip)
        self.global_critic_opt2.step()

        actor_loss_values = []
        local_grad_norms = []
        global_grad_norms = []
        global_ratios = []
        grad_cosines = []

        if self.total_updates % self.policy_delay == 0:
            all_actor_actions = [self.actors[i](obs[:, i, :]) for i in range(self.n_agents)]
            for i in range(self.n_agents):
                params = list(self.actors[i].parameters())
                local_q = torch.min(
                    self.local_critics1[i](obs[:, i, :], all_actor_actions[i]),
                    self.local_critics2[i](obs[:, i, :], all_actor_actions[i]),
                )
                local_loss = -local_q.mean()

                joint_actor_actions = []
                for j in range(self.n_agents):
                    joint_actor_actions.append(all_actor_actions[j] if i == j else all_actor_actions[j].detach())
                joint_actor_actions = torch.stack(joint_actor_actions, dim=1)
                global_q = torch.min(
                    self.global_critic1(joint_obs, joint_actor_actions.reshape(bsz, -1)),
                    self.global_critic2(joint_obs, joint_actor_actions.reshape(bsz, -1)),
                )
                global_loss = -global_q.mean()

                local_grads = torch.autograd.grad(local_loss, params, retain_graph=True, allow_unused=True)
                global_grads = torch.autograd.grad(global_loss, params, retain_graph=True, allow_unused=True)

                local_sq = torch.zeros((), device=device)
                global_sq = torch.zeros((), device=device)
                dot = torch.zeros((), device=device)
                for g_local, g_global in zip(local_grads, global_grads):
                    if g_local is not None:
                        local_sq = local_sq + (g_local.detach() * g_local.detach()).sum()
                    if g_global is not None:
                        global_sq = global_sq + (g_global.detach() * g_global.detach()).sum()
                    if g_local is not None and g_global is not None:
                        dot = dot + (g_local.detach() * g_global.detach()).sum()

                local_norm = float(torch.sqrt(torch.clamp(local_sq, min=0.0)).item())
                global_norm = float(torch.sqrt(torch.clamp(global_sq, min=0.0)).item())
                ratio = global_norm / max(local_norm + global_norm, 1e-12)
                cosine = 0.0
                if local_norm > 1e-12 and global_norm > 1e-12:
                    cosine = float((dot / torch.sqrt(local_sq * global_sq + 1e-24)).clamp(-1.0, 1.0).item())

                self.actor_opts[i].zero_grad()
                for p, g_local, g_global in zip(params, local_grads, global_grads):
                    if g_local is None and g_global is None:
                        p.grad = None
                    elif g_local is None:
                        p.grad = self.blend_weight * g_global
                    elif g_global is None:
                        p.grad = (1.0 - self.blend_weight) * g_local
                    else:
                        p.grad = (1.0 - self.blend_weight) * g_local + self.blend_weight * g_global
                torch.nn.utils.clip_grad_norm_(params, self.grad_clip)
                self.actor_opts[i].step()

                actor_loss_values.append(float(((1.0 - self.blend_weight) * local_loss + self.blend_weight * global_loss).item()))
                local_grad_norms.append(local_norm)
                global_grad_norms.append(global_norm)
                global_ratios.append(ratio)
                grad_cosines.append(cosine)

            for i in range(self.n_agents):
                self._soft_update(self.target_actors[i], self.actors[i])
                self._soft_update(self.target_local_critics1[i], self.local_critics1[i])
                self._soft_update(self.target_local_critics2[i], self.local_critics2[i])
            self._soft_update(self.target_global_critic1, self.global_critic1)
            self._soft_update(self.target_global_critic2, self.global_critic2)

        self.last_stats = UpdateStats(
            local_critic_loss=float(np.mean(local_losses)) if local_losses else 0.0,
            global_critic_loss=float((global_loss1 + global_loss2).item()),
            actor_loss=float(np.mean(actor_loss_values)) if actor_loss_values else 0.0,
            actor_source_local_grad_norm=float(np.mean(local_grad_norms)) if local_grad_norms else 0.0,
            actor_source_global_grad_norm=float(np.mean(global_grad_norms)) if global_grad_norms else 0.0,
            actor_source_global_ratio=float(np.mean(global_ratios)) if global_ratios else 0.0,
            actor_source_cos=float(np.mean(grad_cosines)) if grad_cosines else 0.0,
        )
        return self.last_stats.__dict__.copy()
