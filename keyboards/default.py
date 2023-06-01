from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton

main_menu = ReplyKeyboardBuilder([
    [KeyboardButton(text='🧍‍♂️ Haydovchi kerak')],
    [KeyboardButton(text='🚕 Haydovchiman')],
    [KeyboardButton(text='🆘 Aloqa')],
    [KeyboardButton(text='🔰 Panel')]
])
main_menu.adjust(2)


back_to_main = ReplyKeyboardBuilder([
    [KeyboardButton(text='🔝 Asosiy Menyu')]
])