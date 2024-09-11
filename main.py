# from lesson5.file_manager import main_menu
# from lesson11.loto import LotoGame
import asyncio
from lesson16.flask_web_app import StartWebApp

if __name__ == "__main__":
	asyncio.run(StartWebApp())
	print()
# 	player1_is_pc = input("player1_is_pc:\n")
# 	player2_is_pc = input("player2_is_pc:\n")
# 	game = LotoGame(player1_is_pc,player2_is_pc)
# 	game.StartGame()