class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1

    def age_plant(self) -> None:
        self.age += 1

    def ft_plant_growth(self) -> None:
        days: int = 1
        g: int = -1
        print("=== Garden Plant Growth ===")
        for days in range(1, 8):
            print(f"=== DAY {days} ===")
            print(f"{self.name}: {self.height}cm, {self.age} days old.")
            self.grow()
            self.age_plant()
            g += 1
        if days == 7:
            print(f"Growth this week: {g}cm!")


def main() -> None:
    p1 = Plant("Rose", 25, 30)
    p1.ft_plant_growth()


if __name__ == "__main__":
    main()
