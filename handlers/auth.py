import re

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from aiogram.types import Message

from keyboards.default import main_menu, send_phone, where_you_go
from states import AuthState, AuthDriverState
from utils.misc import car_names
from utils.tables import create_user, car_number_is_unique, get_user_by_id, get_car_id_by_name, \
    create_driver

auth_router = Router()


######################################################
#                  Validators
######################################################


@auth_router.message(AuthState.full_name, F.text.len() < 5)
async def validator_fullname(message: Message, state: FSMContext):
    await message.answer("❗️ Familiya va ismingizni 5 belgidan ko'p bo'lishi kerak!")


######################################################
#                  Handlers
######################################################

@auth_router.message(AuthState.full_name)
async def process_fullname(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await state.set_state(AuthState.phone)
    await message.answer(
        """
        ❗️ Iltimos telefon raqamingizni "Raqamni yuborish" knopkasini bosib yoki yozib yuboring.
        Namuna: +998 99 1234567
        """,
        reply_markup=send_phone.as_markup(resize_keyboard=True)
    )


@auth_router.message(AuthState.phone)
async def process_phone(message: Message, state: FSMContext):
    if message.content_type != 'contact':
        pattern = r'^(?:\+998|0)(?:9[01234579]|97|98|66|71|90|91|93|94|95|96|99)\d{7}$'
        if not re.match(pattern, message.text):
            return await message.answer("""
❗️ Iltimos raqam yuboryotganda faqat sonlardan foydalaning!
❗️ Botdan faqatgina O'zbekiston raqamlari orqali foydalana olasiz!
    """)

    data = await state.get_data()
    data['phone'] = message.contact.phone_number
    await create_user([message.from_user.id, *data.values()])
    photo = FSInputFile(ROOT_FOLDER + 'images/taksi.jpeg')
    await message.answer_photo(
        caption=f"""
😊 Assalomu aleykum ,
❗️ Taxi botimizga hush kelib siz, biz odamlarni uzog'ini yaqin
qilish maqsadida o'z ish faoliyatimizni boshladi. Bizni qo'llab
turasizlar degan umiddaman. Botdan foydalanish uchun
o'zingizga maqul bo`limni tanlang
""",
        photo=photo,
        reply_markup=main_menu.as_markup(resize_keyboard=True)
    )
    await state.clear()


@auth_router.message(AuthDriverState.car_name)
async def process_car_name(message: Message, state: FSMContext):
    if message.text in car_names:
        await state.update_data(car_name=message.text)
        await state.set_state(AuthDriverState.car_number)
        return await message.answer("❓ Moshinangiz raqamini kiriting:\nNamuna: 01 A 060 BA")

@auth_router.message(AuthDriverState.car_number)
async def process_car_name(message: Message, state: FSMContext):
    if await car_number_is_unique(message.text):
        data = await state.get_data()
        await state.clear()
        user_id = (await get_user_by_id(message.from_user.id))['id']
        car_id = await get_car_id_by_name(data['car_name'])
        await create_driver([user_id, car_id, message.text])
        return await message.answer("❓ Qayerga borasiz?", reply_markup=where_you_go.as_markup(resize_keyboard=True)) # noqa
    await message.answer("❗️ Ushbu avtomobil raqami avval ro'yxatdan o'tgan")
