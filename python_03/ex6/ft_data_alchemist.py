#!/usr/bin/env python3

from random import randint

PLAYERS: list[str] = [
    "Alice", "bob", "Achraf", "Charlie", "dylan",
    "Emma", "Gregory", "john", "kevin", "Liam",
]


def main() -> None:
    print("=== Game Data Alchemist ===")
    print(f"\nInitial list of players: {PLAYERS}")

    cap: list[str] = [name.capitalize() for name in PLAYERS]
    print(f"New list with all names capitalized: {cap}")

    init_cap: list[str] = [name for name in PLAYERS if name == name.capitalize()]
    print(f"New list of capitalized names only: {init_cap}")


    scores: dict[str, int] = {name: randint(1, 1000) for name in cap}
    print(f"\nScore dict: {scores}")

    avg: float = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {avg}")

    above: dict[str, int] = {n: s for n, s in scores.items() if s > avg}
    print(f"High scores: {above}")


if __name__ == "__main__":
    main()
