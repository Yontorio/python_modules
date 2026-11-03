#!/usr/bin/env python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def test_healing(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")

    creatures = [
        ("Base", factory.create_base()),
        ("Evolved", factory.create_evolved()),
    ]

    for label, creature in creatures:
        print(f" {label}:")
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, HealCapability):
            print(creature.heal())


def test_transforming(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")

    creatures = [
        ("Base", factory.create_base()),
        ("Evolved", factory.create_evolved()),
    ]

    for label, creature in creatures:
        print(f" {label}:")
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())


def main() -> None:
    test_healing(HealingCreatureFactory())
    print()
    test_transforming(TransformCreatureFactory())


if __name__ == "__main__":
    main()
