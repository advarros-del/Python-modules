def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now -THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    from alchemy.grimoire import dark_spellbook
    result: str = dark_spellbook.dark_spell_record(
        "BANANA", "shadow, bone, ink")
    print(f"Testing record dark spell : {result}")


if __name__ == "__main__":
    main()
