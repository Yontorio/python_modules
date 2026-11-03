#!/usr/bin/env python3

from ex0 import CreatureFactory, AquaFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)


def _strategy_name(strategy: BattleStrategy) -> str:
    return strategy.__class__.__name__.replace("Strategy", "").lower()


def _fight(
    first_factory: CreatureFactory,
    first_strategy: BattleStrategy,
    second_factory: CreatureFactory,
    second_strategy: BattleStrategy,
) -> None:
    creature_one = first_factory.create_base()
    creature_two = second_factory.create_base()

    print("\n* Battle *")
    print(creature_one.describe())
    print(" vs.")
    print(creature_two.describe())
    print(" now fight!")

    # if not first_strategy.is_valid(creature_one):
    #     raise InvalidStrategyError(
    #         f"Invalid Creature '{creature_one.name}' for this "
    #         f"{_strategy_name(first_strategy)} strategy"
    #     )

    # if not second_strategy.is_valid(creature_two):
    #     raise InvalidStrategyError(
    #         f"Invalid Creature '{creature_two.name}' for this "
    #         f"{_strategy_name(second_strategy)} strategy"
    #     )

    for action in first_strategy.act(creature_one):
        print(action)

    for action in second_strategy.act(creature_two):
        print(action)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    try:
        for index, (first_factory, first_strategy) in enumerate(opponents):
            for second_factory, second_strategy in opponents[index + 1:]:
                _fight(
                    first_factory,
                    first_strategy,
                    second_factory,
                    second_strategy,
                )
    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")


def main() -> None:
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])

    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])

    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), "
          "(Transform+Aggressive) ]")
    battle([
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ])


if __name__ == "__main__":
    main()
