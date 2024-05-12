import os

from dotenv import load_dotenv

load_dotenv('.env')

TOKEN = os.getenv('USTOZ_SHOGIRT')
ADMIN = os.getenv('ADMIN')




# @main_router.message(F.text == 'Sherik kerak')
# async def partner(message: Message, state: FSMContext):
#     await message.answer(
#         "<b>Sherik topish uchun ariza berish</b>\n\nHozir sizga birnecha savollar beriladi.\n"
#         "Har biriga javob bering. Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va\n"
#         "arizangiz Adminga yuboriladi."
#     )
#     await state.set_state(PartnerState.full_name)
#     await message.answer("<b>Ism, familiyangizni kiriting?</b>")

#### BUNDAN TAGINI OQIY OLOLMAYAPTI

# @main_router.message(PartnerState.full_name)
# async def full_name(message: Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     await state.set_state(PartnerState.texnology)
#     await message.answer("<b>📚 Texnologiya:</b>\n\n"
#                          "Talab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating."
#                          "\n\n"
#                          "<em>Masalan: Java, C++, C#</em>")

#
# @main_router.message(PartnerState.full_name)
# async def register(message: Message, state: FSMContext):
#     await state.update_data(full_name=message.text)
#     await state.set_state(PartnerState.texnology)
#     await message.answer("<b>📚 Texnologiya:</b>\n\n"
#                          "Talab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating."
#                          "\n\n"
#                          "<em>Masalan: Java, C++, C#</em>")
#
#
# @main_router.message(PartnerState.texnology)
# async def register_technology(message: Message, state: FSMContext):
#     await state.update_data(technology=message.text)
#     await state.set_state(PartnerState.phone_number)
#     await message.answer("<b>📞 Aloqa:</b>\n\n"
#                          "Bog`lanish uchun raqamingizni kiriting?"
#                          "\nMasalan: +998 90 123 45 67")
#
#
# @main_router.message(PartnerState.phone_number)
# async def register_phone(message: Message, state: FSMContext):
#     await state.update_data(phone_number=message.text)
#     await state.set_state(PartnerState.location)
#     await message.answer("<b>🌐 Hudud: </b>\n\n"
#                          "Qaysi hududdansiz?"
#                          "\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
#
#
# @main_router.message(PartnerState.location)
# async def register_location(message: Message, state: FSMContext):
#     await state.update_data(location=message.text)
#     await state.set_state(PartnerState.price)
#     await message.answer("<b>💰 Narxi:</b>\n\n"
#                          "Tolov qilasizmi yoki Tekinmi??"
#                          "\nKerak bo`lsa, Summani kiriting?")
#
#
# @main_router.message(PartnerState.price)
# async def register_price(message: Message, state: FSMContext):
#     await state.update_data(price=message.text)
#     await state.set_state(PartnerState.job)
#     await message.answer("<b>👨🏻‍💻 Kasbi: </b>\n\n"
#                          "Ishlaysizmi yoki o`qiysizmi?"
#                          "\nMasalan, Talaba")
#
#
# @main_router.message(PartnerState.job)
# async def register_job(message: Message, state: FSMContext):
#     await state.update_data(job=message.text)
#     await state.set_state(PartnerState.time)
#     await message.answer("<b>🕰 Murojaat qilish vaqti: </b>\n\n"
#                          "Qaysi vaqtda murojaat qilish mumkin?"
#                          "\nMasalan, 9:00 - 18:00")
#
#
# @main_router.message(PartnerState.time)
# async def register_time(message: Message, state: FSMContext):
#     await state.update_data(time=message.text)
#     await state.set_state(PartnerState.goal)
#     await message.answer("<b>🔎 Maqsad: </b>\n\n"
#                          "Maqsadingizni qisqacha yozib bering.")
#
#
# @main_router.message(PartnerState.goal)
# async def register_goal(message: Message, state: FSMContext):
#     await state.update_data(goal=message.text)
#     data = await state.get_data()
#     await state.clear()
#     text = f""" Hammasi to'rimi tekshiring:
# 🏅 Sherik: {data.get('full_name')}
# 📚 Texnologiya: {data.get('technology')}
# 🇺🇿 Telegram: @{str(message.from_user.username)}
# 📞 Aloqa: {data.get('phone_number')}
# 🌐 Hudud: {data.get('location')}
# 💰 Narxi: {data.get('price')}
# 👨🏻‍💻 Kasbi: {data.get('job')}
# 🕰 Murojaat qilish vaqti: {data.get('time')}
# 🔎 Maqsad: {data.get('goal')}
# """
#     await message.answer(text)
#     rkb = ReplyKeyboardBuilder()
#     rkb.row(KeyboardButton(text="Ha"), KeyboardButton(text="Yo'q"))
#     await message.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=rkb.as_markup(resize_keyboard=True))
#
#
# @main_router.message(F.text == 'Hodim kerak')
# async def partner(message: Message, state: FSMContext):
#     await message.answer(
#         "<b>Ish joyi topish uchun ariza berish</b>\n\nHozir sizga birnecha savollar beriladi.\n"
#         "Har biriga javob bering. Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va\n"
#         "arizangiz Adminga yuboriladi."
#     )
#     await state.set_state(WorkState.office_name)
#     await message.answer("<b>🎓 Idora nomi?</b>")
#
#
# @main_router.message(WorkState.office_name)
# async def register(message: Message, state: FSMContext):
#     await state.update_data(office_name=message.text)
#     await state.set_state(WorkState.texnology)
#     await message.answer("<b>📚 Texnologiya:</b>\n\n"
#                          "Talab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating."
#                          "\n\n"
#                          "<em>Masalan: Java, C++, C#</em>")
#
#
# @main_router.message(WorkState.texnology)
# async def register_technology(message: Message, state: FSMContext):
#     await state.update_data(technology=message.text)
#     await state.set_state(WorkState.phone_number)
#     await message.answer("<b>📞 Aloqa:</b>\n\n"
#                          "Bog`lanish uchun raqamingizni kiriting?"
#                          "\nMasalan: +998 90 123 45 67")
#
#
# @main_router.message(WorkState.phone_number)
# async def register_phone(message: Message, state: FSMContext):
#     await state.update_data(phone_number=message.text)
#     await state.set_state(WorkState.location)
#     await message.answer("<b>🌐 Hudud: </b>\n\n"
#                          "Qaysi hududdansiz?"
#                          "\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
#
#
# @main_router.message(WorkState.phone_number)
# async def register_phone(message: Message, state: FSMContext):
#     await state.update_data(phone_number=message.text)
#     await state.set_state(WorkState.location)
#     await message.answer("<b>🌐 Hudud: </b>\n\n"
#                          "Qaysi hududdansiz?"
#                          "\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
#
#
# @main_router.message(WorkState.location)
# async def register_location(message: Message, state: FSMContext):
#     await state.update_data(location=message.text)
#     await state.set_state(WorkState.responsible_person)
#     await message.answer("<b>✍️Mas'ul ism sharifi?  </b>")
#
#
# @main_router.message(WorkState.responsible_person)
# async def register_job(message: Message, state: FSMContext):
#     await state.update_data(responsible_person=message.text)
#     await state.set_state(WorkState.time)
#     await message.answer("<b>🕰 Murojaat qilish vaqti: </b>\n\n"
#                          "Qaysi vaqtda murojaat qilish mumkin?"
#                          "\nMasalan, 9:00 - 18:00")
#
#
# @main_router.message(WorkState.time)
# async def register_job(message: Message, state: FSMContext):
#     await state.update_data(time=message.text)
#     await state.set_state(WorkState.time_worked)
#     await message.answer("<b>🕰 Ish vaqtini kiriting: </b>\n\n")
#
#
# @main_router.message(WorkState.time_worked)
# async def register_location(message: Message, state: FSMContext):
#     await state.update_data(time_worked=message.text)
#     await state.set_state(WorkState.work_price)
#     await message.answer("<b>💰 Maoshni kiriting: </b>\n\n")
#
#
# @main_router.message(WorkState.work_price)
# async def register_location(message: Message, state: FSMContext):
#     await state.update_data(work_price=message.text)
#     await state.set_state(WorkState.informations)
#     await message.answer("<b>‼️ Qo`shimcha ma`lumotlar: </b>\n\n")
#
#
# @main_router.message(WorkState.informations)
# async def register_location(message: Message, state: FSMContext):
#     await state.update_data(informations=message.text)
#     data = await state.get_data()
#     await state.clear()
#     text = f""" Hammasi to'rimi tekshiring:
#         🏢 Idora: {data.get('full_name')}
#         📚 Texnologiya: {data.get('technology')}
#         🇺🇿 Telegram: {data.get(message.from_user.full_name)}
#         📞 Aloqa: {data.get('phone_number')}
#         🌐 Hudud: {data.get('location')}
#         🕰 Murojaat qilish vaqti: {data.get('time')}
#         🕰 Ish vaqti: {data.get('time_work')}
#         💰 Maosh: {data.get('price')}
#         👨‼️ Qo`shimcha: {data.get('information')}
# """
#     await message.answer(text)
#     await message.answer('Saqlandi')
