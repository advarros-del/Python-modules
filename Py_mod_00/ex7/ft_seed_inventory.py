def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	if unit == "packets":
		print(f"{seed_type} seeds: {quantity} {unit} avalable.")
	elif unit == "grams":
		print(f"{seed_type} seeds: {quantity} {unit} total.")
	elif unit == "area":
		print(f"{seed_type} seeds: {quantity} {unit} square meters.")
	else:
		print("Please, enter a direfferent unit. You can choose beetwen packets, grams or area.")
