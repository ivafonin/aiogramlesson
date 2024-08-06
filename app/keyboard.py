from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.utils.keyboard import *
kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Hello'),KeyboardButton(text='Hi')]
    ],resize_keyboard=True,input_field_placeholder="Введите текст",
)
cars=['h','j','k']
async def carss():
    keyb = ReplyKeyboardBuilder()
    for car in cars:
        keyb.add(KeyboardButton(text=car))
    return keyb.as_markup()