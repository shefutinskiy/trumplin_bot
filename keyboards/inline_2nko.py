from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#НКО
url_nko = InlineKeyboardMarkup(row_width=1)

but_nko1 = InlineKeyboardButton(text='⭐ Омская область', callback_data='nko_menu_1')
but_nko2 = InlineKeyboardButton(text='🇷🇺 Всероссийские гранты', callback_data='nko_menu_2')
but_nko_back = InlineKeyboardButton(text='⬅️ Назад', callback_data='nko_menu_3')


#НКО омск
url_nko_omsk = InlineKeyboardMarkup(row_width=1)

but_nko_omsk1 = InlineKeyboardButton(text='❌ Конкурсный отбор ОМСК.ГРАНТ.РФ\n🗓 второе полугодие', callback_data='nko_omsk_menu_1')
but_nko_omsk_back = InlineKeyboardButton(text='⬅️ Назад', callback_data='nko_omsk_menu_2')

#НКО омск грант назад
url_nko_omsk_back1 = InlineKeyboardMarkup(row_width=1)

but_nko_omsk_back1 = InlineKeyboardButton(text='⬅️ Назад', callback_data='but_nko_omsk_back1_menu_1')




#НКО россия
url_nko_rus = InlineKeyboardMarkup(row_width=1)

but_nko_rus1 = InlineKeyboardButton(text='❌ Фонд культурных инициатив\n🗓 20 апреля - 7 июня', callback_data='nko_rus_menu_1')
but_nko_rus2 = InlineKeyboardButton(text='Родные города\n 🗓 второе полугодие', callback_data='nko_rus_menu_2')
but_nko_rus3 = InlineKeyboardButton(text='Фонд Горчакова\n 🗓 15 июля - 15 августа', callback_data='nko_rus_menu_3')
but_nko_rus4 = InlineKeyboardButton(text='Президентские гранты\n 🗓 1 сентября - 15 октября', callback_data='nko_rus_menu_4')
but_nko_rus_back = InlineKeyboardButton(text='⬅️ Назад', callback_data='nko_rus_menu_5')


#НКО Россия грант назад
url_nko_rus_back1 = InlineKeyboardMarkup(row_width=1)

but_nko_rus_back1 = InlineKeyboardButton(text='⬅️ Назад', callback_data='but_nko_rus_back1_menu_1')


url_nko.row(but_nko1, but_nko2).insert(but_nko_back)
url_nko_omsk.add(but_nko_omsk1).insert(but_nko_omsk_back)
url_nko_omsk_back1.insert(but_nko_omsk_back1)
url_nko_rus.add(but_nko_rus3, but_nko_rus4, but_nko_rus1).insert(but_nko_rus_back)
url_nko_rus_back1.insert(but_nko_rus_back1)