from aiogram.fsm.state import State, StatesGroup


class PartnerState(StatesGroup):
    full_name = State()
    age = State()  # {sherik kerakda va xodim kerakda yoq}  (shogird, ustoz, ish joyi)
    texnology = State()
    phone_number = State()
    location = State()
    price = State()  # xodim kerakda
    job = State()  # xodim kerakda
    time = State()
    goal = State()


class Hodim(StatesGroup):
    idora = State()
    texnology = State()
    phone_number = State()
    location = State()
    masul = State()
    time = State()
    time_worked = State()
    price = State()
    another = State()
