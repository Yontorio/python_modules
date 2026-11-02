from abc import ABC, abstractmethod

from ex0.creatures import Creature
from ex1.creatures import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    """Raised when a strategy is used with an incompatible creature."""


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Return whether this strategy supports the creature."""

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        """Perform this strategy's actions."""


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> list[str]:
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this "
                "aggressive strategy"
            )
        capability = creature
        if not isinstance(capability, TransformCapability):
            raise InvalidStrategyError("Creature cannot transform")
        return [
            capability.transform(),
            capability.attack(),
            capability.revert(),
        ]


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this "
                "defensive strategy"
            )
        capability = creature
        if not isinstance(capability, HealCapability):
            raise InvalidStrategyError("Creature cannot heal")
        return [capability.attack(), capability.heal()]
