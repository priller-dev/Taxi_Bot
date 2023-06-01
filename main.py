from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Text

from keyboards.default import main_menu
from states import AuthState

main_router = Router()


@main_router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.set_state(AuthState.full_name)
    await message.answer('Bot started 🟢', reply_markup=main_menu.as_markup(resize_keyboard=True))

