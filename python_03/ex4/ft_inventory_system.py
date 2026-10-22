#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        parts: list[str] = arg.split(":")

        if (
            len(parts) != 2
            or not parts[0].strip()
            or not parts[1].strip()
        ):
            print(f"Error - invalid parameter '{arg}'")
            continue

        name: str = parts[0].strip()
        raw_quantity: str = parts[1].strip()

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            quantity: int = int(raw_quantity)
        except ValueError:
            print(f"Quantity error for '{name}': invalid quantity '{raw_quantity}'")
            continue

        inventory[name] = quantity

    print(f"Got inventory: {inventory}")

    if not inventory:
        print("Inventory is empty!")
    else:
        item_list: list[str] = list(inventory.keys())
        print(f"Item list: {item_list}")

        total: int = sum(inventory.values())
        count: int = len(inventory)
        print(f"Total quantity of the {count} items: {total}")

        for item_name in inventory:
            if total == 0:
                percent: float = 0.0
            else:
                percent = round(
                    inventory[item_name] / total * 100, 1
                )
            print(f"Item {item_name} represents {percent}%")

        most_name: str = item_list[0]
        least_name: str = item_list[0]

        for item_name in item_list[1:]:
            if inventory[item_name] > inventory[most_name]:
                most_name = item_name
            if inventory[item_name] < inventory[least_name]:
                least_name = item_name

        print(
            f"Item most abundant: {most_name} "
            f"with quantity {inventory[most_name]}"
        )
        print(
            f"Item least abundant: {least_name} "
            f"with quantity {inventory[least_name]}"
        )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
