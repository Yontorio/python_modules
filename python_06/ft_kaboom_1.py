#!/usr/bin/env python3

def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    print("Testing record dark spell: ", end="")
    print(dark_spell_record("Doom", "bats and eyeball"))


if __name__ == "__main__":
    main()
