#!/usr/bin/env python3

import random

ACHIEVEMENTS: list[str] = [
    "First Steps",
    "Master Explorer",
    "Boss Slayer",
    "Speed Runner",
    "Collector Supreme",
    "Crafting Genius",
    "World Savior",
    "Untouchable",
    "Strategist",
    "Survivor",
    "Treasure Hunter",
    "Sharp Mind",
    "Unstoppable",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    length: int = len(ACHIEVEMENTS)
    magic_num: int = length // 3
    random_num: int = random.randint(magic_num, length - magic_num)
    return set(random.sample(ACHIEVEMENTS, random_num))


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    players: list[tuple[str, set[str]]] = []
    names: list[str] = ["Alice", "Bob", "Charlie", "Dylan"]
    for i in range(len(names)):
        players.append((names[i], gen_player_achievements()))
        print(f"Player {players[i][0]}: {players[i][1]}")
    players_union: set[str] = set()
    players_intersection: set[str] = set(ACHIEVEMENTS)
    for player in players:
        players_union = players_union.union(player[1])
        players_intersection = players_intersection.intersection(player[1])
    print(f"\nAll distinct achievements: {players_union}")
    print(f"\nCommon achievements: {players_intersection}\n")
    for player in players:
        others_union: set[str] = set()
        for other_player in players:
            if other_player[0] != player[0]:
                others_union = others_union.union(other_player[1])
        unique: set[str] = player[1].difference(others_union)
        print(f"Only {player[0]} has: {unique}")
    print()
    all_set: set[str] = set(ACHIEVEMENTS)
    for player in players:
        missing: set[str] = all_set.difference(player[1])
        print(f"{player[0]} is missing: {missing}")


if __name__ == "__main__":
    main()
