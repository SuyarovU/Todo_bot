from aiogram.types import Message
from aiogram import Router
from aiogram.fsm.context import FSMContext
from states import AppState
from db.config import cursor, conn


router = Router()

    
@router.message(AppState.update)
async def update_todo(message: Message, state: FSMContext):
    data = await state.get_data()
    todo_id = data.get('todo_id')
    callback = data.get('callback')
    await callback.answer('yangilandi')
    cursor.execute("UPDATE todos SET todo=? WHERE id=?", (message.text, todo_id))
    conn.commit()
    await state.clear()



   
  
