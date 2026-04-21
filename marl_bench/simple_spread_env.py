from typing import Dict, List, Tuple

import numpy as np


try:
    from mpe2 import simple_spread_v3 as simple_spread
except Exception:
    from pettingzoo.mpe import simple_spread_v3 as simple_spread


class SimpleSpreadParallelAdapter:
    def __init__(
        self,
        n_agents: int = 3,
        max_cycles: int = 50,
        local_ratio: float = 0.5,
        continuous_actions: bool = True,
        seed: int = 0,
    ) -> None:
        self.n_agents = int(n_agents)
        self.max_cycles = int(max_cycles)
        self.local_ratio = float(local_ratio)
        self.continuous_actions = bool(continuous_actions)
        self.seed = int(seed)
        self.env = simple_spread.parallel_env(
            N=self.n_agents,
            max_cycles=self.max_cycles,
            local_ratio=self.local_ratio,
            continuous_actions=self.continuous_actions,
        )
        self.agent_names: List[str] = []
        self.obs_dim = None
        self.act_dim = None

    def reset(self, seed: int | None = None) -> np.ndarray:
        use_seed = self.seed if seed is None else int(seed)
        obs_dict, _ = self.env.reset(seed=use_seed)
        self.agent_names = list(self.env.agents)
        obs_list = [np.asarray(obs_dict[name], dtype=np.float32) for name in self.agent_names]
        obs = np.stack(obs_list, axis=0)
        if self.obs_dim is None:
            self.obs_dim = int(obs.shape[-1])
            sample_space = self.env.action_space(self.agent_names[0])
            self.act_dim = int(np.prod(sample_space.shape))
        return obs

    def step(self, actions: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, Dict]:
        action_dict: Dict[str, np.ndarray] = {}
        for i, agent in enumerate(self.agent_names):
            raw = np.asarray(actions[i], dtype=np.float32)
            mapped = np.clip((raw + 1.0) * 0.5, 0.0, 1.0)
            action_dict[agent] = mapped

        next_obs_dict, rewards, terminations, truncations, infos = self.env.step(action_dict)
        alive_agents = list(self.env.agents)

        next_obs = np.zeros((len(self.agent_names), self.obs_dim), dtype=np.float32)
        reward_local = np.zeros((len(self.agent_names),), dtype=np.float32)
        done = np.ones((len(self.agent_names),), dtype=np.float32)
        for i, agent in enumerate(self.agent_names):
            if agent in next_obs_dict:
                next_obs[i] = np.asarray(next_obs_dict[agent], dtype=np.float32)
            reward_local[i] = float(rewards.get(agent, 0.0))
            done[i] = 1.0 if (terminations.get(agent, False) or truncations.get(agent, False)) else 0.0

        reward_global = np.asarray([reward_local.mean()], dtype=np.float32)
        info = {
            "alive_agents": alive_agents,
            "rewards": rewards,
            "terminations": terminations,
            "truncations": truncations,
            "infos": infos,
        }
        return next_obs, reward_local, reward_global, done, info

    def close(self) -> None:
        self.env.close()
