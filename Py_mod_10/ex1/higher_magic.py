from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[Callable, Callable]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int) -> Callable:
        return (base_spell(target, power * multiplier))
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cond_cast(target: str, power: int) -> Callable | str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return cond_cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def caster(target: int, power: int) -> list[Callable]:
        return [spell(target, power) for spell in spells]
    return caster


def fireball(target: str, power: int) -> str:
    return f"{target} recieve {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def cond_cast(target: str, power: int) -> bool:
    return power > 7


def main() -> None:
    combined_spells = spell_combiner(fireball, heal)
    the_target = combined_spells("dragon", 5)
    print(f"Combined spell result: {the_target[0]}, {the_target[1]}\n")
    amplified = power_amplifier(fireball, 4)
    the_target = amplified("Dragon", 4)
    print(f"Spell amplified: {the_target}\n")
    cond = conditional_caster(cond_cast, fireball)
    print(f"Condition Success: {cond('Dragon', 15)}")
    print(f"Condition failed: {cond('Dragon', 2)}\n")
    spellbook: list = [fireball, heal]
    spell_sec = spell_sequence(spellbook)
    the_str = (", ".join(spell_sec('Dragon', 13)))
    print(f"The secuence: {the_str}")


if __name__ == "__main__":
    main()
