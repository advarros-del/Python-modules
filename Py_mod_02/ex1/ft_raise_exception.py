def test_temperature() -> None:
    print("=== Garden Temperatue ===")
    try:
        input_temperature("25")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    try:
        input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    try:
        input_temperature("100")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    try:
        input_temperature("-50")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("")
    print("All test completed - program didn't crash!")
    


def input_temperature(temp_str) -> None:
    print("")
    print(f"Input data: '{temp_str}'")
    try:
       n: int = int(temp_str)
    except ValueError as e:
        raise ValueError(f"invalid literal for int() with base 10: '{temp_str}'") from e
    if 0 < n < 40:
        print(f"Temperature is now {temp_str}ºC")
    
    elif n < 0:
        raise ValueError(f"{temp_str} is too cold for plants (min 0ºC)")
    else:
        raise ValueError(f"{temp_str} is too hot for plants (max 40ºC)")


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()