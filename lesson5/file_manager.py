import os
import sys
import shutil
from lesson4.bank import bank
from lesson4.borndayforewer import born_day_quiz


def decorator_func(func):
	def new_func():
		print("*" * 10)
		func()
		print("*" * 10)

	return new_func


def trace(func):
	def wrapper(*args, **kwargs):
		print(f"TRACE: calling {func.__name__}() " f"with {args}, {kwargs}")

		original_result = func(*args, **kwargs)

		print(f"TRACE: {func.__name__}() " f"returned {original_result!r}")

		return original_result

	return wrapper


def create_folder():
	folder_name = input("Введите название папки: ")
	os.makedirs(folder_name, exist_ok=True)


def delete_file_or_folder():
	name = input("Введите название файла или папки: ")
	if os.path.isdir(name):
		shutil.rmtree(name)
	elif os.path.isfile(name):
		os.remove(name)


def copy_file_or_folder():
	name = input("Введите название файла или папки для копирования: ")
	new_name = input("Введите новое название: ")
	if os.path.isdir(name):
		shutil.copytree(name, new_name)
	elif os.path.isfile(name):
		shutil.copy(name, new_name)


@decorator_func
@trace
def list_directory():
	print(os.listdir("."))


def list_folders():
	# list_of_folders = []
	# for item in os.listdir("."):
	# 	if os.path.isdir(item):
	# 		list_of_folders.append(item)
	# 		print(item)
	list_of_folders = [item for item in os.listdir(".") if os.path.isdir(item)]
	return list_of_folders


def list_files():
	# list_of_files =[]
	# for item in os.listdir("."):
	# 	if os.path.isfile(item):
	# 		list_of_files.append(item)
	# 		print(item)
	list_of_files = [item for item in os.listdir(".") if os.path.isfile(item)]
	return list_of_files


@decorator_func
def view_os_info():
	print("My OS is", sys.platform, "(", os.name, ")")
	pass


@decorator_func
def about_creator():
	print("Информация о создателе программы.")
	print("Name : fxpw")


def play_quiz():
	born_day_quiz()
	pass


def banking_account():
	bank()


def change_directory():
	path = input("Введите путь: ")
	os.chdir(path)


def save_directiry():
	list_files_list = list_files()
	list_folders_list = list_folders()
	try:
		if not os.path.exists("listdir.txt"):
			with open("listdir.txt", "w") as file:
				file.write(f"files {", ".join(list_files_list)}\n")
				file.write(f"dirs {", ".join(list_folders_list)}\n")
				return
		with open("listdir.txt", "w") as file:
			file.write(f"files {", ".join(list_files_list)}\n")
			file.write(f"dirs {", ".join(list_folders_list)}\n")
	except Exception as e:
		print(str(e))
		pass


def exit_program():
	sys.exit()


def main_menu():
	while True:
		print("\nМеню:")
		print("1 - Создать папку")
		print("2 - Удалить (файл/папку)")
		print("3 - Копировать (файл/папку)")
		print("4 - Просмотр содержимого рабочей директории")
		print("5 - Посмотреть только папки")
		print("6 - Посмотреть только файлы")
		print("7 - Просмотр информации об ОС")
		print("8 - Создатель программы")
		print("9 - Играть в викторину")
		print("10 - Мой банковский счет")
		print("11 - Смена рабочей директории")
		print("12 - Сохранение содержимого в файл")
		print("13 - Выход")

		choice = input("Выберите пункт: ")

		if choice == "1":
			create_folder()
		elif choice == "2":
			delete_file_or_folder()
		elif choice == "3":
			copy_file_or_folder()
		elif choice == "4":
			list_directory()
		elif choice == "5":
			list_folders()
		elif choice == "6":
			list_files()
		elif choice == "7":
			view_os_info()
		elif choice == "8":
			about_creator()
		elif choice == "9":
			play_quiz()
		elif choice == "10":
			banking_account()
		elif choice == "11":
			change_directory()
		elif choice == "12":
			save_directiry()
		elif choice == "13":
			exit_program()
		else:
			print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
	main_menu()
