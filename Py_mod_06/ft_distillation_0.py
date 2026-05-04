from alchemy import potions

def printer() -> None:
    print(f"Testing strength_potion: {potions.strength_potion()}")
    print(f"Testing healing_potion: {potions.healing_potion()}")


def main() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potion.py")
    printer()

if __name__ == "__main__":
    main()
