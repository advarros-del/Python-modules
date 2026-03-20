check_temperature(temp_str) -> int:
    i : int = 0
    while temp_str:
        if temp_str[i] >= '0' and temp_str[i] <= '9':
            i += 1
        else:
            print("Invalid input. Please enter a valid temperature.")
            return None
    temp: int = int(temp_str)
    if temp >= 0 and temp <= 40:
        return temp
    elif temp < 0:
        print("The temperature too low")
    else:
        print("The temperature is too high")


test_temperature_input(temp) -> None:
    print("=== Garden Temperature Checker ===")
    print("")
    print(f"Testing temperature: {temp}")
    aux: str = temp
    if ft_is_digit(temp) == "None":
        print(f"Error: {aux} is not a valid number")
        return None
    if temp >= 0 and temp <= 40:
        print(f"Temperature {temp}ºC is perfect for plants!")
    elif temp > 40:
        print(f"Error: {temp}ºC is too hot for plants (max 40ºC)")
    elif temp < 0:
        print(f"Error: {temp}ºC is too cold for plants (max 0ºC)")
    print("All test completed - programs didn't crash!")
    
ft_is_digit(thing:str)
    i : int = 0
    while temp_str:
        if temp_str[i] >= '0' and temp_str[i] <= '9':
            i += 1
        else:
            print("Invalid input. Please enter a valid temperature.")
            return thing = "None"
    return thing