
import random


class LotoGame():
	class Player():
		def __init__(self,is_pc:str,player_name:str):
			self.is_bot = is_pc
			self.GenerateCart()
			self.checkedNums = []
			self.name = player_name
		def __str__(self) -> str:
			print(self.name)
			return self.name

		def __eq__(self, equalobj) -> bool:
			return self.name == equalobj.name
		
		def GenerateCart(self):
			numbers = random.sample(range(1, 91), 27)
			self.numbers = numbers
			card = [sorted(numbers[i : i + 9]) for i in range(0, 27, 9)]
			for row in card:
				blank_indices = random.sample(range(9), 4)  # индексы для замены на 0
				for index in blank_indices:
					row[index] = 0
			self.card = card

		def Check(self, solution:str, num:int):
			if solution == "1":
				if self.IfNumberInCard(num):
					self.checkedNums.append(num)
					return "True"
				return "False"
			elif solution == "2":
				if self.IfNumberInCard(num):
					return "False"
				return "True"
			return "False"
		def AutoCheck(self, num:int):
			if self.IfNumberInCard(num):
				self.checkedNums.append(num)
				return True
			return False



		def IfNumberInCard(self,num):
			for i in range(3):
				if int(num) in self.card[i]:
					return True
			return False
		def ShowCard(self):
			print(f"-------------{self.name}--------------")
			print("-".join(str(number) if number > 0 and number not in self.checkedNums else "[x]" for number in self.card[0]))
			print("-".join(str(number) if number > 0 and number not in self.checkedNums else "[x]" for number in self.card[1]))
			print("-".join(str(number) if number > 0 and number not in self.checkedNums else "[x]" for number in self.card[2]))
			print(f"-------------{self.name}--------------")
			pass
	
	def __init__(self,player1_is_pc,player2_is_pc):
		self.p1=LotoGame.Player(player1_is_pc,"p1")
		self.p2=LotoGame.Player(player2_is_pc,"p2")
		self.generated_nums = []
	def __str__(self) -> str:
			print("nums\n")
			print(self.generated_nums)
			print("\n")
			print("p1\n")
			print(self.p1)
			print("\n")
			print("p2\n")
			print(self.p2)
			print("\n")

	def StartGame(self):
		random_numbers = random.sample(range(1, 91), 90)
		for number in random_numbers:
			print(f"Number {number}\n")
			self.p1.ShowCard()
			self.p2.ShowCard()
			# print("card1\n")
			# print("card2\n")
			if self.p1.is_bot == "1":
				p1_check = input("p1 enter action\n1 if зачеркнуть\n2 if продолжить\n0 exit game\n")
				while not (p1_check =="1" or p1_check == "2"):
					p1_check = input("p1 enter action\n1 if зачеркнуть\n2 if продолжить\n0 exit game\n")
				if p1_check == "0":
					return
				if self.p1.Check(p1_check,number) == "False":
					print("p2 won")
					return
				if len(self.p1.checkedNums)>=27:
					print("p1 won")
					return
			else:
				self.p1.AutoCheck(number)
				if len(self.p1.checkedNums)>=27:
					print("p1 won")
					return
			if self.p2.is_bot == "1":
				p2_check = input("p2 enter action\n1 if зачеркнуть\n2 if продолжить\n0 exit game\n")
				while not (p2_check == "1" or p2_check == "2"):
					p2_check = input("p2 enter action\n1 if зачеркнуть\n2 if продолжить\n0 exit game\n")
				if p2_check == "0":
					return
				if self.p2.Check(p2_check,number) == "False":
					print("p1 won")
					return
				if len(self.p2.checkedNums)>=27:
					print("p2 won")
					return
			else:
				self.p2.AutoCheck(number)
				if len(self.p2.checkedNums)>=27:
					print("p2 won")
					return


# import pytest
# from pytest import capfd


def test_card_generation():
    player = LotoGame.Player("0", "Test")
    assert len(player.card) == 3
    for row in player.card:
        assert len(row) == 9
        # Проверяем, что в каждой строке 5 чисел и 4 нуля
        assert sum(1 for number in row if number > 0) == 5
        assert sum(1 for number in row if number == 0) == 4



def test_check_function():
    player = LotoGame.Player("0", "Test")
    # Добавляем какое-то число в карточку
    player.card[0][0] = 42

    # Тестируем сценарий, когда число есть в карточке и игрок решает зачеркнуть его
    assert player.Check("1", 42) == "True"

    # Тестируем сценарий, когда число есть в карточке, но игрок решает не зачеркивать его
    assert player.Check("2", 42) == "False"

    # Тестируем сценарий, когда числа нет в карточке, и игрок решает зачеркнуть его
    assert player.Check("1", 99) == "False"

def test_auto_check_function():
    player = LotoGame.Player("0", "Test")
    player.card = [[0, 0, 0, 0, 5, 0, 0, 0, 9], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    assert player.AutoCheck(5) is True
    assert player.AutoCheck(1) is False

def test_show_card(capfd):
    player = LotoGame.Player("0", "Test")
    player.card = [[1, 2, 3, 0, 5, 6, 0, 8, 9], [10, 11, 0, 13, 0, 15, 16, 0, 18], [19, 0, 21, 22, 0, 24, 25, 26, 0]]
    player.ShowCard()
    out, err = capfd.readouterr()
    assert "1-2-3-[x]-5-6-[x]-8-9" in out
    assert "10-11-[x]-13-[x]-15-16-[x]-18" in out
    assert "19-[x]-21-22-[x]-24-25-26-[x]" in out
    
def test_start_game_initialization():
    game = LotoGame("0", "0")
    assert game.p1 is not None
    assert game.p2 is not None


def test_equal():
	player1 = LotoGame.Player("0", "Test1")
	player11 = LotoGame.Player("0", "Test1")
	player2 = LotoGame.Player("0", "Test2")
	assert player1 != player2
	assert player11 == player1

def test_name(capfd):
	# game = LotoGame("0", "0")
	player = LotoGame.Player("0", "Test")
	print(player)
	out, err = capfd.readouterr()
	assert "Test" in out
