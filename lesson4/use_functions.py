import os

"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
balance: float = 0
list_of_purchase = []

# while True:
# 	print("1. пополнение счета")
# 	print("2. покупка")
# 	print("3. история покупок")
# 	print("4. выход")

# 	choice = input("Выберите пункт меню ")
# 	if choice == "1":
# 		new_balance = float(input("Введите сумму для пополнения "))
# 		balance += new_balance
# 		print(f"Баланс пополнен на {new_balance} текущий баланс {balance}")
# 		pass
# 	elif choice == "2":
# 		name_of_product = input("Что хотите купить? ")
# 		sum = float(input("На какую сумму? "))
# 		if balance < sum:
# 			print("Не хватает денег на покупку")
# 			continue
# 		print(f"Куплено:{name_of_product}\nСумма:{sum}")
# 		list_of_purchase.append({"name": name_of_product, "sum": sum})
# 		pass
# 	elif choice == "3":
# 		for log in list_of_purchase:
# 			print(f"Товар:{log['name']}; Сумма {log['sum']}\n")
# 		pass
# 	elif choice == "4":
# 		break
# 	else:
# 		print("Неверный пункт меню")


def bank():
	print("1. пополнение счета")
	print("2. покупка")
	print("3. история покупок")
	print("4. выход")
	# global balance
	choice = input("Выберите пункт меню ")
	if choice == "1":
		balance = 0.0
		if not os.path.exists("balance.txt"):
			with open("balance.txt", "w") as file:
				file.write("0")
		with open("balance.txt", "r") as file:
			balance = float(file.read())
		new_balance = float(input("Введите сумму для пополнения "))
		balance += new_balance
		with open("balance.txt", "w") as file:
			file.write(str(balance))
		print(f"Баланс пополнен на {new_balance} текущий баланс {balance}")
		pass
	elif choice == "2":
		balance = 0
		with open("balance.txt", "r") as file:
			balance = float(file.read())
		name_of_product = input("Что хотите купить? ")
		sum = 0
		try:
			sum = float(input("На какую сумму? "))
		except Exception as e:
			sum = -1
		if sum>0:
			if balance < sum:
				print("Не хватает денег на покупку")
			else:
				print(f"Куплено:{name_of_product}\nСумма:{sum}")
				if not os.path.exists("purchases.txt"):
					with open("purchases.txt", "w") as file:
						file.write(f"{name_of_product}:{sum}\n")
				else:
					with open("purchases.txt", "w") as file:
						file.write(f"{name_of_product}:{sum}\n")
				balance = balance - sum
				with open("balance.txt", "w") as file:
					file.write(str(balance))
	elif choice == "3":
		if not os.path.exists("purchases.txt"):
			print("покупок еще не было")
		else:
			with open("purchases.txt", "r") as file:
				print(file.read())
		# for log in list_of_purchase:
		# 	print(f"Товар:{log['name']}; Сумма {log['sum']}\n")
		# pass
	elif choice == "4":
		return
	else:
		print("Неверный пункт меню")
	bank()
