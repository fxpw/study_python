# celebs = {
# 	"Альберт Эйнштейн": 1879,
# 	"Мария Кюри": 1867,
# 	"Стив Джобс": 1955,
# 	"Никола Тесла": 1856,
# 	"Леонардо да Винчи": 1452,
# }


# def func_for_loop():
# 	correct_answers = 0
# 	wrong_answers = 0

# 	for celeb, birth_year in celebs.items():
# 		user_answer = int(input(f"Введите год рождения {celeb}: "))
# 		if user_answer == birth_year:
# 			correct_answers += 1
# 		else:
# 			wrong_answers += 1

# 	total_questions = correct_answers + wrong_answers
# 	percentage_correct = (correct_answers * 100) / total_questions
# 	percentage_wrong = (wrong_answers * 100) / total_questions

# 	print(f"Количество правильных ответов: {correct_answers}")
# 	print(f"Количество ошибок: {wrong_answers}")
# 	print(f"Процент правильных ответов: {percentage_correct}%")
# 	print(f"Процент неправильных ответов: {percentage_wrong}%")

# 	answer = input("Хотите начать игру сначала? (да/нет): ")
# 	if answer == "да":
# 		func_for_loop()


# func_for_loop()


celebs = {
	"Альберт Эйнштейн": 1879,
	"Мария Кюри": 1867,
	"Стив Джобс": 1955,
	"Никола Тесла": 1856,
	"Леонардо да Винчи": 1452,
}
while True:
	correct_answers = 0
	wrong_answers = 0

	for celeb, birth_year in celebs.items():
		user_answer = int(input(f"Введите год рождения {celeb}: "))
		if user_answer == birth_year:
			correct_answers += 1
		else:
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
