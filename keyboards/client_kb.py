from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('🧍 Гранты для физических лиц')
b2 = KeyboardButton('👨‍👩‍👧‍👧 Гранты для организаций и НКО')
#b3 = KeyboardButton('👨‍🎓 Мероприятия и семинары по грантам')
b4 = KeyboardButton('❓ Получить консультацию')
#b4 = KeyboardButton('Поделиться контактом', request_contact=True)
#b5 = KeyboardButton('Поделиться геолокацией', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

#one_time_keyboard=True - скрыть клаву
#kb_client.add(b1).add(b2).add(b3) в вертикаль
#kb_client.add(b1).add(b2).insert(b3) в свободное место
#kb_client.row(b1, b2, b3) в строку

kb_client.row(b1, b2).row(b4)