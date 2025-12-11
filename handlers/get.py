from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from states import AppState
from db.config import cursor
from keyboards import inline_menu


router = Router()

@router.message(F.text=="Jami todolar")
async def create_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    cursor.execute("SELECT id, todo, status FROM todos WHERE user_id=?", (user_id,))
    rows = cursor.fetchall()
    for i, todo in enumerate(rows):
        if todo[2]==True:
            status = "Bajarilgan"
        else:
            status = "Bajarilmagan"
        todo_id = todo[0]
        await message.answer(f'''{i+1}. {todo[1]}
\nStatus: {status}''', reply_markup=inline_menu(todo_id))
    
   
    




   
  
