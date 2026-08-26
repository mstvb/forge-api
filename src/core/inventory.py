from dataclasses import dataclass, field

from src.game_types.inventory_type import InventoryType


@dataclass
class Inventory:
    """Custom API for Inventory.

    Parameters
    ----------
    name : str, optional
        Name of the inventory (default is empty string).
    type : InventoryType, optional
        Inventory type (default is InventoryType.PLAYER).
    owner : str, optional
        Inventory owner username (default is empty string).
    slots : list[object], optional
        Content of Inventory

    Attributes
    ----------
    name : str
        Name of Inventory
    type : InventoryType
        Type of Inventory
    owner : str
        Owner of Inventory
    slots : list[object]
        Content of Inventory

    Examples
    --------
    >>> inv = Inventory(name="Default", type=InventoryType.PLAYER, owner="Player")
    >>> inv.get_name()
    'Default'
    """

    name: str = field(default_factory=str)
    type: InventoryType = InventoryType.PLAYER
    owner: str = field(default_factory=str)
    slots: list[object] = field(default_factory=list)

    def add_item(self, add_item) -> None:
        """Add Item to Inventory."""
        self.slots.append(add_item)

    def set_item(self, slot: int, set_item) -> object | bool:
        """Set Item to Inventory."""
        if slot < len(self.slots):
            self.slots[slot] = set_item
            return set_item
        else:
            return False

    def pop_item(self, slot: int) -> bool:
        """Remove Item from Inventory by Slot Integer."""
        if slot < len(self.slots):
            self.slots.pop(slot)
            return True
        else:
            return False

    def remove_item(self, remove_item) -> object | bool:
        """Remove Item from Inventory by Item Class."""
        if remove_item in self.slots:
            self.slots.remove(remove_item)
            return remove_item
        else:
            return False

    def get_slot(self, slot: int) -> object | bool:
        return self.slots[slot] if slot < len(self.slots) else False

    def get_name(self) -> str:
        """Returns Name of Inventory."""
        return self.name

    def get_type(self) -> InventoryType:
        """Returns Type of Inventory."""
        return self.type

    def get_owner(self) -> str:
        """Returns Owner of Inventory."""
        return self.owner

    def get_slots(self) -> list[object]:
        """Returns Slots of Inventory."""
        return self.slots
