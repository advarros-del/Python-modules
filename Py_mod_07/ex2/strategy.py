import abc
from ex0.creature import Creature
from ex1.healing_things import HealCapability, TransformCapability


class BattleStrategy(abc.ABC):
    @abc.abstractmethod
    def act(self, creature: "Creature") -> None:
        pass

    @abc.abstractmethod
    def is_valid(self, creature: "Creature") -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: "Creature") -> None:
        print(creature.attack())

    def is_valid(self, creature: "Creature") -> bool:
        return hasattr(creature, 'attack')


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: "Creature") -> None:
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())

    def is_valid(self, creature: "Creature") -> bool:
        return hasattr(creature, 'transform') and hasattr(creature, 'revert')


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: "Creature") -> None:
        if isinstance(creature, HealCapability):
            print(creature.attack())
            print(creature.heal("itself"))

    def is_valid(self, creature: "Creature") -> bool:
        return hasattr(creature, 'heal')
