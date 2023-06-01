from aiogram import Router
from aiogram.filters import Text, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, ReplyKeyboardRemove
from aiogram.types import Message

from keyboards.default import back_to_main, main_menu

buttons_router = Router()


@buttons_router.message(Text('🆘 Aloqa'))
async def start(message: Message):
    await message.answer(
        "@taksi_clone_bot botining <a href=\"https://t.me/all_nc\">TAXIDASUPPORT</a> bilan bog'lanish",
        # noqa
        reply_markup=back_to_main.as_markup(resize_keyboard=True)
    )


@buttons_router.message(Text('🔝 Asosiy Menyu'))
async def start(message: Message):
    photo = FSInputFile('/home/user/projects/aiogram_projects/taksi_bot/images/taksi.jpeg')
    await message.answer_photo(
        caption=f"""😊 Assalomu alaykum {message.from_user.full_name} ,
❗️ Taxi botimizga xush kelibsiz, o'zingizga maqul bo'limni tanlang""",
        photo=photo,
        reply_markup=main_menu.as_markup(resize_keyboard=True)
    )


@buttons_router.message(Command(commands=["cancel"]))
@buttons_router.message(Text(text="cancel", ignore_case=True))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Bekor qilindi!",
        reply_markup=ReplyKeyboardRemove()
    )
