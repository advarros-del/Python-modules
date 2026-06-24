from typing import Callable, Any


def mage_counter() -> Callable:
    counter = 0

    def counter_func() -> int:
        nonlocal counter
        counter += 1
        return counter
    return counter_func


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def acumulator(amount_power) -> int:
        nonlocal power
        power += amount_power
        return power
    return acumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def make_the_enchant(item_name) -> str:
        return f"{enchantment_type} {item_name}"
    return make_the_enchant


def memory_vault() -> dict[str, Callable]:
    the_dict: dict[str, Any] = {}

    def store(key: str, value: int) -> str:
        the_dict[key] = value
        return f"{value}"

    def recall(key: str) -> str:
        return f"{the_dict.get(key, 'Memory not found')}"

    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    counter_b = mage_counter()
    print(f"counter_b call 1: {counter_b()}")
    print("\nTesting spell accumulator...")
    the_amount = spell_accumulator(100)
    print(f"Base 100, add 20: {the_amount(20)}")
    print(f"Base 100, add 30: {the_amount(30)}\n")
    ffactory = enchantment_factory("Frozen")
    flfactory = enchantment_factory("Flaming")
    sword: dict = flfactory("Sword")
    shield: dict = ffactory("Shield")
    print("Testing enchantment factory...")
    print(sword)
    print(shield)
    print("\nTesting memory vault...")
    call = memory_vault()
    print(f"Store 'secret' = {call['store']('secret', 42)}")
    print(f"Recall 'secret' = {call['recall']('secret')}")
    print(f"Recall 'secret' = {call['recall']('unknown')}")


if __name__ == "__main__":
    main()
