import alchemy

def printer() -> None:
    print(f"Testing lead to gold: {alchemy.transmutation.lead_to_gold()}")


def main() -> None:
    print("=== Transmutation 2 ===")
    print("Import alchemy module only")
    printer()

if __name__ == "__main__":
    main()
