# src/__init__.py
"""Forge API"""

# Imports
import tomllib

# Project Imports
from src.core import GameState, GameStateManager, GameStates

__all__: list[str] = ["GameState", "GameStateManager", "GameStates"] # Imported Objects

__modules__: list[str] = ["core"] # Project Modules

def load() -> None:
    """Load Project File"""
    with open("../pyproject.toml", "rb") as file:
        project_data = tomllib.load(file)

    # Project Information
    __project__: str = project_data['project']['name'] or "forge-api"
    __version__: str = project_data['project']['version'] or "v0.1"
    __authors__: str = project_data['project']['authors'] or "Manuel Staufer"
    __maintainers__: list[str] = project_data['project']['maintainers'] or []

    if __modules__:
        print("-- Modules --")
        for m in __modules__:
            print(f"{m} \n")

    print("-- Project Info --")

    print(f"{__project__} \n - " +
          f"v{__version__} loaded")

    print(f"developed by {__authors__}\n")

    if __maintainers__:
        print("-- Maintainers --")
        for member in __maintainers__:
            print(member)

if __name__ == "__main__":
    load()
