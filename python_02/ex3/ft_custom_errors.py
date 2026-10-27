#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, error: str = "Unknown garden error") -> None:
        super().__init__(error)


class PlantError(GardenError):
    def __init__(self, error: str = "Unknown plant error") -> None:
        super().__init__(error)


class WaterError(GardenError):
    def __init__(self, error: str = "Unknown water error") -> None:
        super().__init__(error)


def check_plant_status(plant_status: bool) -> None:
    if not plant_status:
        raise PlantError("The tomato plant is wilting!")
    print("The tomato plant is healthy!")


def check_water_tank(water_status: bool) -> None:
    if not water_status:
        raise WaterError("Not enough water in the tank!")
    print("The water tank is full!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        check_plant_status(False)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        check_water_tank(False)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    for action in (check_plant_status, check_water_tank):
        try:
            action(False)
        except GardenError as e:
            print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
