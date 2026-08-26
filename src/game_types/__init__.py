# src/game_types/__init__.py
"""Module of Forge Types"""

# Project Imports
from src.game_types.inventory_type import InventoryType
from src.game_types.item_type import ItemType

__all__: list[str] = ["InventoryType", "ItemType"]
