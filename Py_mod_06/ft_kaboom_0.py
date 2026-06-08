from alchemy.grimoire import light_spellbook


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    result: str = light_spellbook.light_spell_record(
        "BANANA", "fire, thorn, clay")
    print(f"Testing record light spell : {result}")


if __name__ == "__main__":
    main()
