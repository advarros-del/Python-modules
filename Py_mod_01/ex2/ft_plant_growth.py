class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1

    def age_plant(self) -> None:
        self.age += 1

    def ft_plant_growth() -> None:
        p1 = Plant(
            name="Rose",
            height=25,
            age=30,
        )
        days: int = 1
        g: int = -1
        print("=== Garden Plant Growth ===")
        for days in range(1, 8):
            print(f"=== DAY {days} ===")
            print(f"{p1.name}: {p1.height}cm, {p1.age} days old.")
            p1.grow()
            p1.age_plant()
            g += 1
        if days == 7:
            print(f"Growth this week: {g}cm!")


def main():
    Plant.ft_plant_growth()


if __name__ == "__main__":
    main()
