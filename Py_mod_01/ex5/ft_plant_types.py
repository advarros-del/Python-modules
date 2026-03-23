class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    def __init__(
            self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        print(f"{self.name} is not bloomed yet!")
        print(f"[asking the {self.name} to bloom]")
        self.show()
        print(f" {self.name} is blooming beautifully!")

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        print(f" Color: {self.color}")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self, value: int):
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} produces shade of "
              f"{value} long and {self.trunk_diameter}cm wide")

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
        self, name: str, height:
        int, age: int, harvest_season: str,
        nutritional_value: int
    ):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def age_plant(self, value: int) -> None:
        print(f"[make the {self.name} grow and age for {value} days]")
        self.age += value
        self.nutritional_value += value
        self.grow(value)
        self.show()

    def grow(self, value: float) -> None:
        self.height = round((self.height + value) * 1.9)

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")
    f1 = Flower("Rose", 15, 10, "red")
    t1 = Tree("Oak", 200, 365, 5)
    v1 = Vegetable("Tomato", 5, 10, "April", 0)
    print("=== Flower")
    f1.show()
    f1.bloom()
    print("\n=== Tree")
    t1.show()
    t1.produce_shade(200)
    print("\n=== Vegetable")
    v1.show()
    v1.age_plant(20)


if __name__ == "__main__":
    main()
