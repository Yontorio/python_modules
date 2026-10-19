#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int, growth_rate: float = 0.42) -> None:
        self.name = name
        self.height = height
        self.age_ = age
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age_} days old")

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.age_ += 1

def main() -> None:
    plants = [
        Plant("Rose", 25.0, 30, 0.8),
        Plant("Oak", 200.0, 365, 1.5),
        Plant("Cactus", 5.0, 90, 0.2),
        Plant("Sunflower", 80.0, 45, 2.0),
        Plant("Fern", 15.0, 120, 0.5)
    ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created:", end=" ")
        plant.show()

    for _ in range(1, 8):
        for plant in plants:
            plant.grow()
            plant.age()

    print(">>> One Week Later <<<")
    for plant in plants:
        plant.show()

if __name__ == "__main__":
    main()
