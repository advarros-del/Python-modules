def ft_count_harvest_iterative () -> None:
	day = int(input("Days until harvest: "))
	counter = 1
	while counter <= day:
		print(f"Day {counter}")
		counter += 1 
	print("Harvest time!")
