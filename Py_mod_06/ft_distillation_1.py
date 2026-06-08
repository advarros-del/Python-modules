import alchemy


def printer() -> None:
    print(f"Testing strength_potion: {alchemy.strength_potion()}")
    print(f"Testing heal alias: {alchemy.heal()}")


def main() -> None:
    print("=== Destillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    printer()


if __name__ == "__main__":
    main()
