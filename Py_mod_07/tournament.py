from ex0.creature import FlameFactory, WaterFactory
from ex1.healing_things import HealingFactory, TransformFactory
from ex2.strategy import NormalStrategy, AggressiveStrategy, DefensiveStrategy
import typing




def main() -> None:
    class BattleError(Exception):
        pass
    
    flame_factory = FlameFactory()
    water_factory = WaterFactory()
    healing_factory = HealingFactory()
    transform_factory = TransformFactory()
    flame = flame_factory.create_base("Flameling")
    water = water_factory.create_base("Aquabob")
    sproutling = healing_factory.create_base("Sproutling")
    shiftling = transform_factory.create_base("Shiftling")
    pack1: tuple = (flame, NormalStrategy())
    pack2: tuple = (sproutling, DefensiveStrategy())
    pack3: tuple = (flame, AggressiveStrategy())
    pack4: tuple = (water, NormalStrategy())
    pack5: tuple = (shiftling, AggressiveStrategy())
    print("Tournament 0 (basic)")
    tour1: list = [pack1, pack2]
    formatted_tour = []
    for pack in tour1:
        creture_name: str = pack[0].__class__.__name__
        strategy_name: str = pack[1].__class__.__name__.replace('Strategy', '')
        formatted_tour.append(f"({creture_name}+{strategy_name})")
    print(f"[ {', '.join(formatted_tour)} ]")
    print("*** Tournament ***")
    print(f"{len(tour1)} opponents involved\n")
    print("*Battle*")
    try:
        print(f"{pack1[0].describe()}\n vs.\n{pack2[0].describe()}\n now fight!")
        if (pack1[1].is_valid(pack1[0])):
            pack1[1].act(pack1[0])
        else:
            raise BattleError(f"Invalid criature {pack1[0].name} for the {pack1[1].__class__.__name__}")
        if (pack2[1].is_valid(pack2[0])):
            pack2[1].act(pack2[0])
        else:
            raise BattleError(f"Invalid criature {pack2[0].name} for the {pack2[1].__class__.__name__}")
    except BattleError as e:
        print(f"Battle error: {e}")
    print("")
    print("Tournament 1 (error)")
    tour2: list = [pack3, pack2]
    formatted_tour = []
    for pack in tour2:
        creture_name: str = pack[0].__class__.__name__
        strategy_name: str = pack[1].__class__.__name__.replace('Strategy', '')
        formatted_tour.append(f"({creture_name}+{strategy_name})")
    print(f"[ {', '.join(formatted_tour)} ]")
    print("*** Tournament ***")
    print(f"{len(tour2)} opponents involved\n")
    print("")
    print("*Battle*")
    try:
        print(f"{pack3[0].describe()}\n vs.\n{pack2[0].describe()}\n now fight!")
        if (pack3[1].is_valid(pack3[0])) is True:
            pack3[1].act(pack3[0])
        else:
            raise BattleError(f"Invalid criature {pack3[0].name} for the {pack3[1].__class__.__name__}")
        if (pack2[1].is_valid(pack2[0])) is True:
            pack2[1].act(pack2[0])
        else:
            raise BattleError(f"Invalid criature {pack2[0].name} for the {pack2[1].__class__.__name__}")
    except BattleError as e:
        print(f"Battle error: {e}")
    print("")
    print("Tournament 2 (multiple)")
    tour3: list = [pack2, pack4, pack5]
    formatted_tour = []
    for pack in tour3:
        creture_name: str = pack[0].__class__.__name__
        strategy_name: str = pack[1].__class__.__name__.replace('Strategy', '')
        formatted_tour.append(f"({creture_name}+{strategy_name})")
    print(f"[ {', '.join(formatted_tour)} ]")
    print("*** Tournament ***")
    print(f"{len(tour3)} opponents involved\n")
    print("")
    try:
        for i in range(len(tour3) - 1):
            print("*Battle*")
            fighter1: tuple = tour3[i]
            fighter2: tuple = tour3[(i + 1)]
            print(f"{fighter1[0].describe()}\n vs.\n{fighter2[0].describe()}\n now fight!")
            if (fighter1[1].is_valid(fighter1[0])) is True:
                fighter1[1].act(fighter1[0])
            else:
                raise BattleError(f"Invalid criature {fighter1[0].name} for the {fighter1[1].__class__.__name__}")
            if (fighter2[1].is_valid(fighter2[0])) is True:
                fighter2[1].act(fighter2[0])
            else:
                raise BattleError(f"Invalid criature {fighter2[0].name} for the {fighter2[1].__class__.__name__}")
    except BattleError as e:
        print(f"Battle error: {e}")

if __name__ == "__main__":
    main()
