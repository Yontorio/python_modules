#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw_input: str = input(
            "Enter new coordinates as floats in format 'x,y,z': ")
        parts: list[str] = raw_input.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        coordinates: list[float] = []
        for part in parts:
            stripped: str = part.strip()
            try:
                coordinates.append(float(stripped))
            except ValueError:
                print(f"Error on parameter '{stripped}': "
                      f"could not convert string to float: '{stripped}'")
                break
        else:
            return (coordinates[0], coordinates[1], coordinates[2])


def distance(p1: tuple[float, float, float],
             p2: tuple[float, float, float]) -> float:
    return math.sqrt(
        (p2[0] - p1[0]) ** 2 +
        (p2[1] - p1[1]) ** 2 +
        (p2[2] - p1[2]) ** 2)


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    first: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")
    origin: tuple[float, float, float] = (0.0, 0.0, 0.0)
    print(f"Distance to center: {round(distance(origin, first), 4)}")
    print("Get a second set of coordinates")
    second: tuple[float, float, float] = get_player_pos()
    print(f"Distance between the 2 sets of coordinates:"
          f" {round(distance(first, second), 4)}")


if __name__ == "__main__":
    main()
