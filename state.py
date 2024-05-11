from aiogram.fsm.state import State, StatesGroup


class PartnerState(StatesGroup):
    full_name = State()
    age = State() # {sherik kerakda va xodim kerakda yoq}  (shogird, ustoz, ish joyi)
    texnology = State()
    telegram = State()
    phone_number = State()
    location = State()
    masul = State()
    price = State() # xodm kerakda
    job = State() # xodm kerakda
    murojat_qilish = State
    maosh = State() # xodm kerakda
    qoshimcha = State() # xodm kerakda
    time = State()
    goal = State()


