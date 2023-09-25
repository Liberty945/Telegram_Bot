from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton('Добавить задачу', callback_data='kb_add'),
        InlineKeyboardButton('Очистить список', callback_data='kb_clear'),  #inline keyboard
    )

    return keyboard