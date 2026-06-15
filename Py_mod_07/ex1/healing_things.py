import abc
from ex0.creature import Creature, CreatureFactory


class HealCapability(abc.ABC):
    @abc.abstractmethod
    def heal(self, target: str) -> str:
        pass


class TransformCapability(abc.ABC):
    @abc.abstractmethod
    def transform(self) -> str:
        pass

    @abc.abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: str) -> str:
        return f"{self.name} heals {target} for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: str) -> str:
        target = "itself and others"
        return f"{self.name} heals {target} for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Normal")
        self.transformed: bool = False

    def attack(self) -> str:
        if self.transformed is False:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} performs a boosted strike!"

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} returns to normal."


class Morphgon(Creature, TransformCapability):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Normal/Dragon")
        self.transformed: bool = False

    def attack(self) -> str:
        if self.transformed is False:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} stabilizes its form."


class HealingFactory(CreatureFactory):
    def create_base(self, name: str) -> Creature:
        return Sproutling(name)

    def create_evolved(self, name: str) -> Creature:
        return Bloomelle(name)


class TransformFactory(CreatureFactory):
    def create_base(self, name: str) -> Creature:
        return Shiftling(name)

    def create_evolved(self, name: str) -> Creature:
        return Morphgon(name)
