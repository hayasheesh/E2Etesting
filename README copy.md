# tektometesting
Repository contain tektome platform testing framework for UI, API and Database


# Installation

## Setup ChromeDriver on Linux

1. Update your system’s package list:

```bash
sudo apt-get update
```

2. Download and install the Google Chrome .deb package:

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
```

3. Fix any missing dependencies (if needed):

```bash
sudo apt --fix-broken install
```

4. Verify the installation:
    
```bash
google-chrome --version
```


## Install the package
```bash
pip install -e .
```

## Development setup

For developers use the following command:

```bash
pip install '.[dev]'
```

or 

```bash
pip install .[dev]
```

Next setup prec-commit hooks:

```bash
pre-commit install
pre-commit run --all-files
```


# Usage

To run `demo.py` file, use the following command:

```bash
python -m src.dummy.demo
```