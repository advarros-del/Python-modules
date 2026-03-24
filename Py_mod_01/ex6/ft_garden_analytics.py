class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age
        self.n_grow: int = 0
        self.n_age: int = 0
        self.n_show: int = 0

    def age_plant(self, value: int) -> None:
        self.age += value
        self.n_age += 1

    def grow(self, value: int) -> None:
        self.height = (self.height + value)
        self.n_grow += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        self.n_show += 1

    @staticmethod
    def is_year(n: int) -> None:
        if n < 365:
            print(f"Is {n} days more than a year? -> True")
        else:
            print(f"Is {n} days more than a year? -> False")

    @classmethod
    def unknown_plant(cls, height: int, age: int) -> "Plant":
        return cls("Unknown", height, age)


class Flower(Plant):
    def __init__(
            self, name: str, height: int,
            age: int, color: str, blooming: bool = False):
        super().__init__(name, height, age)
        self.color: str = color
        self.blooming: bool = blooming

    def bloom(self) -> None:
        if self.blooming is False:
            print(f"{self.name} is not bloomed yet!")
            self.blooming = True
        else:
            print(f" {self.name} is blooming beautifully!")

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        print(f" Color: {self.color}")
        self.n_show += 1


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter
        self.n_shade: int = 0

    def produce_shade(self, value: int) -> None:
        print(f"Tree {self.name} produces shade of "
              f"{value}cm long and {self.trunk_diameter}cm wide")
        self.n_shade += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        print(f" Trunk diameter: {self.trunk_diameter}cm")
        self.n_show += 1


class Seed(Flower):
    def __init__(
        self, name: str, height: int, age: int, color: str, n_seeds: int
    ):
        super().__init__(name, height, age, color)
        self.n_seeds = n_seeds

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        print(f" Color: {self.color}")
        self.n_show += 1

    def bloom(self) -> None:
        if self.blooming is False:
            print(f"{self.name} is not bloomed yet!")
            print("Seeds: 0")
            self.blooming = True
        else:
            print(f" {self.name} is blooming beautifully!")
            print(f"Seeds: {self.n_seeds}")


def print_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    print(f"Stats : {plant.n_grow} grow,"
          f" {plant.n_age} age, {plant.n_show} show")


def main() -> None:
    print("=== Garden Statistics ===\n")
    Plant.is_year(30)
    Plant.is_year(400)
    f1 = Flower("Rose", 15, 10, "red", False)
    t1 = Tree("Oak", 200, 365, 5)
    s1 = Seed("Sunflower", 80, 45, "yellow", 42)
    print("\n=== Flower")
    f1.show()
    f1.bloom()
    print_statistics(f1)
    print(f"[asking the {f1.name} to grow and bloom]")
    f1.grow(7)
    f1.show()
    f1.bloom()
    print_statistics(f1)
    print("\n=== Tree")
    t1.show()
    print_statistics(t1)
    print(f" {t1.n_shade} shade")
    print(f"[asking the {t1.name} to produce shade]")
    t1.produce_shade(200)
    print_statistics(t1)
    print(f" {t1.n_shade} shade")
    print("\n=== Seed")
    s1.show()
    s1.bloom()
    print(f"[make {s1.name} grow, age and bloom]")
    s1.grow(30)
    s1.age_plant(20)
    s1.show()
    s1.bloom()
    print_statistics(s1)
    print("\n=== Anonymous")
    a1 = Plant.unknown_plant(0, 0)
    a1.show()
    print_statistics(a1)


if __name__ == "__main__":
    main()
