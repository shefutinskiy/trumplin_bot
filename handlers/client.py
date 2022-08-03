from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from create_bot import dp, bot

from keyboards import kb_client

from keyboards import url_fiz, url_fiz_omsk, url_fiz_omsk_back1, url_fiz_rus, url_fiz_rus_back1
from keyboards import url_nko, url_nko_omsk, url_nko_omsk_back1, url_nko_rus, url_nko_rus_back1
from keyboards import url_mer, url_mer_back
from keyboards import stats

from keyboards import ritm2, tavrida1, shum4, ladoga5, tersm6, birusa7, sreda8, ivolga9, utro10, ostrova11, mashuk12, rostov13, amur14, predpr15, ekosis16, rzhev17
from keyboards.base_grant import omskgrant1, fondkult1, fondgorch3, fondprez4
from keyboards import mer1, mer2


#@dp.message_handler(commands=['start','help'])

async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, f"Привет, давайте подберём грант ⬇️", reply_markup=kb_client)
		#await message.delete()
	except:
		await message.reply('Оопс, что-то не работает. Сообщите об этом разработчикам: @shefutinskiy')

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
        await message.answer('Привет 👋\
\nУ тебя есть крутая идея, но ты не знаешь, где можно получить финансовую поддержку на ее реализацию?\
\n\nСпециально для тебя мы создали этот чат-бот, где ты всегда сможешь получить информацию об актуальных грантовых конкурсах в Омской области и за ее пределами.\
\n\nПогнали 🔥 \
\n\nДля навгации воспользуйтесь клавиатурой бота 👇')

@dp.message_handler(filters.Text(equals = '🧍 Гранты для физических лиц'))
@dp.message_handler(commands=['Для_физиков'])
async def fiz_command(message: types.Message):
    joinedFile = open("stat/fiz_user.txt","r")
    joinedUsers = set ()
    for line in joinedFile:
        joinedUsers.add(line.strip())

    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("stat/fiz_user.txt","a")
        joinedFile.write(str(message.chat.id)+ " зашёл на физиков\n")
        joinedUsers.add(message.chat.id)
    try:
        await message.answer('Выберем место проведения гранта 👇', reply_markup=url_fiz)
    except:
        await message.reply('Оопс, что-то не работает. Сообщите об этом разработчикам: @shefutinskiy')

@dp.message_handler(filters.Text(equals = '👨‍👩‍👧‍👧 Гранты для организаций и НКО'))
@dp.message_handler(commands=['Для_НКО'])
async def nko_command(message: types.Message):
        joinedFile = open("stat/nko_user.txt","r")
        joinedUsers = set ()
        for line in joinedFile:
            joinedUsers.add(line.strip())

        if not str(message.chat.id) in joinedUsers:
            joinedFile = open("stat/nko_user.txt","a")
            joinedFile.write(str(message.chat.id)+ " зашёл на нко\n")
            joinedUsers.add(message.chat.id)
        try:
            await message.answer('Выберем место проведения гранта 👇', reply_markup=url_nko)
        except:
            await message.reply('Оопс, что-то не работает. Сообщите об этом разработчикам: @shefutinskiy')

@dp.message_handler(filters.Text(equals = '❓ Получить консультацию'))
@dp.message_handler(commands=['Контакты'])
async def kontact_command(message: types.Message):
        await message.answer('Вы можете связаться с нами 👇\
        \n 📞 8 (913) 605-13-40\
        \n 📧 mdms@omskportal.ru\
        \n\n 💬 написать <a href="https://t.me/Andrew_Bem">в телеграме</a>\
        \n 💬 написать <a href="https://api.whatsapp.com/send?phone=79136051340">в WhatsApp</a>\
        \n\n 🤖 Сообщить о неточности информации или баге бота Вы можете разработчику <a href="https://t.me/shefutinskiy">в телеграме</a>')


#статистиказапуска
@dp.message_handler(commands=("start"), state=None)

