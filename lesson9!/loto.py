
import random


class LotoGame():
	class Player():
		def __init__(self,is_pc:str,player_name:str):
			self.is_bot = is_pc
			self.GenerateCart()
			self.checkedNums = []
			self.name = player_name

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
