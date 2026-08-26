# Contributing Guide

Thank you for your interest in contributing to this project! We welcome contributions from everyone. Please read these guidelines to help make the contribution process smooth and effective.

## Quick Start

### Prerequisites

- **Python** | Python 3.14 or higher | [python](https://python.com/)
- **UV** | Package Management | [uv](https://github.com/astral-sh/uv)
- **Ruff** | Linter | [ruff](https://github.com/astral-sh/ruff)
- **TY** | Type Checker | [ty](https://github.com/astral-sh/ty)
- **Git** | Version Control | [Git](https://git-scm.com)

### Getting Started

```bash
# Clone Repository
git clone https://github.com/mstvb/forge-api
cd forge-api

# Create & Active Virtual Environment (.venv)
uv venv
source .venv/bin/activate  # Unix
.venv\Scripts\activate     # Windows

# Install Dependencies for Development
uv sync --dev