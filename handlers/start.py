from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router
from keyboards import menu

router=Router()

@router.message(CommandStart())
async def start_handler(message:Message):
    await message.answer("Botga start bosildi!", reply_markup=menu)





