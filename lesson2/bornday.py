while(True):
	year = int(input("input enter Pushkin's year of birth\n"))
	if year == 1799:
		print("year verno")
		day = int(input("input enter Pushkin's day of birth\n"))
		if day == 6:
			print("day verno")
			break
		elif day < 1799:
			print("day bolshe")
		elif day > 1799:
			print("day menshe")
	elif year < 1799:
		print("year bolshe")
	elif year > 1799:
		print("year menshe")
