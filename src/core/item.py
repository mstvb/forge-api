from dataclasses import dataclass, field

from src.game_types.item_type import ItemType


@dataclass
class Item:
    """Custom API for Items

    Parameters
    ----------
    name : str, optional
        Item Name
    type : InventoryType, optional
        Item Type

    Attributes
    ----------
    name : str
        Item Name
    type : InventoryType
        Item Type

    Examples
    --------
    >>> item = Item(name="Compass", type=ItemType.TOOL)
    >>> item.get_name()
    'Compass'
    """

    name: str = field(default_factory=str)
    type: ItemType = ItemType.TOOL

    def get_name(self) -> str:
        return self.name

    def get_type(self) -> ItemType:
        return self.type
