import os
import sys
import shutil
from lesson4.use_functions import bank
from lesson4.borndayforewer import born_day_quiz


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


def list_directory():
	print(os.listdir("."))


def list_folders():
	for item in os.listdir("."):
		if os.path.isdir(item):
			print(item)


def list_files():
	for item in os.listdir("."):
		if os.path.isfile(item):
			print(item)


def view_os_info():
	print('My OS is', sys.platform, '(', os.name, ')')
	pass


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
		print("12 - Выход")

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
			exit_program()
		else:
			print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
	main_menu()