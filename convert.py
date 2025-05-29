import toml

with open('pyproject.toml', 'r') as f:
    pyproject = toml.load(f)

dependencies = pyproject['project']['dependencies']
optional_dependencies = pyproject['project']['optional-dependencies']['dev']

with open('requirements.txt', 'w') as f:
    for dep in dependencies:
        f.write(dep + '\n')
    for dep in optional_dependencies:
        f.write(dep + '\n')