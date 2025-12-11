from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from states import AppState
from db.config import cursor, conn
from keyboards import inline_menu
from aiogram.types import CallbackQuery
from states import AppState

router = Router()


@router.callback_query()
async def handle_callback(callback:CallbackQuery, state: FSMContext):
    todo_id = callback.data.split('_')[1]
    if callback.data.startswith("yangilash"):
        await state.update_data(todo_id=todo_id, callback=callback)
        await state.set_state(AppState.update)
        await callback.message.answer("Matn kiriting!")

    elif callback.data.startswith("delete"):
        cursor.execute("DELETE FROM todos WHERE id=?", (todo_id,))
        conn.commit()
        await callback.answer("O'chirildi!")

    elif callback.data.startswith("done"):
        cursor.execute("UPDATE todos SET status=? WHERE id=?", (True, todo_id))
        conn.commit()
        await callback.answer("Bajarildi")
    

