#!/usr/bin/env python3

from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(first_factory: CreatureFactory,
                second_factory: CreatureFactory) -> None:
    print("Testing battle")
    first = first_factory.create_base()
    second = second_factory.create_base()
    print(first.describe())
    print(" vs.")
    print(second.describe())
    print(" fight!")
    print(first.attack())
    print(second.attack())


def main() -> None:
    test_factory(FlameFactory())
    print()
    test_factory(AquaFactory())
    print()
    test_battle(FlameFactory(), AquaFactory())


if __name__ == "__main__":
    main()
