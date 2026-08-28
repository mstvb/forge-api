from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import StrEnum, auto


class GameStates(StrEnum):

    DEFAULT = auto()
    INGAME = auto()
    PAUSE = auto()


@dataclass
class GameState(ABC):
    """Abstract Class for Game States."""
    name: str = field(default_factory=str)
    type: GameStates = field(default=GameStates.DEFAULT)

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def get_name(self) -> str:
        return self.name

    def get_type(self) -> GameStates:
        return self.type


@dataclass
class GameStateManager:
    """Manager for Game States"""
    states: list[GameState] = field(default_factory=list)
    current: GameState | bool = field(default=False)

    def add_state(self, state: GameState) -> int:
        self.states.append(state)
        return self.states.count(state)

    def set_state(self, i: int, auto_start: bool = False) -> bool:
        if self.states[i]:
            self.current: GameState = self.states[i]
            if auto_start:
                self.current.start()
            return True
        else:
            return False

    def start_state(self) -> bool:
        if isinstance(self.current, GameState):
            self.current.start()
            return True
        else:
            return False

    def stop_state(self) -> bool:
        if isinstance(self.current, GameState):
            self.current.stop()
            return True
        else:
            return False

    def get_state(self) -> GameState | bool:
        return self.current

    def get_states(self) -> list[GameState]:
        return self.states
