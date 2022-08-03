from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#физики
url_fiz = InlineKeyboardMarkup(row_width=1)

but_fiz1 = InlineKeyboardButton(text='⭐ Омская область', callback_data='fiz_menu_1')
but_fiz2 = InlineKeyboardButton(text='🇷🇺 Всероссийские гранты', callback_data='fiz_menu_2')
but_fiz_back = InlineKeyboardButton(text='⬅️ Назад', callback_data='fiz_menu_3')




#физики омск
url_fiz_omsk = InlineKeyboardMarkup(row_width=1)

but_fiz_omsk2 = InlineKeyboardButton(text='Молодежный форум РИТМ\n 🗓 18 - 24 июля', callback_data='fiz_omsk_menu_2')
but_fiz_omsk_back = InlineKeyboardButton(text='⬅️ Назад', callback_data='fiz_omsk_menu_3')


#физики омск грант назад
url_fiz_omsk_back1 = InlineKeyboardMarkup(row_width=1)

but_fiz_omsk_back1 = InlineKeyboardButton(text='⬅️ Назад', callback_data='but_fiz_omsk_back1_menu_1')

#физики Россия
url_fiz_rus = InlineKeyboardMarkup(row_width=1)

but_fiz_rus1 = InlineKeyboardButton(text='Таврида.Арт\n🗓 12 июня-5 октября', callback_data='fiz_rus_menu_1')
but_fiz_rus4 = InlineKeyboardButton(text='❌ ШУМ\n 🗓 21-27 июня', callback_data='fiz_rus_menu_4')
but_fiz_rus5 = InlineKeyboardButton(text='❌ Ладога\n 🗓 23-30 июня', callback_data='fiz_rus_menu_5')
but_fiz_rus6 = InlineKeyboardButton(text='Территория смыслов\n 🗓 июль-август', callback_data='fiz_rus_menu_6')
but_fiz_rus7 = InlineKeyboardButton(text='❌ Бирюса\n 🗓 11-17 июля', callback_data='fiz_rus_menu_7')
but_fiz_rus8 = InlineKeyboardButton(text='❌ Среда\n 🗓 11-20 июля', callback_data='fiz_rus_menu_8')
but_fiz_rus9 = InlineKeyboardButton(text='❌ Иволга\n 🗓 21-29 июля', callback_data='fiz_rus_menu_9')
but_fiz_rus10 = InlineKeyboardButton(text='Утро\n 🗓 август', callback_data='fiz_rus_menu2_1')
but_fiz_rus11 = InlineKeyboardButton(text='❌ ОстроVa\n 🗓 13-20 августа', callback_data='fiz_rus_menu2_2')
but_fiz_rus12 = InlineKeyboardButton(text='Машук\n 🗓 13-27 августа', callback_data='fiz_rus_menu2_3')
but_fiz_rus13 = InlineKeyboardButton(text='Ростов\n 🗓 7-11 сентября', callback_data='fiz_rus_menu2_4')
but_fiz_rus14 = InlineKeyboardButton(text='Амур\n 🗓 28 сентября-4 октября', callback_data='fiz_rus_menu2_5')
but_fiz_rus15 = InlineKeyboardButton(text='Молодые предприниматели\n 🗓 4-8 августа', callback_data='fiz_rus_menu2_6')
but_fiz_rus16 = InlineKeyboardButton(text='Экосистема\n 🗓 29 августа-4 сентября', callback_data='fiz_rus_menu2_7')
but_fiz_rus17 = InlineKeyboardButton(text='Ржевская битва\n 🗓 18-31 июля', callback_data='fiz_rus_menu2_8')
but_fiz_rusback = InlineKeyboardButton(text='⬅️ Назад', callback_data='fiz_rus_menu2_9')

#физики Россия грант назад
url_fiz_rus_back1 = InlineKeyboardMarkup(row_width=1)

but_fiz_rus_back1 = InlineKeyboardButton(text='⬅️ Назад', callback_data='but_fiz_rus_back1_menu_1')


url_fiz.row(but_fiz1, but_fiz2).insert(but_fiz_back)
url_fiz_omsk.add(but_fiz_omsk2).insert(but_fiz_omsk_back)
url_fiz_omsk_back1.insert(but_fiz_omsk_back1)
url_fiz_rus.add(but_fiz_rus1, but_fiz_rus6, but_fiz_rus17, but_fiz_rus10, but_fiz_rus15, but_fiz_rus12, but_fiz_rus16, but_fiz_rus13, but_fiz_rus14, but_fiz_rus4, but_fiz_rus5, but_fiz_rus7, but_fiz_rus8, but_fiz_rus9, but_fiz_rus11).insert(but_fiz_rusback)
url_fiz_rus_back1.insert(but_fiz_rus_back1)

stats = InlineKeyboardMarkup()    # СОЗДАЁМ ОСНОВУ ДЛЯ ИНЛАЙН КНОПКИ
stats.add(InlineKeyboardButton(f'Нет', callback_data = 'cancle')).add(InlineKeyboardButton(f'Да', callback_data = 'join')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