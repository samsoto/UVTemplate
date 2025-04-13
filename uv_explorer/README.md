## Create Virtual Environment

```sh
uv venv .venv --python 3.12
```

## Create Projects
https://docs.astral.sh/uv/concepts/projects/init

## Create Packaged Applications
```sh
uv init --package example-pkg
```

## Crete Libraries
```sh
uv init --lib example-lib
```

## Install Tools
```sh
uv tool install ruff
```

## Run Tool
```sh
uvx ruff check
```

## VS Code Environment

Add `.vscode/setting.json` to the top level root directory

```json
{
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}
```

Add `.vscode/setting.json` to the project level directory
```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
    "python.envFile": "${workspaceFolder}/.env",
    "python.analysis.extraPaths": [
        "${workspaceFolder}/src",
    ],
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        "tests",
        "-p",
        "test_*.py"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true,
    "python.testing.cwd": "${workspaceFolder}/tests",
    "python.testing.autoTestDiscoverOnSaveEnabled": true,
    "python.testing.pytestArgs": [
        "uv_explorer"
    ],
}
```

Add `.env` at the project level directory
```env
PYTHONPATH=${workspaceFolder}/src
```

# Editable mode

```sh
uv pip install -e .
```

## Ruff

```sh
uvx ruff format
```