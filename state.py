from aiogram.fsm.state import State, StatesGroup


class PartnerState(StatesGroup):
    full_name = State()
    age = State()
    texnology = State()
    phone_number = State()
    location = State()
    price = State()
    job = State()
    time = State()
    goal = State()


class WorkState(StatesGroup):
    office_name = State()
    texnology = State()
    phone_number = State()
    location = State()
    responsible_person = State()
    time = State()
    time_worked = State()
    work_price = State()
    informations = State()
