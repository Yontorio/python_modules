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


def main() -> None:
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)
    print("Plant created:", end=" ")
    rose.show()

    if rose.set_height(25.0):
        print(f"Height updated: {round(rose.get_height(), 1)}cm")

    if rose.set_age(30):
        print(f"Age updated: {rose.get_age()} days")

    if not rose.set_height(-5):
        print("Height update rejected")

    if not rose.set_age(-3):
        print("Age update rejected")

    print("Current state:", end=" ")
    rose.show()


if __name__ == "__main__":
    main()
