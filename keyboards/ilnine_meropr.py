from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#мероприятия
url_mer = InlineKeyboardMarkup(row_width=1)

but_mer1 = InlineKeyboardButton(text='Рандомное мероприятие', callback_data='mer_menu_1')
but_mer2 = InlineKeyboardButton(text='Ещё одно мероприятие', callback_data='mer_menu_2')
but_mer3 = InlineKeyboardButton(text='⬅️ Назад', callback_data='mer_menu_3')

url_mer_back = InlineKeyboardMarkup(row_width=1)

but_mer_back = InlineKeyboardButton(text='⬅️ Назад', callback_data='mer_back_menu_1')

url_mer.add(but_mer1, but_mer2).insert(but_mer3)
url_mer_back.insert(but_mer_back)