from abc import ABC, abstractmethod

from .creatures import Aquabub, Creature, Flameling, Pyrodon, Torragon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        """Create the base creature for this family."""

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create the evolved creature for this family."""


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
