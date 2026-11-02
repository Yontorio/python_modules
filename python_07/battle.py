from ex0 import AquaFactory, CreatureFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(first_factory: CreatureFactory,
                second_factory: CreatureFactory) -> None:
    first = first_factory.create_base()
    second = second_factory.create_base()
    print(f"{first.describe()} vs. {second.describe()} fight!")
    print(first.attack())
    print(second.attack())


if __name__ == "__main__":
    print("Testing factory")
    test_factory(FlameFactory())
    test_factory(AquaFactory())
    print("Testing battle")
    test_battle(FlameFactory(), AquaFactory())
