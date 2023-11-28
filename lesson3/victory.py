import random
celebs_dict = {
	"Альберт Эйнштейн": "01.01.1879",
	"Мария Кюри": "01.01.1867",
	"Стив Джобс": "01.01.1955",
	"Никола Тесла": "01.01.1856",
	"Леонардо да Винчи": "01.01.1452",
}

celebs_dict2 = {
	"Альберт Эйнштейн": "первое января 1879",
	"Мария Кюри": "первое января 1867",
	"Стив Джобс": "первое января 1955",
	"Никола Тесла": "первое января 1856",
	"Леонардо да Винчи": "первое января 1452",
}

celebs_list = list(celebs_dict.keys())


while True:
	correct_answers = 0
	wrong_answers = 0
	random_list = random.sample(celebs_list,2)

	for celeb in random_list:
		user_answer = str(input(f"Введите год рождения {celeb} в формате dd.mm.yyyy: "))
		if user_answer == celebs_dict[celeb]:
			correct_answers += 1
		else:
			print(f"neverno nastoyaschee = {celebs_dict2[celeb]}")
			wrong_answers += 1

	total_questions = correct_answers + wrong_answers
	percentage_correct = (correct_answers * 100) / total_questions
	percentage_wrong = (wrong_answers * 100) / total_questions

	print(f"Количество правильных ответов: {correct_answers}")
	print(f"Количество ошибок: {wrong_answers}")
	print(f"Процент правильных ответов: {percentage_correct}%")
	print(f"Процент неправильных ответов: {percentage_wrong}%")

	answer = input("Хотите начать игру сначала? (да/нет): ")
	if answer == "нет":
		break