async def unikal_user(message):
    joinedFile = open("stat/user.txt","r")
    joinedUsers = set ()
    for line in joinedFile:
        joinedUsers.add(line.strip())

    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("stat/user.txt","a")
        joinedFile.write(str(message.chat.id)+ "\n")
        joinedUsers.add(message.chat.id)
    try:
        await bot.send_message(message.from_user.id, f"Привет, давайте подберём грант ⬇️", reply_markup=kb_client)
        #await message.delete()
    except:
        await message.reply('Оопс, что-то не работает. Сообщите об этом разработчикам: @shefutinskiy')

@dp.message_handler(content_types=['text'])
async def get_message(message):
    if message.text == "Социализм победит":
        await bot.send_message(message.chat.id, text = "Вы уверены?", reply_markup=stats, parse_mode='Markdown')

@dp.callback_query_handler(text_contains='join') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "JOIN" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "JOIN"
async def join(call: types.CallbackQuery):
        all_user = sum(1 for line in open('stat/user.txt'))
        fiz_user = sum(1 for line in open('stat/fiz_user.txt'))
        nko_user = sum(1 for line in open('stat/nko_user.txt'))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Вот статистика бота:\
        \nУникальных пользователей - *{all_user}* человек\
        \nИнтересовалось грантами для физ.лиц - *{fiz_user}* раз \
        \nИнтересовалось грантами для НКО - *{nko_user}* раз', parse_mode='Markdown')


@dp.callback_query_handler(text_contains='cancle') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "cancle" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "cancle"
async def cancle(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= "Ну раз передумал, то добро пожаловать в меню!", parse_mode='Markdown')



