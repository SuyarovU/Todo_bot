from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Todo yaratish")],
        [KeyboardButton(text="Jami todolar")]
    ],
    resize_keyboard=True
)


def inline_menu(todo_id:int): 
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Yangilash", callback_data=f"yangilash_{todo_id}")],
            [InlineKeyboardButton(text="O'chirish", callback_data=f"delete_{todo_id}")],
            [InlineKeyboardButton(text="Bajardim", callback_data=f"done_{todo_id}")]
        ]
    )
