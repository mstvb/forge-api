import pytest

from src.core.inventory import Inventory
from src.game_types.inventory_type import InventoryType


@pytest.fixture
def sample() -> Inventory:
    """Fixture for creating a sample Inventory object"""
    return Inventory("Default", InventoryType.PLAYER, "Player", [])

@pytest.mark.unit
class TestInventoryCreation:
    """Tests for the Inventory object creation and basic properties"""

    def test_inventory_name(self, sample: Inventory) -> None:
        """Inventory should store and return the correct name"""
        assert sample.name == "Default"

    def test_inventory_type(self, sample: Inventory) -> None:
        """Inventory should store and return the correct type"""
        assert sample.type == InventoryType.PLAYER

    def test_inventory_owner(self, sample: Inventory) -> None:
        """Inventory should store and return the correct owner"""
        assert sample.owner == "Player"

    def test_inventory_slots(self, sample: Inventory) -> None:
        """Inventory should store and return the correct slots"""
        assert sample.slots == []
