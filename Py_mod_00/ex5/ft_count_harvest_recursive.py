def ft_count_harvest_recursive () -> None:
	day = int(input("Days until harvest: "))
	def goes(counter):
		if counter > day:
			return
		print(f"Day {counter}")
		goes(counter + 1)
	goes (1)
	print("Harvest time!")
