from aiogram.fsm.state import StatesGroup, State

class AppState(StatesGroup):
    main_state=State()
    create=State()
    update = State()
    
    
    