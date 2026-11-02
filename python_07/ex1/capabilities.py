from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        """Return this creature's healing message."""


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        """Transform this creature."""

    @abstractmethod
    def revert(self) -> str:
        """Revert this creature's transformation."""
