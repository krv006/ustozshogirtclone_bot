from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from state import PartnerState, Hodim

main_router = Router()


@main_router.message(CommandStart())
async def start(message: Message):
    rkb = ReplyKeyboardBuilder()
    rkb.row(KeyboardButton(text='Sherik kerak'), KeyboardButton(text='Ish joyi kerak'))
    rkb.row(KeyboardButton(text='Hodim kerak'), KeyboardButton(text='Ustoz kerak'))
    rkb.row(KeyboardButton(text='Shogird kerak'))
    await message.answer(
        f'Assalomu alaykum {message.from_user.first_name} \nUstozShogird kanalining rasmiy botiga xush kelibsiz!',
        reply_markup=rkb.as_markup(resize_keyboard=True))


@main_router.message(F.text.startswith(('Sherik', 'Ish', 'Ustoz', 'Shogird')))
async def partner(message: Message, state: FSMContext):
    await state.update_data(button_name=message.text)
    data = await state.get_data()
    if data['button_name'].startswith('Ish'):
        await message.answer(
            "<b>Ish joyi topish uchun ariza berish</b>\n\nHozir sizga birnecha savollar beriladi.\n"
            "Har biriga javob bering. Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va\n"
            "arizangiz Adminga yuboriladi."
        )
    elif data['button_name'].startswith('Ustoz'):
        await message.answer(
            "<b>Ustoz topshirish uchun ariza berish</b>\n\nHozir sizga birnecha savollar beriladi.\n"
            "Har biriga javob bering. Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va\n"
            "arizangiz Adminga yuboriladi."
        )
    elif data['button_name'].startswith('Sherik'):
        await message.answer(
            "<b>Sherik topshirish uchun ariza berish</b>\n\nHozir sizga birnecha savollar beriladi.\n"
            "Har biriga javob bering. Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va\n"
            "arizangiz Adminga yuboriladi."
        )
    else:
        await message.answer(
            "<b>Shogirt topshirish uchun ariza berish</b>\n\nHozir sizga birnecha savollar beriladi.\n"
            "Har biriga javob bering. Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va\n"
            "arizangiz Adminga yuboriladi."
        )
    await state.set_state(PartnerState.full_name)
    await message.answer("<b>Ism, familiyangizni kiriting?</b>")


