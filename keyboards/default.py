from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton
import json

main_menu = ReplyKeyboardBuilder([
    [KeyboardButton(text='🧍‍♂️ Haydovchi kerak')],
    [KeyboardButton(text='🚕 Haydovchiman')],
    [KeyboardButton(text='🆘 Aloqa')],
    [KeyboardButton(text='🔰 Panel')]
])
main_menu.adjust(2)

menu = [KeyboardButton(text='🔝 Asosiy Menyu')]

back_to_main = ReplyKeyboardBuilder([
    menu
])

panel_menu = ReplyKeyboardBuilder([
    [KeyboardButton(text='💳 Balans')],
    [KeyboardButton(text='📈 Kanal / Guruh')],
    [KeyboardButton(text="♾ Majburiy a'zo bot")],
    [KeyboardButton(text="👥 Referal")],
    [KeyboardButton(text="⚙️ Sozlamalar")],
    [KeyboardButton(text="🆘 Yordam")],
    menu
])
panel_menu.adjust(2)

panel_channel = ReplyKeyboardBuilder([
    [KeyboardButton(text="Kanal qo'shish")],
    [KeyboardButton(text="Guruh qo'shish ")],
    menu
])
panel_channel.adjust(2)

# majburiy
panel_mandatory = ReplyKeyboardBuilder([
    [KeyboardButton(text="Majbur guruh qo'shish")],
    menu
])

panel_referal = ReplyKeyboardBuilder([
    [KeyboardButton(text="Reklama posti")],
    [KeyboardButton(text="Reklama post video")],
    [KeyboardButton(text="Referallar ro'yxati")],
    [KeyboardButton(text="🔙 Orqaga")],
    menu
])
panel_referal.adjust(2)

"""passenger"""

passenger_menu = ReplyKeyboardBuilder([
    [KeyboardButton(text="Yetib borish")],
    [KeyboardButton(text="Yetkazib berish")],
    menu
])
passenger_menu.adjust(2)

"""driver"""

driver_menu = ReplyKeyboardBuilder([
    [KeyboardButton(text="Yo'lovchi kutish")],
    [KeyboardButton(text="Hisobingiz")],
    [KeyboardButton(text="Ma'lumotlarni o'zgartirish")],
    [KeyboardButton(text="🔙 Orqaga")],
    menu
])
driver_menu.adjust(2)

# hisob
driver_accaunt = ReplyKeyboardBuilder([
    [KeyboardButton(text="CLICK")],
    [KeyboardButton(text="PAYME")],
    menu
])

driver_accaunt.adjust(2)

"""region_district"""
list_reg = []
with open('/home/abror/Taxi_Bot_musharraf/region_district/reg_dis.json') as f:
    d: dict = json.load(f)
    for i in d.keys():
        print(i)
        list_reg += [[KeyboardButton(text=i)]]
region = ReplyKeyboardBuilder(list_reg + [menu])
region.adjust(2)


def make_district(region):
    with open('/home/abror/Taxi_Bot_musharraf/region_district/reg_dis.json') as f:
        data: dict = json.load(f)
        districts = data.get(region)
        buttons = [[KeyboardButton(text=district)] for district in districts]
    districts_buttons = ReplyKeyboardBuilder(buttons + [menu])
    return districts_buttons
