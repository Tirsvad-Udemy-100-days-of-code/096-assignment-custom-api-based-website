# Setup

How to prepare a local environment, run the checks and publish safely.

## Requirements

- Python 3.14 or newer. Check with `python --version` (on Windows, `py -3.14 --version`).
- Doxygen, to build the API documentation (optional).

## Create and use a local `.venv`

Windows (PowerShell):

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux and macOS:

```bash
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Leave the environment with `deactivate`. The `.venv` folder is ignored by git.

## Run the checks

```bash
python -m pytest
python -m ruff check src tests
python -m mypy src
doxygen Doxyfile
```

The Doxygen output goes to `docs/doxygen/`, which is ignored by git.

## Static analysis before a push

Run opengrep locally before every push:

```powershell
& "$HOME\.opengrep\cli\latest\opengrep.exe" scan --config auto --error src tests
```

Fix every finding before pushing.

## Secrets

The `.env` file holds personal tokens for the git host. It is ignored by git and
is never read, imported or tested by the project.
