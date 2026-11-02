from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def test_healing(factory: HealingCreatureFactory) -> None:
    for label, creature in (
        ("base", factory.create_base()),
        ("evolved", factory.create_evolved()),
    ):
        print(f"{label}: {creature.describe()}")
        print(creature.attack())
        if isinstance(creature, HealCapability):
            print(creature.heal())


def test_transforming(factory: TransformCreatureFactory) -> None:
    for label, creature in (
        ("base", factory.create_base()),
        ("evolved", factory.create_evolved()),
    ):
        print(f"{label}: {creature.describe()}")
        print(creature.attack())
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    test_healing(HealingCreatureFactory())
    print("Testing Creature with transform capability")
    test_transforming(TransformCreatureFactory())
