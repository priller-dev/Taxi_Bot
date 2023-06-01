from aiogram.fsm.state import StatesGroup, State


class AuthState(StatesGroup):
    full_name = State()
    phone = State()
