# forge-api

[![Python Version](https://img.shields.io/badge/python-3.14-blue.svg)](https://www.python.org/downloads/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![ty](https://img.shields.io/badge/ty-checked-blue)](https://github.com/astral-sh/ty)

Minecraft inspired Game Logic API

## Table of Contents

- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Development](#development)
- [Linting & Development](#linting--formatting)
- [Type Checking](#type-checking)
- [License](#license)
- [Contact](#contact)

## Prerequisites

- Python 3.14+
- Install UV from Astral.sh

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Quick Start

```bash
# Clone repository
git clone https://github.com/mstvb/forge-api.git
cd your-project

# Create virtual environment and install dependencies
uv sync --dev

# Run tests
uv run pytest

# Check linting
uv run ruff check .

# Format code
uv run ruff format .

# Type checking (ty)
uv run ty check
```

## Development

```bash
# Create development environment
uv sync --dev

# Activate environment (optional)
uv shell

# Or run directly with uv
uv run python -m your_project
```

## Linting & Formatting

```bash
# Check code style (Ruff)
uv run ruff check .

# Auto-fix issues
uv run ruff check --fix .

# Format code (Ruff Format)
uv run ruff format .

# Show diff without changes
uv run ruff format . --diff
```

## Type Checking

```bash
# Run types checker (beta as of 2026)
uv run ty check

# Check specific files
uv run ty check src/module.py

# Show detailed output
uv run ty check --output-format=json

# Check with strict settings (when available)
uv run ty check --strict
```

## License

> This Project is licensed with [MIT](LICENSE)

## Contact

> Manuel Staufer (mstvb)
* [Github](https://github.com/mstvb)
* [Email](mailto::mstvb@proton.me)