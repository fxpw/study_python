import random


def test_GenerateCart():
	numbers = random.sample(range(1, 91), 27)
	card = [sorted(numbers[i : i + 9]) for i in range(0, 27, 9)]
	for row in card:
		blank_indices = random.sample(range(9), 4)  # индексы для замены на 0
		for index in blank_indices:
			row[index] = 0
	return card
