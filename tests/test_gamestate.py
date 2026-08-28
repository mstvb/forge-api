import pytest

from src.core.gamestate import GameState, GameStateManager, GameStates


class DummyState(GameState):
    """Concrete GameState for testing that records start/stop calls."""
    def __init__(self, name: str = "", ty: GameStates = GameStates.DEFAULT):
        super().__init__(name=name, type=ty)

    def start(self):
        pass

    def stop(self):
        pass

@pytest.fixture
def sample_state() -> DummyState:
    """Fixture for sample state."""
    return DummyState(name="run", ty=GameStates.DEFAULT)


@pytest.fixture
def sample_manager() -> GameStateManager:
    """Fixture for GameStateManager creation."""
    return GameStateManager()


@pytest.mark.unit
class TestGameState:
    """Tests for GameState creation and management methods."""

    def test_add_state(self, sample_state: GameState, sample_manager: GameStateManager):
        """Add a state to the game state."""
        assert sample_manager.get_states() == [] # Before Adding State
        sample_manager.add_state(sample_state)
        assert sample_manager.get_states() == [sample_state] # With Added State

    def test_set_state(self, sample_state: GameState, sample_manager: GameStateManager):
        """Set a state to the game state."""
        sample_manager.add_state(sample_state)
        sample_manager.set_state(0)
        assert sample_manager.get_state() == sample_state # With State Set

    def test_start_state(self, sample_state: GameState,
                         sample_manager: GameStateManager):
        """Start a state to the game state."""
        sample_manager.add_state(sample_state)
        sample_manager.set_state(0, True)

    def test_stop_state(self, sample_state: GameState,
                        sample_manager: GameStateManager):
        """Stop a state to the game state."""
        sample_manager.add_state(sample_state)
        sample_manager.set_state(0, True)
        sample_manager.stop_state()
