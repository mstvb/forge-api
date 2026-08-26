from dataclasses import dataclass, field


@dataclass
class API:
    """Custom API for game logic.

    Parameters
    ----------
    name : str, optional
        Name of the inventory (default is empty string).
    description : str, optional
        Description of the inventory (default is empty string).
    modules : list[str], optional
        List of module names from Forge (default is empty list).

    Attributes
    ----------
    name : str
        Name of the inventory.
    description : str
        Description of the inventory.
    modules : list[str]
        List of module names from Forge.

    Examples
    --------
    >>> api = API(name="MyGame", description="A cool game")
    >>> api.get_name()
    'MyGame'
    """

    name: str = field(default_factory=str)
    description: str = field(default_factory=str)
    modules: list[str] = field(default_factory=list)

    def get_name(self) -> str:
        """Return the name of the inventory."""
        return self.name

    def get_description(self) -> str:
        """Return the description of the inventory."""
        return self.description

    def get_modules(self) -> list[str]:
        """Return the list of modules."""
        return self.modules
