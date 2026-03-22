def test_temperature() -> None:
    print("=== Garden Temperatue ===")
    input_temperature("25")
    input_temperature("abc")
    print("All test completed - program didn't crash!")
    


def input_temperature(temp_str) -> None:
    print("")
    print(f"Input data: '{temp_str}'")
    if ft_is_digit(temp_str) == 0:
        print(f"Temperature is now {temp_str}")
    else:
        print(
            f"Caught inpu_temperature error: invalid literal for int() with base 10: '{temp_str}'"
            )
    
def ft_is_digit(thing: str) -> int:
    i: int = 0
    for i in thing:
        if i in "0123456789":
            pass
        else:
            return 1
    return 0

test_temperature()