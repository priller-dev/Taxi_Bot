from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton

main_menu = ReplyKeyboardBuilder([
    [KeyboardButton(text='🧍‍♂️ Haydovchi kerak')],
    [KeyboardButton(text='🚕 Haydovchiman')],
    [KeyboardButton(text='🆘 Aloqa')],
    [KeyboardButton(text='🔰 Panel')]
])
main_menu.adjust(2)

support = ReplyKeyboardBuilder([
    [KeyboardButton(
        text="@taksi_clone_bot botining TAXIDASUPPORT (https://t.me/all_nc) bilan bog'lanish"
    )]
])