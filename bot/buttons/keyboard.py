from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

async def get_card_table():
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Оплатить")]])