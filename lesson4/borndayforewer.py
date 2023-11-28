def mfunc():
	year = int(input("input enter Pushkin's year of birth "))
	if year == 1799:
		print("verno")
	elif year < 1799:
		print("bolshe")
	elif year > 1799:
		print("menshe")
	check = input("Выйти? ")
	if check == "да":
		return
	mfunc()
mfunc()