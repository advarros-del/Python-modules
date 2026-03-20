class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def print_info(self) -> None:
        print(f"{self.name}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str,
            bloom: bool):
        super().__init__(name, height, age)
        self.color = color
        self.bloom = False

    def print_info(self) -> None:
        if self.bloom == True:
            status = "blooming"
        else:
            status = "not blooming"
        print(f"{self.name}: {self.height}cm, {self.color} flowers ({status})")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str,
            bloom: bool, prize_points: int):
        super().__init__(name, height, age, color, bloom)
        self.prize_points = 0

    def print_info(self) -> None:
        status = "blooming" if self.bloom == True else "not blooming"
        print(
            f"{self.name}: {self.height}cm, {self.color} flowers ({status},"
            f" Price points: {self.prize_points} ")


class Garden:
    def __init__(self, name: str):
        self.name = name
        self.plants: list = []
        self.t_growth: int = 0
        self.t_plants: int = 0
        self.score: int = 0

    def add_plants(self, plant) -> None:
        self.plants.append(plant)
        self.t_plants += 1
        print(f"Added {plant.name} to {self.name}'s garden")

    def growing_plants(self) -> None:
        print(f"{self.name} is helping plants grow...")
        for plant in self.plants:
            plant.height += 1
            print(f"{plant.name} grew 1cm")
            self.t_growth += 1
        print("")

    def garden_status(self) -> None:
        print(f"=== {self.name}'s Gaden Report ===")
        print("Plats in garden:")
        for plant in self.plants:
            print("-", end=" ")
            plant.print_info()
        print("")
        print(
        f"Plants added: {self.t_plants}, Total growth: {self.t_growth}cm"
        )


class GardenManager:
    def __init__(self):
        self.gardens: list = []
        self.gardens_added: int = 0

    def add_garden(self, gardens) -> None:
        self.gardens.append(gardens)

    def get_garden_by_owner(self, owner) -> list:
        for garden in self.gardens:
            if garden.name == owner:
                return garden
        return None

    def score_garden(self, value) -> None:
        self.score = value

    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        print("=== Garden Management System Demo ===")
        print("")
        manager: "GardenManager" = cls()
        g1 = Garden("Alice")
        g2 = Garden("Bob")
        p1 = Plant("Oak Tree", 101, 3070)
        p2 = FloweringPlant("Rose", 26, 45, "red", True)
        p3 = PrizeFlower("Sunflower", 51, 45, "yellow", True, 10)
        g1.add_plants(p1)
        g1.add_plants(p2)
        g1.add_plants(p3)
        print("")
        g1.growing_plants()
        g1.garden_status()
        GardenManager.score_garden(g1, 218)
        GardenManager.score_garden(g2, 92)
        manager.add_garden(g1)
        manager.add_garden(g2)
        return manager

    @staticmethod
    def is_valid_owner(owner) -> bool:
        if owner == "":
            return False
        else:
            return True

    def is_valid_height(plant) -> bool:
        i: bool = True
        for plant in plant:
            if plant.height < 0:
                i = False
        if i == False:
            print("Hegiht validation test: False")
        else:
            print("Height validation test: True")

    def is_valid_points(plant):
        if plant.ppoints < 0:
            return False
        else:
            return True

    class GardenStats:
        @staticmethod
        def count_plant_types(garden) -> None:
            Regular: int = 0
            Flowering: int = 0
            Prize: int = 0
            for plant in garden.plants:
                class_name = plant.__class__.__name__
                if class_name == "PrizeFlower":
                    Prize += 1
                elif class_name == "FloweringPlant":
                    Flowering += 1
                else:
                    Regular += 1
            print(
                f"Plant types: {Regular} regular, {Flowering} flowering,"
                f"{Prize} prize flowers"
                )

        def Print_an_4_onwers(self, owner):
            garden = self.get_garden_by_owner(owner)
            if garden is None:
                print("Garden not found", owner)
                return


def main():
    manager: list = GardenManager.create_garden_network()
    garden = manager.get_garden_by_owner("Alice")
    GardenManager.GardenStats.count_plant_types(garden)
    print("")
    GardenManager.is_valid_height(garden.plants)
    print(
        f"Garden scores - {manager.gardens[0].name}: "
        f"{manager.gardens[0].score},"
        f" {manager.gardens[1].name}: {manager.gardens[1].score}"
    )
    i: int = 0
    for garden in manager.gardens:
        i += 1
    print(f"Total gardens managed: {i}")


if __name__ == "__main__":
    main()
