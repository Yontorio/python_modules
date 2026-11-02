from ex0 import CreatureFactory
from ex2 import BattleStrategy, InvalidStrategyError


def battle(
    opponents: list[tuple[CreatureFactory, BattleStrategy]],
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    creatures = [
        (factory.create_base(), strategy) for factory, strategy in opponents
    ]
    for index, (first, first_strategy) in enumerate(creatures):
        for second, second_strategy in creatures[index + 1:]:
            print("* Battle *")
            print(f"{first.describe()} vs. {second.describe()} now fight!")
            try:
                for action in first_strategy.act(first):
                    print(action)
                for action in second_strategy.act(second):
                    print(action)
            except InvalidStrategyError as error:
                print(f"Battle error, aborting tournament: {error}")
                return
