from aiogram.types import Message
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from states import AppState
from db.config import cursor, conn


router = Router()

@router.message(F.text=="Todo yaratish")
async def create_handler(message: Message, state: FSMContext):
    await message.answer("Iltimos, todoni kiriting.")
    await state.set_state(AppState.create)
    
@router.message(AppState.create)
async def create_todo(message: Message, state: FSMContext):
    todo = message.text
    user_id = message.from_user.id
    
    cursor.execute("INSERT INTO todos (user_id, todo, status) VALUES (?, ?, ?)",
            (user_id, todo, 0))
    conn.commit()

    await message.answer('Todo yaratildi!')
    await state.clear()



   
  
