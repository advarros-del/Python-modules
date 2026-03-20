class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


    class Flower(Plant):
        def __init__(self name: str, color: str, bloom: bool):
            super().__init__(name)
            self.color = color
            self.bloom = False

        def bloom(self, bloomed) -> None:
            if self:bloomed == False:
                print(f"{name} is not bloomed yet!")
            else
                print(f"{name} is blooming beautifully!")


    class Tree(Plant):
        def __init__(self name:str, trunk_diameter: int):
            super().__init__(name)
            self.trunk_diameter = t_diam

        def produce_shade (self, value: int):
            print(f"{self.name} provides {value} square meters of shade")

    class Vegetable(Plant):
        def __init__(self name: str, haverst_season: str, nutritional_vaule: str):
            super().__init__(name)
            self.harves_season = harvest_season
            self.nutritional_value = n_value

    


def main():
    f1(Flower) = ("Rose", 25, 30, "red")
    f2(Flower) = ("Daffodil" 5, 60, "yellow"
    t1(Tree) = "Oak", 500, 1825, 50)
    t2(Tree) = "Birch", 308, 3567, 20)
    v1(Vegetable) = ("Tomato", 80, 90, "summer", "vitamin C")
    v2(Vegetable) = ("Carrot", 20, 65, "autumn", "vitamin A")
    print(f"{f1.name} (Flower): {f1.height}cm, {f1.age} days, {f1.color} color")
    bloom(f1, True)
    print(f"{f2.name} (Flower): {f2.height}cm, {f2.age} days, {f2.color} color")
    bloom(f2, False)
    print(f"{t1.name} (Tree): {t1.height}cm, {t1.age} days, {t1.t_diam}cm diameter")
    produce_shade(t1, 78)
    print(f"{t2.name} (Tree): {t2.height}cm, {t2.age} days, {t2.t_diam}cm diameter")
    produce_shade(t2, 24)
    print(f"{v1.name} (Vegetable): {v1.height}cm, {v1.age} days, {v1.harvest_season} harvest")
    print(f"{v1.name} is rich in {v1.n_value}")
    print(f"{v2.name} (Vegetable): {v2.height}cm, {v2.age} days, {v2.harvest_season} harvest")
    print(f"{v2.name} is rich in {v2.n_value}")


if __name__ == "__main__":
    main()
