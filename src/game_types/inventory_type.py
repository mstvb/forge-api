from enum import StrEnum, auto


class SlotType(StrEnum):

    CRAFTING = auto()
    FUEL = auto()
    ARMOR = auto()
    RESULT = auto() # Crafting Result (Furnace etc ... )
    CONTAINER = auto()


class InventoryType(StrEnum):

    PLAYER = auto()
    CHEST = auto()
