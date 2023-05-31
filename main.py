from aiogram import Router  # noqa
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.default import main_menu

main_router = Router()


@main_router.message(CommandStart())
async def start(message: Message):
    await message.answer('Bot started 🟢', reply_markup=main_menu.as_markup(resize_keyboard=True))
