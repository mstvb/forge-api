# src/__init__.py
"""Forge API"""

# Project Imports
from src.core import API, Inventory, Item
from src.game_types import EntityType, InventoryType, ItemType

__all__: list[str] = ["Inventory", "API", "Item",
                      "EntityType", "InventoryType", "ItemType"]

__modules__: list[str] = ["core", "game-types", "plugins", "utils"]

__project__: str = "forge-api"
__version__: str = "0.1"
__author__: str = "Manuel Staufer"

def get_name() -> str:
    """Returns Name of Package."""
    return __name__

def get_version() -> str:
    """Returns Version of Package."""
    return __version__

def get_author() -> str:
    """Returns Name of Author."""
    return __author__

if __name__ == "__main__":
    print("-- Modules --")
    print(f"{__modules__}\n")
    print("-- Project Info --")
    print(f"{__project__} - v{__version__} loaded")
    print(f"developed by {__author__}")