# ХЭНДЛЕРЫ ФИЗИКОВ
# Омская область
@dp.callback_query_handler(text_contains='fiz_menu_')
async def menu(call: types.CallbackQuery):
    if call.data and call.data.startswith("fiz_menu_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            await call.message.edit_text('В Омской области в ближайшее время пройдут следующие гранты 👇', reply_markup=url_fiz_omsk)
        if code == 2:
            await call.message.edit_text('Калининградская область? Красноярский край? Или Крым? Настраиваем навигатор на грантовые конкурсы росмолодёжи ⬇️', reply_markup=url_fiz_rus)
        if code == 3:
            await call.message.edit_text('Начнём сначала? Воспользуйтесь нижней клавиутурой ⬇️')
        else:
            await bot.answer_callback_query(call.id)





#ГРАНТЫ В ОМСКЕ для физиков
@dp.callback_query_handler(text_contains='fiz_omsk_menu_')
async def menu(call: types.CallbackQuery):
    if call.data and call.data.startswith("fiz_omsk_menu_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 2:
            await call.message.edit_text('О грантовом конкурсе Ритм ⬇️')
            await call.message.answer_photo(photo="http://xn--90agcbozdwe4a.xn--p1ai/wp-content/uploads/2022/06/photo_2022-06-15_01-36-25.jpg")
            await call.message.answer(text=ritm2, reply_markup=url_fiz_omsk_back1)
        if code == 3:
            await call.message.edit_text('Выберем место проведения гранта 👇', reply_markup=url_fiz)
        else:
            await bot.answer_callback_query(call.id)





#кнопка назад от грантов области
@dp.callback_query_handler(text_contains='but_fiz_omsk_back1_menu_1')
async def menu(call: types.CallbackQuery):
    if call.data and call.data.startswith("but_fiz_omsk_back1_menu_1"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            await call.message.answer(text='В Омской области в ближайшее время пройдут следующие гранты 👇', reply_markup=url_fiz_omsk)
        else:
            await bot.answer_callback_query(call.id)



#ГРАНТЫ В России для физиков
@dp.callback_query_handler(text_contains='fiz_rus_menu_')
async def menu(call: types.CallbackQuery):
    if call.data and call.data.startswith("fiz_rus_menu_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            await call.message.edit_text('О грантовом конкурсе Таврида.Арт ⬇️')
            await call.message.answer_photo(photo="https://www.mgpu.ru/wp-content/uploads/2020/04/691-1-78.jpeg")
            await call.message.answer(text=tavrida1, reply_markup=url_fiz_rus_back1)
        if code == 4:
            await call.message.edit_text('О грантовом конкурсе Шум ⬇️')
            await call.message.answer_photo(photo="https://sun9-43.userapi.com/impf/u9-Gy5tyxOzi_XlUAqiGkp93T8UQ0xdRcW2oaw/-nL4a4mU7KU.jpg?size=1590x530&quality=95&crop=0,0,1590,530&sign=604faee371b1445f40e0d66b5dcc272b&type=cover_group")
            await call.message.answer(text=shum4, reply_markup=url_fiz_rus_back1)
        if code == 5:
            await call.message.edit_text('О грантовом конкурсе Ладога ⬇️')
            await call.message.answer_photo(photo="http://sun9-88.userapi.com/BLak5TYIBlpu6zfWl_QVftwlbZGezCMidpdQGw/4WHfUGPFXlg.jpg")
            await call.message.answer(text=ladoga5, reply_markup=url_fiz_rus_back1)
        if code == 6:
            await call.message.edit_text('О грантовом конкурсе Территория смыслов ⬇️')
            await call.message.answer_photo(photo="https://upload.wikimedia.org/wikipedia/commons/a/a3/%D0%A2%D0%A118_%D0%9B%D0%BE%D0%B3%D0%BE%D1%82%D0%B8%D0%BF.jpg")
            await call.message.answer(text=tersm6, reply_markup=url_fiz_rus_back1)
        if code == 7:
            await call.message.edit_text('О грантовом конкурсе Бирюса ⬇️')
            await call.message.answer_photo(photo="http://sun9-57.userapi.com/Z_FK3Q8WAq7hPYNxGYblrB9dJ1DAwUipY3bzHg/CMeKGKiikRM.jpg")
            await call.message.answer(text=birusa7, reply_markup=url_fiz_rus_back1)
        if code == 8:
            await call.message.edit_text('О грантовом конкурсе Среда ⬇️')
            await call.message.answer_photo(photo="https://mirbelogorya.ru/images/stories/news/2022/04/forum.jpg")
            await call.message.answer(text=sreda8, reply_markup=url_fiz_rus_back1)
        if code == 9:
            await call.message.edit_text('О грантовом конкурсе iВолга ⬇️')
            await call.message.answer_photo(photo="https://api.rbsmi.ru/attachments/db8082b5549f3bf11eedbc46c9f8c011bc6f7849/store/crop/0/0/1059/705/800/0/0/4b3183420541cf17b6bd1a771ebfde1e007b0928b8f54e8ff68ce066f48c/0dim_6gc0ws_jpg_crop1624982392.jpg")
            await call.message.answer(text=ivolga9, reply_markup=url_fiz_rus_back1)
        else:
            await bot.answer_callback_query(call.id)

@dp.callback_query_handler(text_contains='fiz_rus_menu2_')
async def menu(call: types.CallbackQuery):
    if call.data and call.data.startswith("fiz_rus_menu2_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            await call.message.edit_text('О грантовом конкурсе Утро ⬇️')
            await call.message.answer_photo(photo="https://sever-press.ru/wp-content/uploads/2019/02/07022019_ytro.jpg")
            await call.message.answer(text=utro10, reply_markup=url_fiz_rus_back1)
        if code == 2:
            await call.message.edit_text('О грантовом конкурсе ОстроVа ⬇️')
            await call.message.answer_photo(photo="http://sun9-23.userapi.com/pWut7gkmYYwq-yJkKRYbzV_mu_Fl_uVf0P7MqA/8BJDGLPnfmQ.jpg")
            await call.message.answer(text=ostrova11, reply_markup=url_fiz_rus_back1)
        if code == 3:
            await call.message.edit_text('О грантовом конкурсе Машук ⬇️')
            await call.message.answer_photo(photo="https://gazetaingush.ru/sites/default/files/styles/juicebox_small/public/pubs/obshchestvo/20200722-ot-ingushetii-na-severo-kavkazskiy-molodezhnyy-onlayn-forum-mashuk-2020-byla-podana-241/mashuk2_0.jpg?itok=uBDCVXWJ")
            await call.message.answer(text=mashuk12, reply_markup=url_fiz_rus_back1)
        if code == 4:
            await call.message.edit_text('О грантовом конкурсе Ростов ⬇️')
            await call.message.answer_photo(photo="http://xn--90agcbozdwe4a.xn--p1ai/wp-content/uploads/2022/06/photo_2022-06-15_02-55-03.jpg")
            await call.message.answer(text=rostov13, reply_markup=url_fiz_rus_back1)
        if code == 5:
            await call.message.edit_text('О грантовом конкурсе Амур ⬇️')
            await call.message.answer_photo(photo="https://uralgufk.ru/sites/default/files/Amur_2018.png")
            await call.message.answer(text=amur14, reply_markup=url_fiz_rus_back1)
        if code == 6:
            await call.message.edit_text('О грантовом конкурсе молодых предпринимателей ⬇️')
            await call.message.answer_photo(photo="http://xn--90agcbozdwe4a.xn--p1ai/wp-content/uploads/2022/06/предпр.png")
            await call.message.answer(text=predpr15, reply_markup=url_fiz_rus_back1)
        if code == 7:
            await call.message.edit_text('О грантовом конкурсе «Экосистема» ⬇️')
            await call.message.answer_photo(photo="http://xn--90agcbozdwe4a.xn--p1ai/wp-content/uploads/2022/06/7c83386a1369f4bc2afd432c186fc109.png")
            await call.message.answer(text=ekosis16, reply_markup=url_fiz_rus_back1)
        if code == 8:
            await call.message.edit_text('О грантовом конкурсе «Ржевская битва: Вахта памяти» ⬇️')
            await call.message.answer_photo(photo="http://xn--90agcbozdwe4a.xn--p1ai/wp-content/uploads/2022/06/ржев.png")
            await call.message.answer(text=rzhev17, reply_markup=url_fiz_rus_back1)
        if code == 9:
            await call.message.edit_text('Выберем место проведения гранта 👇', reply_markup=url_fiz)
        else:
            await bot.answer_callback_query(call.id)




@dp.callback_query_handler(text_contains='but_fiz_rus_back1_menu_')
async def menu(call: types.CallbackQuery):
    if call.data and call.data.startswith("but_fiz_rus_back1_menu_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            await call.message.answer(text='Калининградская область? Красноярский край? Или Крым? Настраиваем навигатор на грантовые конкурсы росмолодёжи ⬇️', reply_markup=url_fiz_rus)
        else:
            await bot.answer_callback_query(call.id)



#НКО
#Омск
@dp.callback_query_handler(text_contains='nko_menu_')
async def menu(call: types.CallbackQuery):
    if call.data and call.data.startswith("nko_menu_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            await call.message.edit_text('В этом году все грантовые конкурсы для НКО на территории Омской области уже состоялись. Но Вы можете ознакомиться с уже прошедшими грантовыми конкурсами 👇', reply_markup=url_nko_omsk)
        if code == 2:
            await call.message.edit_text('В России в ближайшее время пройдут следующие грантовые конкурсы 👇', reply_markup=url_nko_rus)
        if code == 3:
            await call.message.edit_text('Начнём сначала? Воспользуйтесь нижней клавиутурой ⬇️')
        else:
            await bot.answer_callback_query(call.id)

@dp.callback_query_handler(text_contains='nko_omsk_menu_')
async def menu(call: types.CallbackQuery):
    if call.data and call.data.startswith("nko_omsk_menu_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            await call.message.edit_text('О грантовом конкурсе гранты.омск.рф ⬇️')
            await call.message.answer_photo(photo="https://i.ibb.co/nmwt9X2/Screenshot-2.png")
            await call.message.answer(text=omskgrant1, reply_markup=url_nko_omsk_back1)
        if code == 2:
            await call.message.edit_text('Выберем место проведения гранта 👇', reply_markup=url_nko)
        else:
            await bot.answer_callback_query(call.id)

#кнопка назад от грантов области
@dp.callback_query_handler(text_contains='but_nko_omsk_back1_menu_1')
async def menu(call: types.CallbackQuery):
    if call.data and call.data.startswith("but_nko_omsk_back1_menu_1"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            await call.message.answer(text='В этом году все грантовые конкурсы для НКО на территории Омской области уже состоялись. Но Вы можете ознакомиться с уже прошедшими грантовыми конкурсами 👇', reply_markup=url_nko_omsk)
        else:
            await bot.answer_callback_query(call.id)

#РОССИЯ
@dp.callback_query_handler(text_contains='nko_rus_menu_')
async def menu(call: types.CallbackQuery):
    if call.data and call.data.startswith("nko_rus_menu_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            await call.message.edit_text('О грантовом конкурсе Фонда культурных инициатив ⬇️')
            await call.message.answer_photo(photo="https://www.gikit.ru/sites/default/files/foto_gallery/2022/news-04-19/PFKI_Logo-041.png")
            await call.message.answer(text=fondkult1, reply_markup=url_nko_rus_back1)
        if code == 2:
            await call.message.edit_text('О грантовом конкурсе Родные города ⬇️')
            await call.message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0AXk-kKdDfnOhyiSg-Uq92XaNVh3WPwoUvXyq5ebwS3TkzWESFIruoQx3qvsmpIP9VKg&usqp=CAU")
            await call.message.answer(text=rodnie2, reply_markup=url_nko_rus_back1)
        if code == 3:
            await call.message.edit_text('О грантовом конкурсе Фонда Горчакова ⬇️')
            await call.message.answer_photo(photo="https://i2.wp.com/ksors.org/wp-content/uploads/2014/10/KSORS-Partners-logos-gorchakov.png?fit=500%2C500&ssl=1")
            await call.message.answer(text=fondgorch3, reply_markup=url_nko_rus_back1)
        if code == 4:
            await call.message.edit_text('О президентских грантах ⬇️')
            await call.message.answer_photo(photo="http://президентскиегранты.рф/public/static/img/Fpg/fpg-logo.png")
            await call.message.answer(text=fondprez4, reply_markup=url_nko_rus_back1)
        if code == 5:
            await call.message.edit_text('Выберем место проведения гранта 👇', reply_markup=url_nko)
        else:
            await bot.answer_callback_query(call.id)




@dp.callback_query_handler(text_contains='but_nko_rus_back1_menu_')
async def menu(call: types.CallbackQuery):
    if call.data and call.data.startswith("but_nko_rus_back1_menu_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            await call.message.answer(text='В России в ближайшее время пройдут следующие грантовые конкурсы 👇', reply_markup=url_nko_rus)
        else:
            await bot.answer_callback_query(call.id)



#мероприятия
@dp.callback_query_handler(text_contains='mer_menu_')
async def menu(call: types.CallbackQuery):
    if call.data and call.data.startswith("mer_menu_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            await call.message.edit_text('Рандомное мероприятие ⬇️')
            await call.message.answer(text=mer1, reply_markup=url_mer_back)
        if code == 2:
            await call.message.edit_text('Ещё одно мероприятие ⬇️')
            await call.message.answer(text=mer2, reply_markup=url_mer_back)
        if code == 3:
            await call.message.edit_text('Начнём сначала? Воспользуйтесь нижней клавиутурой ⬇️')
        else:
            await bot.answer_callback_query(call.id)


def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(command_start, commands=['start','help'])
	dp.register_message_handler(fiz_command, commands=['Для_физиков'])
	dp.register_message_handler(nko_command, commands=['Для_НКО'])
	dp.register_message_handler(kontact_command, commands=['Контакты'])
	#dp.register_message_handler(Location_command, commands=['Расположение'])