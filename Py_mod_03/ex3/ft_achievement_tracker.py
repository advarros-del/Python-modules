import random


class Player:
    def __init__(self, name: str, lst_ach: set):
        self.name = name
        self.lst_ach = lst_ach

    def get_player_achievements(self, achievements: list) -> set:

        n: int = random.randint(1, len(achievements))
        self.lst_ach = set(random.sample(achievements, n))
        return self.lst_ach


def main() -> None:
    achievements: list = [
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Master Ecplorer",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer"
        ]
    print("=== Achievement Tracker System ===\n")
    Alice = Player("Alice", set())
    Alice.get_player_achievements(achievements)
    print(f"Player {Alice.name}: {Alice.lst_ach}")
    Bob = Player("Bob", set())
    Bob.get_player_achievements(achievements)
    print(f"Player {Bob.name}: {Bob.lst_ach}")
    Charlie = Player("Charlie", set())
    Charlie.get_player_achievements(achievements)
    print(f"Player {Charlie.name}: {Charlie.lst_ach}")
    Dylan = Player("Dylan", set())
    Dylan.get_player_achievements(achievements)
    print(f"Player {Dylan.name}: {Dylan.lst_ach}\n")
    temp: set = set.intersection(Alice.lst_ach, Bob.lst_ach,
                                 Charlie.lst_ach, Dylan.lst_ach)
    all_ach: set = set.union(Alice.lst_ach, Bob.lst_ach,
                             Charlie.lst_ach, Dylan.lst_ach)
    print(f"All distinct achievements: {all_ach}\n")
    print(f"Common achievements: {temp}\n")
    aux: set = set.difference(Alice.lst_ach, Bob.lst_ach,
                              Charlie.lst_ach, Dylan.lst_ach)
    print(f"Only Alice has: {aux}")
    aux = set.difference(Bob.lst_ach, Alice.lst_ach,
                         Charlie.lst_ach, Dylan.lst_ach)
    print(f"Only Bob has: {aux}")
    aux = set.difference(Charlie.lst_ach, Alice.lst_ach,
                         Bob.lst_ach, Dylan.lst_ach)
    print(f"Only Charlie has: {aux}")
    aux = set.difference(Dylan.lst_ach, Alice.lst_ach,
                         Bob.lst_ach, Charlie.lst_ach)
    print(f"Only Dylan has: {aux}\n")
    aux = set(achievements).difference(Alice.lst_ach)
    print(f"Alice is missing: {aux}")
    aux = set(achievements).difference(Bob.lst_ach)
    print(f"Bob is missing: {aux}")
    aux = set(achievements).difference(Charlie.lst_ach)
    print(f"Charlie is missing: {aux}")
    aux = set(achievements).difference(Dylan.lst_ach)
    print(f"Dylan is missing: {aux}")


if __name__ == "__main__":
    main()
