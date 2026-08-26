import pytest

from src.core.api import API


@pytest.fixture
def sample_api() -> API:
    """Fixture providing a sample API instance for tests."""
    return API("default-game", "Default test game", [])


@pytest.mark.unit
class TestAPICreation:
    """Tests for API object creation and basic properties."""

    def test_api_name(self, sample_api: API) -> None:
        """API should store and return correct name."""
        assert sample_api.get_name() == "default-game"

    def test_api_description(self, sample_api: API) -> None:
        """API should store and return correct description."""
        assert sample_api.get_description() == "Default test game"

    def test_api_modules(self, sample_api: API) -> None:
        """API should store and return correct modules."""
        assert sample_api.get_modules() == []
