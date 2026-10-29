#!/usr/bin/env python3

from alchemy.potions import healing_potion, strength_potion


def main() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print("Testing strength_potion:", strength_potion())
    print("Testing healing_potion:", healing_potion())


if __name__ == "__main__":
    main()
