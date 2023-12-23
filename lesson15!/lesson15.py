import os

from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import CommandStart, StateFilter  # noqa
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (
	Message,
	InlineKeyboardMarkup,
	InlineKeyboardButton,
	CallbackQuery,
)
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv, find_dotenv

from constants import LAUNCH_MODE, TYPE_HINT_SESSION

load_dotenv(find_dotenv())


async def StartupBotCallback(bot: Bot):
	# from bot.ui import UI
	from aiogram.types import BotCommand

	await bot.set_my_commands(
		commands=[
			BotCommand(command="start", description="start"),
		]
	)


main_router = Router()


@main_router.message(CommandStart())
async def start_message_handler(
	message: Message,
	state: FSMContext,
	bot: Bot,
	async_session: TYPE_HINT_SESSION,
):
	await state.clear()

	sended_message = await message.answer(
		text="test",
	)

@main_router.message(CommandStart())
async def start_message_handler(
	message: Message,
	state: FSMContext,
	bot: Bot,
	async_session: TYPE_HINT_SESSION,
):
	await state.clear()

	sended_message = await message.answer(
		text="test",
	)


async def StartTelegramBot(async_session: TYPE_HINT_SESSION) -> None:
	from bot.handlers import main_router

	MainDispatcher = Dispatcher(storage=MemoryStorage())



	TelegramBot = Bot(
		token=str(
			os.environ.get(
				"TOKEN_BOT_MAIN"
			)
		),
		parse_mode="HTML",
	)
	await StartupBotCallback(TelegramBot)
	try:
		await MainDispatcher.start_polling(
			TelegramBot,
			async_session=async_session,
		)
	finally:
		await TelegramBot.session.close()
