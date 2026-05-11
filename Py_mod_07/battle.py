from ex0 import FlameFactory, WaterFactory


def main():
    print("Testing factory")
    flame_factory = FlameFactory()
    flame = flame_factory.create_base("Flameling")
    print(flame.describe())
    print(flame.attack())
    Pyrodon = flame_factory.create_evolved("Pyrodon")
    print(Pyrodon.describe())
    print(Pyrodon.attack())
    print("")
    water_factory = WaterFactory()
    water = water_factory.create_base("Aquabob")
    print(water.describe())
    print(water.attack())
    Torragon = water_factory.create_evolved("Torragon")
    print(Torragon.describe())
    print(Torragon.attack())
    print("")
    print("Testing battle")
    print(flame.describe())
    print(" vs.")
    print(water.describe())
    print(" fight!")
    print(flame.attack())
    print(water.attack())


if __name__ == "__main__":
    main()
