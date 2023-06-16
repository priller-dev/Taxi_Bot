from aiogram.fsm.state import StatesGroup, State


class AuthState(StatesGroup):
    full_name = State()
    phone = State()

class AuthDriverState(StatesGroup):
    car_name = State()
    car_number = State()


class DriverState(StatesGroup):
    from_region = State()
    from_district = State()
    to_region = State()
    to_district = State()
    seats_count = State()
    additional_info = State()


class ClientState(StatesGroup):
    from_region = State()
    from_district = State()
    to_region = State()
    to_district = State()
    price = State()
    passenger_count = State()
    additional_info = State()

