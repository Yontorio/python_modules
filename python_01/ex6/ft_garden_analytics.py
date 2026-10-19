#!/usr/bin/env python3

class Plant:
    class Statistics:
        def __init__(self) -> None:
            self.__grow_count = 0
            self.__age_count = 0
            self.__show_count = 0

        def record_grow(self) -> None:
            self.__grow_count += 1

        def record_age(self) -> None:
            self.__age_count += 1

        def record_show(self) -> None:
            self.__show_count += 1

        def display(self) -> None:
            print(
                f"Stats: {self.__grow_count} grow, "
                f"{self.__age_count} age, "
                f"{self.__show_count} show"
            )

    def __init__(self, name: str, height: float,
                    age: int, growth_rate: float = 0.42) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self._growth_rate = 0.42
        self._statistics = Plant.Statistics()

        self.set_height(height)
        self.set_age(age)
        self.set_growth_rate(growth_rate)

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(class_) -> "Plant":
        return class_("Unknown plant", 0.0, 0)

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
        self._statistics.record_show()
        print(
            f"{self.name}: {round(self.get_height(), 1)}cm, "
            f"{self.get_age()} days old"
        )

    def grow(self) -> None:
        self.set_height(self._height + self._growth_rate)
        self._statistics.record_grow()

    def age(self) -> None:
        self.set_age(self._age + 1)
        self._statistics.record_age()

    def display_statistics(self) -> None:
        self._statistics.display()


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
        self.__shade_count = 0

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{round(self._height, 1)}cm long and "
            f"{round(self.trunk_diameter, 1)}cm wide."
        )
        self.__shade_count += 1

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def display_statistics(self) -> None:
        super().display_statistics()
        print(f"{self.__shade_count} shade")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                    color: str, growth_rate: float = 0.42) -> None:
        super().__init__(name, height, age, color, growth_rate)
        self.__seed_count = 0

    def get_seed_count(self) -> int:
        return self.__seed_count

    def set_seed_count(self, seed_count: int) -> None:
        if self._bloomed:
            self.__seed_count = seed_count
        else:
            print(f"{self.name} can't hold seeds right now, it hasn't bloomed yet!")

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.get_seed_count()}")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str, growth_rate: float = 0.42) -> None:
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


def display_plant_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.display_statistics()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(
        "Is 30 days more than a year? ->",
        Plant.is_older_than_year(30)
    )
    print(
        "Is 400 days more than a year? ->",
        Plant.is_older_than_year(400)
    )

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red", 8.0)
    rose.show()
    display_plant_statistics(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_plant_statistics(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_statistics(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.bloom()
    sunflower.set_seed_count(42)
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.set_growth_rate(30.0)
    sunflower.grow()
    sunflower.age()
    sunflower.set_age(65)
    sunflower.bloom()
    sunflower.show()
    display_plant_statistics(sunflower)

    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_plant_statistics(anonymous)


if __name__ == "__main__":
    main()
