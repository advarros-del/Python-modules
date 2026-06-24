from typing import Callable, Any
import time
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Castin {func.__name__}...")
        time_start = time.perf_counter()
        result: Any = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - time_start
        print(f"Spell completed in {execution_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if 'power' in kwargs:
                power = kwargs.get('power')
            else:
                power = args[2]
            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            atttemp: int = 0
            while atttemp < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    atttemp += 1
                    if atttemp < max_attempts:
                        print(f"Spell failed, retrying ..."
                              f"attemp{atttemp}/{max_attempts}")
            return (
                f"Spell casting failed after {max_attempts} attempts"
            )
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3:
            if all(c.isalpha() or c.isspace() for c in name):
                return True
        return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    time.sleep(0.101)
    return "Fireball cast!"


@retry_spell(max_attempts=3)
def invalid_spell() -> None:
    raise Exception("Invalid spell")


@retry_spell(max_attempts=3)
def wagh() -> str:
    return "Waaaaaaagh"


def main() -> None:
    print("Testin Spell timer:")
    print(f"Resutl {fireball()}")
    print("\nTesting retryin spell")
    print(invalid_spell())
    print(wagh())
    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Dumbeldor"))
    print(MageGuild.validate_mage_name("ah"))
    print(guild.cast_spell(" Lightning", 15))
    print(guild.cast_spell("Potatos", 3))


if __name__ == "__main__":
    main()
