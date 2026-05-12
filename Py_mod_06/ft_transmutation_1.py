import alchemy.transmutation


def printer() -> None:
    print(f"Testing lead to gold: {alchemy.transmutation.lead_to_gold()}")


def main() -> None:
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    printer()


if __name__ == "__main__":
    main()
