from aiogram import Router # noqa
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.default import skip, button_1234, treaty, region, make_district, accept_or_not, \
    button_1234_driver
from states import DriverState
from utils.misc import region_list, get_districts_by_region

take_client_router = Router()

######################################################
#                  Handlers
######################################################

@take_client_router.message(DriverState.from_region)
async def process_from_region(message: Message, state: FSMContext):
    if message.text not in region_list:
        return await message.answer("❗️ Viloyat tanlashda xatolik yuz berdi, iltimos quyidagi viloyatlardan birini tanlang!") # noqa
    await state.update_data(from_region=message.text)
    await state.set_state(DriverState.from_district)
    await message.answer("❗️ Tumanni tanlang", reply_markup=make_district(message.text).as_markup(resize_keyboard=True))


@take_client_router.message(DriverState.from_district)
async def process_from_district(message: Message, state: FSMContext):
    region_name = (await state.get_data())['from_region']
    if message.text not in get_districts_by_region(region_name):
        return await message.answer("❗️ Tuman tanlashda xatolik!") # noqa
    await state.update_data(from_district=message.text)
    await state.set_state(DriverState.to_region)
    await message.answer("Qayerga bormoqchisiz?", reply_markup=region.as_markup(resize_keyboard=True))


@take_client_router.message(DriverState.to_region)
async def process_to_region(message: Message, state: FSMContext):
    if message.text not in region_list:
        return await message.answer("❗️Viloyat tanlashda xatolik yuz berdi, iltimos quyidagi viloyatlardan birini tanlang!") # noqa
    await state.update_data(to_region=message.text)
    await state.set_state(DriverState.to_district)
    await message.answer("❗️ Tumanni tanlang", reply_markup=make_district(message.text).as_markup(resize_keyboard=True))


@take_client_router.message(DriverState.to_district)
async def process_to_district(message: Message, state: FSMContext):
    region_name = (await state.get_data())['to_region']
    if message.text not in get_districts_by_region(region_name):
        return await message.answer("❗️ Tuman tanlashda xatolik!") # noqa
    await state.update_data(to_district=message.text)
    await state.set_state(DriverState.seats_count)
    await message.answer("❗️ Olib ketuvchi yo'lovchilar soni:\nNamuna: 4", reply_markup=button_1234_driver.as_markup(resize_keyboard=True)) # noqa

@take_client_router.message(DriverState.seats_count) # noqa
async def process_to_district(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(seats_count=int(message.text))
        await state.set_state(DriverState.additional_info)
        return await message.answer("Qo'shimcha ma'lumot kiritishingiz mumkin:", reply_markup=skip.as_markup(resize_keyboard=True)) # noqa
    await message.answer('❗️ Faqat raqamlarda kiriting')


@take_client_router.message(DriverState.additional_info)
async def process_to_district(message: Message, state: FSMContext):
    data = await state.get_data()
    result = """
🏘 Qayerdan: {from_region}, {from_district}
🚕 Qayerga: {to_region}, {to_district}
👤 Yo'lovchilar soni: {seats_count} ta
""".format(**data)
    if message.text != "O'tkazib yuborish":
        await state.update_data(additional_info=message.text)
        result += f"ℹ️ Qo'shimcha ma'lumot: {message.text}"
    await message.answer(result, reply_markup=accept_or_not.as_markup(resize_keyboard=True))


