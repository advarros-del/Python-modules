from alchemy import grimoire


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    result: str = grimoire.light_spellbook.light_spell_record("BANANA", "fire, thorn, clay")
    print(f"Testing record light spell : {result}")
