#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float,
                 age: int, growth_rate: float = 0.42) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self._growth_rate = 0.42

        self.set_height(height)
        self.set_age(age)
        self.set_growth_rate(growth_rate)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return False
        self._height = height
        return True

    def set_age(self, age: int) -> bool:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            return False
        self._age = age
        return True

    def set_growth_rate(self, growth_rate: float) -> bool:
        if growth_rate < 0:
            print(f"{self.name}: Error, growth rate can't be negative")
            return False
        self._growth_rate = growth_rate
        return True

    def show(self) -> None:
        print(f"{self.name}: "
              f"{round(self.get_height(), 1)}cm, "
              f"{self.get_age()} days old")

    def grow(self) -> None:
        self.set_height(self._height + self._growth_rate)

    def age(self) -> None:
        self.set_age(self._age + 1)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str, growth_rate: float = 0.42) -> None:
        super().__init__(name, height, age, growth_rate)
        self.color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float, growth_rate: float = 0.42) -> None:
        super().__init__(name, height, age, growth_rate)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{round(self._height, 1)}cm long and "
            f"{round(self.trunk_diameter, 1)}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, growth_rate: float = 0.42) -> None:
        super().__init__(name, height, age, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = 0
        self._nut_age_sync = False
        self._nut_grow_sync = False

    def _increase_nutrition(self) -> None:
        if self._nut_age_sync and self._nut_grow_sync:
            self.nutritional_value += 1
            self._nut_age_sync = False
            self._nut_grow_sync = False

    def grow(self) -> None:
        super().grow()
        self._nut_grow_sync = True
        self._increase_nutrition()

    def age(self) -> None:
        super().age()
        self._nut_age_sync = True
        self._increase_nutrition()

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 2.1)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    main()
