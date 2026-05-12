import alchemy.transmutation.recipes


def printer() -> None:
    print(f"Testing lead to gold: "
          f"{alchemy.transmutation.recipes.lead_to_gold()}")


def main() -> None:
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    printer()


if __name__ == "__main__":
    main()
