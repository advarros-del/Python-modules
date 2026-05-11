from ex1.healing_things import HealingFactory, TransformFactory
import typing


def main() -> None:
    print("Testing Creature with healing capability")
    healing_factory = HealingFactory()
    print(" base:")
    sproutling = healing_factory.create_base("Sproutling")
    print(sproutling.describe())
    print(sproutling.attack())
    print(typing.cast(typing.Any, sproutling).heal("itself"))
    print(" evolved:")
    bloomelle = healing_factory.create_evolved("Bloomelle")
    print(bloomelle.describe())
    print(bloomelle.attack())
    print(typing.cast(typing.Any, bloomelle).heal("itself and others"))
    print("")
    print("Testing Creature with transform capability")
    transform_factory = TransformFactory()
    print(" base:")
    shiftling = transform_factory.create_base("Shiftling")
    print(shiftling.describe())
    print(shiftling.attack())
    print(typing.cast(typing.Any, shiftling).transform())
    print(shiftling.attack())
    print(typing.cast(typing.Any, shiftling).revert())
    print(" evolved:")
    morphgon = transform_factory.create_evolved("Morphgon")
    print(morphgon.describe())
    print(morphgon.attack())
    print(typing.cast(typing.Any, morphgon).transform())
    print(morphgon.attack())
    print(typing.cast(typing.Any, morphgon).revert())


if __name__ == "__main__":
    main()
