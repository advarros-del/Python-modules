'# import typing'
import abc


class Creature(abc.ABC):
    @abc.abstractmethod
    def __init__(self, name: str, type: str) -> None:
        self.name: str = name
        self.type: str = type

    @abc.abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Fire")

    def attack(self: Creature) -> str:
        return f"{self.name} uses Ember!"


class Aquabob(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Water")

    def attack(self: Creature) -> str:
        return f"{self.name} uses Water Gun!"


class Pyrodon(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Fire/Flying")

    def attack(self: Creature) -> str:
        return f"{self.name} uses Flamethrower!"


class Torragon(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Water")

    def attack(self: Creature) -> str:
        return f"{self.name} uses Hydro Pump!"


class CreatureFactory(abc.ABC):
    @abc.abstractmethod
    def create_base(self, name: str) -> Creature:
        pass

    @abc.abstractmethod
    def create_evolved(self, name: str) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self, name: str) -> Creature:
        return Flameling(name)

    def create_evolved(self, name: str) -> Creature:
        return Pyrodon(name)


class WaterFactory(CreatureFactory):
    def create_base(self, name: str) -> Creature:
        return Aquabob(name)

    def create_evolved(self, name: str) -> Creature:
        return Torragon(name)
