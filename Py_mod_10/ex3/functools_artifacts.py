from typing import Callable, Any
from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    result: int = 0
    if len(spells) == 0 or operation not in ["add", "multiply", "max", "min"]:
        print("Error. Check the arguments")
        return result
    if operation == "add":
        result = reduce(operator.add, spells)
    elif operation == "multiply":
        result = reduce(operator.mul, spells)
    elif operation == "max":
        result = reduce(max, spells)
    elif operation == "min":
        result = reduce(min, spells)
    return result


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    func1 = partial(base_enchantment, 50, "Ice")
    func2 = partial(base_enchantment, 50, "Fire")
    func3 = partial(base_enchantment, 50, "Wind")
    return {
        "ice enchant": func1,
        "Fire enchant": func2,
        "Wind enchant": func3
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        return 0
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatcher(arg):
        return "Unknown spell type"

    @dispatcher.register(int)
    def damage(arg):
        return f"Damage spell: {arg} damage"

    @dispatcher.register(str)
    def enchant(arg):
        return f"Enchantement: {arg}"

    @dispatcher.register(list)
    def multicast(arg):
        return f"Multi-cast: {len(arg)} spells"
    return dispatcher


def main() -> None:
    print("Testing spell reducer...")
    spells_power: list[int] = [20, 40, 16, 24]
    print(f"Sum: {spell_reducer(spells_power, 'add')}")
    print(f"Product: {spell_reducer(spells_power, 'multiply')}")
    print(f"Max: {spell_reducer(spells_power, 'max')}")
    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print("\nTesting spell dispatcher...")
    dispat = spell_dispatcher()
    print(dispat(42))
    print(f"{dispat('fireball')}")
    spellbook: list = ["fireball", "heal", "meteor"]
    print(f"{dispat(spellbook)}")
    print(f"{dispat(None)}")


if __name__ == "__main__":
    main()