@main_router.message(PartnerState.full_name)
async def full_name(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    data = await state.get_data()
    if data['button_name'] == 'Sherik':
        await state.set_state(PartnerState.texnology)
    else:
        await message.answer("<b>🕑 Yosh: </b>\n\n"
                             "Yoshingizni kiriting?"
                             "Masalan, 19")
        await state.set_state(PartnerState.age)


@main_router.message(PartnerState.age)
async def register(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(PartnerState.texnology)
    await message.answer("<b>📚 Texnologiya:</b>\n\n"
                         "Talab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating."
                         "\n\n"
                         "<em>Masalan: Java, C++, C#</em>")


@main_router.message(PartnerState.texnology)
async def register_technology(message: Message, state: FSMContext):
    await state.update_data(technology=message.text)
    await state.set_state(PartnerState.phone_number)
    await message.answer("<b>📞 Aloqa:</b>\n\n"
                         "Bog`lanish uchun raqamingizni kiriting?"
                         "\nMasalan: +998 90 123 45 67")


@main_router.message(PartnerState.phone_number)
async def register_phone(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await state.set_state(PartnerState.location)
    await message.answer("<b>🌐 Hudud: </b>\n\n"
                         "Qaysi hududdansiz?"
                         "\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")


@main_router.message(PartnerState.location)
async def register_location(message: Message, state: FSMContext):
    await state.update_data(location=message.text)
    await state.set_state(PartnerState.price)
    await message.answer("<b>💰 Narxi:</b>\n\n"
                         "Tolov qilasizmi yoki Tekinmi??"
                         "\nKerak bo`lsa, Summani kiriting?")


@main_router.message(PartnerState.price)
async def register_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await state.set_state(PartnerState.job)
    await message.answer("<b>👨🏻‍💻 Kasbi: </b>\n\n"
                         "Ishlaysizmi yoki o`qiysizmi?"
                         "\nMasalan, Talaba")


@main_router.message(PartnerState.job)
async def register_job(message: Message, state: FSMContext):
    await state.update_data(job=message.text)
    await state.set_state(PartnerState.time)
    await message.answer("<b>🕰 Murojaat qilish vaqti: </b>\n\n"
                         "Qaysi vaqtda murojaat qilish mumkin?"
                         "\nMasalan, 9:00 - 18:00")


@main_router.message(PartnerState.time)
async def register_time(message: Message, state: FSMContext):
    await state.update_data(time=message.text)
    await state.set_state(PartnerState.goal)
    await message.answer("<b>🔎 Maqsad: </b>\n\n"
                         "Maqsadingizni qisqacha yozib bering.")


@main_router.message(PartnerState.goal)
async def register_goal(message: Message, state: FSMContext):
    await state.update_data(goal=message.text)
    data = await state.get_data()
    await state.clear()

    text = ""
    if data['button_name'].startswith('Ish'):
        text += f"<b>Ish joyi kerak:</b>\n\n👨‍💼 Xodim: {data.get('full_name')}\n"
    elif data['button_name'].startswith('Ustoz'):
        text += f"<b>Ustoz kerak:</b>\n\n👨‍💼 Ustoz: {data.get('full_name')}\n"
    else:
        text += f"<b>Shogird kerak:</b>\n\n👨‍💼 Shogird: {data.get('full_name')}\n"

    text += f"""🕑 Yosh: {data.get('age')}
📚 Texnologiya: {data.get('technology')}
🇺🇿 Telegram: @{str(message.from_user.username)}
📞 Aloqa: {data.get('phone_number')}
🌐 Hudud: {data.get('location')}
💰 Narxi: {data.get('price')}
👨🏻‍💻 Kasbi: {data.get('job')}
🕰 Murojaat qilish vaqti: {data.get('time')}
🔎 Maqsad: {data.get('goal')}
"""
    if data['button_name'].startswith('Sherik'):
        text = f"""<b>Sherik kerak:</b>\n\n👨‍💼 Sherik: {data.get('full_name')}
📚 Texnologiya: {data.get('technology')}
🇺🇿 Telegram: @{str(message.from_user.username)}
📞 Aloqa: {data.get('phone_number')}
🌐 Hudud: {data.get('location')}
💰 Narxi: {data.get('price')}
👨🏻‍💻 Kasbi: {data.get('job')}
🕰 Murojaat qilish vaqti: {data.get('time')}
🔎 Maqsad: {data.get('goal')}

            """
    await message.answer(text)
    await message.answer('Saqlandi')


@main_router.message(F.text.startswith(('Hodim')))
async def partner(message: Message, state: FSMContext):
    await message.answer(
        "<b>Hodim topshirish uchun ariza berish</b>\n\nHozir sizga birnecha savollar beriladi.\n"
        "Har biriga javob bering. Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va\n"
        "arizangiz Adminga yuboriladi."
    )
    await state.update_data(button_name=message.text)
    await state.set_state(Hodim.idora)
    await message.answer("<b>🎓 Idora nomi??</b>")


@main_router.message(Hodim.idora)
async def register(message: Message, state: FSMContext):
    await state.update_data(idora=message.text)
    await state.set_state(Hodim.texnology)
    await message.answer("<b>📚 Texnologiya:</b>\n\n"
                         "Talab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating."
                         "\n\n"
                         "<em>Masalan: Java, C++, C#</em>")


@main_router.message(Hodim.texnology)
async def register_technology(message: Message, state: FSMContext):
    await state.update_data(technology=message.text)
    await state.set_state(Hodim.phone_number)
    await message.answer("<b>📞 Aloqa:</b>\n\n"
                         "Bog`lanish uchun raqamingizni kiriting?"
                         "\nMasalan: +998 90 123 45 67")


@main_router.message(Hodim.phone_number)
async def register_phone(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await state.set_state(Hodim.location)
    await message.answer("<b>🌐 Hudud: </b>\n\n"
                         "Qaysi hududdansiz?"
                         "\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")


@main_router.message(Hodim.location)
async def register_location(message: Message, state: FSMContext):
    await state.update_data(location=message.text)
    await state.set_state(Hodim.time)
    await message.answer("<b>🕰 Murojaat qilish vaqti: </b>\n\n"
                         "Qaysi vaqtda murojaat qilish mumkin?"
                         "\nMasalan, 9:00 - 18:00")


@main_router.message(Hodim.time)
async def register_price(message: Message, state: FSMContext):
    await state.update_data(time=message.text)
    await state.set_state(Hodim.time_worked)
    await message.answer("<b>🕰 Ish vaqtini kiriting? </b>")


@main_router.message(Hodim.time_worked)
async def register_job(message: Message, state: FSMContext):
    await state.update_data(time_worked=message.text)
    await state.set_state(Hodim.price)
    await message.answer("<b>💰 Narxi:</b>\n\n"
                         "Tolov qilasizmi yoki Tekinmi??"
                         "\nKerak bo`lsa, Summani kiriting?")


@main_router.message(Hodim.price)
async def register_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await state.set_state(Hodim.another)
    await message.answer("<b>‼️ Qo`shimcha ma`lumotlar? </b>\n\n")


@main_router.message(Hodim.another)
async def register_goal(message: Message, state: FSMContext):
    await state.update_data(goal=message.text)
    data = await state.get_data()
    await state.clear()
    text = f"""
🏢 Idora: {data.get('idora')}
📚 Texnologiya: {data.get('technology')}
🇺🇿 Telegram: @{str(message.from_user.username)}
📞 Aloqa: {data.get('phone_number')}
🌐 Hudud: {data.get('location')}
✍️ Mas'ul: {data.get('masul')}
🕰 Murojaat qilish vaqti: {data.get('time')}
🕰 Ish vaqti: {data.get('time_worked')}
💰 Maosh: {data.get('price')}
‼️ Qo`shimcha: {data.get('another')}
"""
    await message.answer(text)
    await message.answer('Saqlandi')
