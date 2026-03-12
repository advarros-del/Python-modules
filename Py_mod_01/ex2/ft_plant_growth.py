def ft_plant_growth() -> None:
    class Plant:
        def __init__(self, name: str, height: int, age: int):
            self.name = name
            self.height = height
            self.age = age
    p1 = Plant(
        name="Rose",
        height=25,
        age=30,
    )
    p2 = Plant(
        name="Sunflower",
        height=80,
        age=45,
    )
    p3 = Plant(
        name="Cactus",
        height=15,
        age=120,
    )
    plants = [p1, p2, p3]
    days: int = 1
    g: int = -1
    for days in range(1, 8):
        print(f"=== DAY {days} ===")
        for i in range(3):
            p = plants[i]
            print(f"{p.name}: {p.height}cm, {p.age} days old.")
            p.height += 1
            p.age += 1
        g += 1
    if days == 7:
        print(f"This week the plants growth {g}cm!")


def main():
    ft_plant_growth()


if __name__ == "__main__":
    main()
