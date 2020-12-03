import telebot
from telebot import types

bot = telebot.TeleBot("1449898330:AAEyRXaLmSFBu-o9yM218szE1tU107a9zTI")

trup_2_message = 'Мокренький на месте!🤤'
trup_message = 'Мокренький на месте!🤤'
lis_message = 'Мокренький на месте!🤤'
penb_message = 'Мокренький на месте!🤤'
petuk_message = 'Мокренький на месте!🤤'
budya_message = 'Мокренький на месте!🤤'
trup_2_photo = 'https://imgur.com/a/4Xrvt9G'
budya1 = 'https://imgur.com/kqt2APT'
trup1 = 'https://imgur.com/lGuQGwC'
lis1 = 'https://imgur.com/MUGefpj'
petuk1 = 'https://imgur.com/5lMGjHn'
penb1 = 'https://imgur.com/16635d2'



@bot.message_handler(commands = ['start'])
@bot.message_handler(content_types = ['photo'])
def welcome(message):
	welcome_img = 'https://imgur.com/7rgyF0O'
	start_button = types.InlineKeyboardMarkup()
	item_cont = types.InlineKeyboardButton(text = '👉Продолжить👈', callback_data = 'cont')

	start_button.add(item_cont)
	bot.send_photo(message.chat.id, welcome_img, caption='Привет👋, это бот поиска водных апаратов🤤🥵!\nНажимай на кнопку "Прододжить", и выбирай город... \n',
	reply_markup = start_button
	)
@bot.callback_query_handler(func = lambda call: True)
def choose_city(call):
	global trup_2_message
	global trup_message
	global lis_message
	global penb_message
	global petuk_message
	global budya_message
	global j
	global dlid

	global trup_2_photo
	global budya1
	global trup1
	global lis1
	global petuk1
	global penb1

	if call.data == 'torch':
		space_button = types.InlineKeyboardMarkup(row_width = 2)
		item_trup = types.InlineKeyboardButton(text = 'Трупарка👻', callback_data = 'trup')
		item_lis = types.InlineKeyboardButton(text = 'Лісок🌲🌳', callback_data = 'lis')
		item_petuk = types.InlineKeyboardButton(text = 'Пітух🐔', callback_data = 'petuk')
		item_budya = types.InlineKeyboardButton(text = 'В Буді на 3🏢', callback_data = 'budya')
		item_penb = types.InlineKeyboardButton(text = 'Пєньок🌿', callback_data = 'penb')
		item_trup_2 = types.InlineKeyboardButton(text = 'Трупарка 2👻', callback_data = 'trup_2')
		item_support = types.InlineKeyboardButton(text = '⚠️Поменять состояние мокрого⚠️', callback_data = 'support')
		item_back2 = types.InlineKeyboardButton(text = 'Назад🔙', callback_data = 'back2')

		for id in range((call.message.message_id-j), call.message.message_id):
			bot.delete_message(call.message.chat.id, id)

		space_button.add(item_trup, item_trup_2, item_lis, item_petuk, item_budya, item_penb)
		space_button.add(item_support)
		space_button.add(item_back2)
		bot.send_message(call.message.chat.id,'Выбирай место!',
		reply_markup = space_button
		)
		bot.delete_message(call.message.chat.id, call.message.message_id)
	elif call.data == 'back':
		welcome_img = 'https://imgur.com/7rgyF0O'
		back_button = types.InlineKeyboardMarkup()
		item_back = types.InlineKeyboardButton(text = '👉Продолжить👈', callback_data = 'cont')

		bot.delete_message(call.message.chat.id, call.message.message_id)

		back_button.add(item_back)
		bot.send_photo(call.message.chat.id, welcome_img, caption='Привет👋, это бот поиска водных апаратов🤤🥵!\nНажимай на кнопку "Прододжить", и выбирай город... \n',
		reply_markup = back_button
		)
	elif call.data == 'cont':
		city_button = types.InlineKeyboardMarkup(row_width = 1)
		item_sosnovka = types.InlineKeyboardButton(text = 'Сосновка', callback_data = 'sosnovka')
		item_back = types.InlineKeyboardButton(text = 'Назад🔙', callback_data = 'back')

		bot.delete_message(call.message.chat.id, call.message.message_id)

		city_button.add(item_sosnovka, item_back)
		bot.send_message(call.message.chat.id,'Выберете город, в котором нужен мокренький💦: ',
		reply_markup = city_button
		)

	elif call.data == 'sosnovka':
		space_button = types.InlineKeyboardMarkup(row_width = 2)
		item_trup = types.InlineKeyboardButton(text = 'Трупарка👻', callback_data = 'trup')
		item_lis = types.InlineKeyboardButton(text = 'Лісок🌲🌳', callback_data = 'lis')
		item_petuk = types.InlineKeyboardButton(text = 'Пітух🐔', callback_data = 'petuk')
		item_budya = types.InlineKeyboardButton(text = 'В Буді на 3🏢', callback_data = 'budya')
		item_penb = types.InlineKeyboardButton(text = 'Пєньок🌿', callback_data = 'penb')
		item_trup_2 = types.InlineKeyboardButton(text = 'Трупарка 2👻', callback_data = 'trup_2')
		item_support = types.InlineKeyboardButton(text = '⚠️Поменять состояние мокрого⚠️', callback_data = 'support')
		item_back2 = types.InlineKeyboardButton(text = 'Назад🔙', callback_data = 'back2')

		space_button.add(item_trup, item_trup_2, item_lis, item_petuk, item_budya, item_penb)
		space_button.add(item_support)
		space_button.add(item_back2)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'Выбирай место!',
		reply_markup = space_button
		)
	if call.data == 'support':
		j = 0
		support_button = types.InlineKeyboardMarkup(row_width = 2)
		item_trup_support = types.InlineKeyboardButton(text = 'Трупарка', callback_data = 'trup_support')
		item_lis_support = types.InlineKeyboardButton(text = 'Лісок', callback_data = 'lis_support')
		item_petuk_support = types.InlineKeyboardButton(text = 'Пітух', callback_data = 'petuk_support')
		item_budya_support = types.InlineKeyboardButton(text = 'В Буді на 3', callback_data = 'budya_support')
		item_penb_support = types.InlineKeyboardButton(text = 'Пєньок', callback_data = 'penb_support')
		item_trup_2_support = types.InlineKeyboardButton(text = 'Трупарка 2', callback_data = 'trup_2_support')
		item_back3 = types.InlineKeyboardButton(text = 'Назад...', callback_data = 'torch')

		bot.delete_message(call.message.chat.id, call.message.message_id)

		support_button.add(item_trup_support,item_trup_2_support, item_lis_support, item_petuk_support, item_budya_support, item_penb_support)
		support_button.add(item_back3)
		bot.send_message(call.message.chat.id, text = 'Это страница саппорта мокрых\nВыбирай точку, чтобы изменить состояние мокрого)',
		reply_markup = support_button
		)
	if call.data == 'trup_support':
		j = 0
		trup_suppot_button = types.InlineKeyboardMarkup(row_width = 2)
		item_trup_support_here = types.InlineKeyboardButton(text = 'Мокренький на месте ;)', callback_data = 'trup_support_here')
		item_trup_support_nothere = types.InlineKeyboardButton(text = 'Мокренького нет :(', callback_data = 'trup_support_nothere')
		item_trup_support_back = types.InlineKeyboardButton(text = 'Назад', callback_data = 'support')

		bot.delete_message(call.message.chat.id, call.message.message_id)

		trup_suppot_button.add(item_trup_support_here, item_trup_support_nothere)
		trup_suppot_button.add(item_trup_support_back)
		bot.send_message(call.message.chat.id, text = 'Ты выбрал трупарку...\nМокрый на месте?',
		reply_markup = trup_suppot_button
		)
	if call.data == 'trup_support_here':
		trup_message = 'Мокренький на месте!🤤'
		trup1 = 'https://imgur.com/lGuQGwC'
		space_button = types.InlineKeyboardMarkup(row_width = 2)
		item_trup = types.InlineKeyboardButton(text = 'Трупарка👻', callback_data = 'trup')
		item_lis = types.InlineKeyboardButton(text = 'Лісок🌲🌳', callback_data = 'lis')
		item_petuk = types.InlineKeyboardButton(text = 'Пітух🐔', callback_data = 'petuk')
		item_budya = types.InlineKeyboardButton(text = 'В Буді на 3🏢', callback_data = 'budya')
		item_penb = types.InlineKeyboardButton(text = 'Пєньок🌿', callback_data = 'penb')
		item_trup_2 = types.InlineKeyboardButton(text = 'Трупарка 2👻', callback_data = 'trup_2')
		item_support = types.InlineKeyboardButton(text = '⚠️Поменять состояние мокрого⚠️', callback_data = 'support')
		item_back2 = types.InlineKeyboardButton(text = 'Назад🔙', callback_data = 'back2')

		space_button.add(item_trup, item_trup_2, item_lis, item_petuk, item_budya, item_penb)
		space_button.add(item_support)
		space_button.add(item_back2)
		bot.send_message(call.message.chat.id,'Выбирай место!',
		reply_markup = space_button
		)
		bot.delete_message(call.message.chat.id, call.message.message_id)
	elif call.data == 'trup_support_nothere':
		trup_message = 'Мокренького !НЕТ! на месте😞😭'
		trup1 = 'https://imgur.com/a/9SG0AFH'
		space_button = types.InlineKeyboardMarkup(row_width = 2)
		item_trup = types.InlineKeyboardButton(text = 'Трупарка👻', callback_data = 'trup')
		item_lis = types.InlineKeyboardButton(text = 'Лісок🌲🌳', callback_data = 'lis')
		item_petuk = types.InlineKeyboardButton(text = 'Пітух🐔', callback_data = 'petuk')
		item_budya = types.InlineKeyboardButton(text = 'В Буді на 3🏢', callback_data = 'budya')
		item_penb = types.InlineKeyboardButton(text = 'Пєньок🌿', callback_data = 'penb')
		item_trup_2 = types.InlineKeyboardButton(text = 'Трупарка 2👻', callback_data = 'trup_2')
		item_support = types.InlineKeyboardButton(text = '⚠️Поменять состояние мокрого⚠️', callback_data = 'support')
		item_back2 = types.InlineKeyboardButton(text = 'Назад🔙', callback_data = 'back2')

		space_button.add(item_trup, item_trup_2, item_lis, item_petuk, item_budya, item_penb)
		space_button.add(item_support)
		space_button.add(item_back2)
		bot.send_message(call.message.chat.id,'Выбирай место!',
		reply_markup = space_button
		)
		bot.delete_message(call.message.chat.id, call.message.message_id)
	elif call.data == 'back2':
		city_button = types.InlineKeyboardMarkup(row_width = 1)
		item_sosnovka = types.InlineKeyboardButton(text = 'Сосновка', callback_data = 'sosnovka')
		item_back = types.InlineKeyboardButton(text = 'Назад🔙', callback_data = 'back')

		city_button.add(item_sosnovka, item_back)
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = 'Выберете город, в котором нужен мокренький💦: ',
		reply_markup = city_button
		)
	if call.data == 'trup':
		j = 0
		#trup2 = 'https://imgur.com/KifodVA'
		back_button3 = types.InlineKeyboardMarkup()
		item_back3 = types.InlineKeyboardButton(text = 'К точкам📍', callback_data = 'torch')

		bot.delete_message(call.message.chat.id, call.message.message_id)

		#bot.send_photo(call.message.chat.id, trup2)
		back_button3.add(item_back3)
		bot.send_photo(call.message.chat.id, trup1, caption = trup_message,
		reply_markup = back_button3
		)
	if call.data == 'trup_2_support':
		j = 0
		trup_2_suppot_button = types.InlineKeyboardMarkup(row_width = 2)
		item_trup_2_support_here = types.InlineKeyboardButton(text = 'Мокренький на месте ;)', callback_data = 'trup_2_support_here')
		item_trup_2_support_nothere = types.InlineKeyboardButton(text = 'Мокренького нет :(', callback_data = 'trup_2_support_nothere')

		bot.delete_message(call.message.chat.id, call.message.message_id)

		trup_2_suppot_button.add(item_trup_2_support_here, item_trup_2_support_nothere)
		bot.send_message(call.message.chat.id, text = 'Ты выбрал трупарку...\nМокрый на месте?',
		reply_markup = trup_2_suppot_button
		)
	if call.data == 'trup_2_support_here':
		trup_2_photo = 'https://imgur.com/a/4Xrvt9G'
		trup_2_message = 'Мокренький на месте!🤤'
		space_button = types.InlineKeyboardMarkup(row_width = 2)
		item_trup = types.InlineKeyboardButton(text = 'Трупарка👻', callback_data = 'trup')
		item_lis = types.InlineKeyboardButton(text = 'Лісок🌲🌳', callback_data = 'lis')
		item_petuk = types.InlineKeyboardButton(text = 'Пітух🐔', callback_data = 'petuk')
		item_budya = types.InlineKeyboardButton(text = 'В Буді на 3🏢', callback_data = 'budya')
		item_penb = types.InlineKeyboardButton(text = 'Пєньок🌿', callback_data = 'penb')
		item_trup_2 = types.InlineKeyboardButton(text = 'Трупарка 2👻', callback_data = 'trup_2')
		item_support = types.InlineKeyboardButton(text = '⚠️Поменять состояние мокрого⚠️', callback_data = 'support')
		item_back2 = types.InlineKeyboardButton(text = 'Назад🔙', callback_data = 'back2')

		space_button.add(item_trup, item_trup_2, item_lis, item_petuk, item_budya, item_penb)
		space_button.add(item_support)
		space_button.add(item_back2)
		bot.send_message(call.message.chat.id,'Выбирай место!',
		reply_markup = space_button
		)
		bot.delete_message(call.message.chat.id, call.message.message_id)
	elif call.data == 'trup_2_support_nothere':
		trup_2_photo = 'https://imgur.com/a/9SG0AFH'
		trup_2_message = 'Мокренького !НЕТ! на месте😞😭'
		space_button = types.InlineKeyboardMarkup(row_width = 2)
		item_trup = types.InlineKeyboardButton(text = 'Трупарка👻', callback_data = 'trup')
		item_lis = types.InlineKeyboardButton(text = 'Лісок🌲🌳', callback_data = 'lis')
		item_petuk = types.InlineKeyboardButton(text = 'Пітух🐔', callback_data = 'petuk')
		item_budya = types.InlineKeyboardButton(text = 'В Буді на 3🏢', callback_data = 'budya')
		item_penb = types.InlineKeyboardButton(text = 'Пєньок🌿', callback_data = 'penb')
		item_trup_2 = types.InlineKeyboardButton(text = 'Трупарка 2👻', callback_data = 'trup_2')
		item_support = types.InlineKeyboardButton(text = '⚠️Поменять состояние мокрого⚠️', callback_data = 'support')
		item_back2 = types.InlineKeyboardButton(text = 'Назад🔙', callback_data = 'back2')

		space_button.add(item_trup, item_trup_2, item_lis, item_petuk, item_budya, item_penb)
		space_button.add(item_back2)
		bot.send_message(call.message.chat.id,'Выбирай место!',
		reply_markup = space_button
		)
		bot.delete_message(call.message.chat.id, call.message.message_id)
	if call.data == 'trup_2':
		j = 0
		back_button3 = types.InlineKeyboardMarkup()
		item_back3 = types.InlineKeyboardButton(text = 'К точкам📍', callback_data = 'torch')
		item_search_trup_2 = types.InlineKeyboardButton(text = 'Найти мокренький',url = 'https://maps.app.goo.gl/3C3XyJkWzmMhN7C39', callback_data = 'search_trup_2')


		bot.delete_message(call.message.chat.id, call.message.message_id)

		back_button3.add(item_back3, item_search_trup_2)
		bot.send_photo(call.message.chat.id, trup_2_photo, caption = trup_2_message,
		reply_markup = back_button3
		)
	if call.data == 'lis_support':
		j = 0
		lis_suppot_button = types.InlineKeyboardMarkup(row_width = 2)
		item_lis_support_here = types.InlineKeyboardButton(text = 'Мокренький на месте ;)', callback_data = 'lis_support_here')
		item_lis_support_nothere = types.InlineKeyboardButton(text = 'Мокренького нет :(', callback_data = 'lis_support_nothere')
		item_lis_support_back = types.InlineKeyboardButton(text = 'Назад', callback_data = 'support')

		bot.delete_message(call.message.chat.id, call.message.message_id)

		lis_suppot_button.add(item_lis_support_here, item_lis_support_nothere)
		lis_suppot_button.add(item_lis_support_back)
		bot.send_message(call.message.chat.id, text = 'Ты выбрал лісок...\nМокрый на месте?',
		reply_markup = lis_suppot_button
		)
	if call.data == 'lis_support_here':
		lis_message = 'Мокренький на месте!🤤'
		lis1 = 'https://imgur.com/MUGefpj'
		space_button = types.InlineKeyboardMarkup(row_width = 2)
		item_trup = types.InlineKeyboardButton(text = 'Трупарка👻', callback_data = 'trup')
		item_lis = types.InlineKeyboardButton(text = 'Лісок🌲🌳', callback_data = 'lis')
		item_petuk = types.InlineKeyboardButton(text = 'Пітух🐔', callback_data = 'petuk')
		item_budya = types.InlineKeyboardButton(text = 'В Буді на 3🏢', callback_data = 'budya')
		item_penb = types.InlineKeyboardButton(text = 'Пєньок🌿', callback_data = 'penb')
		item_trup_2 = types.InlineKeyboardButton(text = 'Трупарка 2👻', callback_data = 'trup_2')
		item_support = types.InlineKeyboardButton(text = '⚠️Поменять состояние мокрого⚠️', callback_data = 'support')
		item_back2 = types.InlineKeyboardButton(text = 'Назад🔙', callback_data = 'back2')

		space_button.add(item_trup, item_trup_2, item_lis, item_petuk, item_budya, item_penb)
		space_button.add(item_support)
		space_button.add(item_back2)
		bot.send_message(call.message.chat.id,'Выбирай место!',
		reply_markup = space_button
		)
		bot.delete_message(call.message.chat.id, call.message.message_id)
	elif call.data == 'lis_support_nothere':
		lis_message = 'Мокренького !НЕТ! на месте😞😭'
		lis1 = 'https://imgur.com/a/9SG0AFH'
		space_button = types.InlineKeyboardMarkup(row_width = 2)
		item_trup = types.InlineKeyboardButton(text = 'Трупарка👻', callback_data = 'trup')
		item_lis = types.InlineKeyboardButton(text = 'Лісок🌲🌳', callback_data = 'lis')
		item_petuk = types.InlineKeyboardButton(text = 'Пітух🐔', callback_data = 'petuk')
		item_budya = types.InlineKeyboardButton(text = 'В Буді на 3🏢', callback_data = 'budya')
		item_penb = types.InlineKeyboardButton(text = 'Пєньок🌿', callback_data = 'penb')
		item_trup_2 = types.InlineKeyboardButton(text = 'Трупарка 2👻', callback_data = 'trup_2')
		item_support = types.InlineKeyboardButton(text = '⚠️Поменять состояние мокрого⚠️', callback_data = 'support')
		item_back2 = types.InlineKeyboardButton(text = 'Назад🔙', callback_data = 'back2')

		space_button.add(item_trup, item_trup_2, item_lis, item_petuk, item_budya, item_penb)
		space_button.add(item_support)
		space_button.add(item_back2)
		bot.send_message(call.message.chat.id,'Выбирай место!',
		reply_markup = space_button
		)
		bot.delete_message(call.message.chat.id, call.message.message_id)
	elif call.data == 'lis':
		j = 0

		#lis2 = 'https://imgur.com/RclfWRq'
		back_button3 = types.InlineKeyboardMarkup()
		item_back3 = types.InlineKeyboardButton(text = 'К точкам📍', callback_data = 'torch')
		item_search_lis = types.InlineKeyboardButton(text = 'Найти мокренький',url = 'https://goo.gl/maps/zgTv9TspR3bnPbsN9', callback_data = 'search_lis')

		bot.delete_message(call.message.chat.id, call.message.message_id)

		#bot.send_photo(call.message.chat.id, lis2)
		back_button3.add(item_back3, item_search_lis)
		bot.send_photo(call.message.chat.id, lis1, caption = lis_message,
		reply_markup = back_button3
		)
	if call.data == 'penb_support':
		j = 0
		penb_suppot_button = types.InlineKeyboardMarkup(row_width = 2)
		item_penb_support_here = types.InlineKeyboardButton(text = 'Мокренький на месте ;)', callback_data = 'penb_support_here')
		item_penb_support_nothere = types.InlineKeyboardButton(text = 'Мокренького нет :(', callback_data = 'penb_support_nothere')
		item_penb_support_back = types.InlineKeyboardButton(text = 'Назад', callback_data = 'support')

		bot.delete_message(call.message.chat.id, call.message.message_id)

		penb_suppot_button.add(item_penb_support_here, item_penb_support_nothere)
		penb_suppot_button.add(item_penb_support_back)
		bot.send_message(call.message.chat.id, text = 'Ты выбрал пєньок...\nМокрый на месте?',
		reply_markup = penb_suppot_button
		)
	if call.data == 'penb_support_here':
		penb_message = 'Мокренький на месте!🤤'
		penb1 = 'https://imgur.com/16635d2'
		space_button = types.InlineKeyboardMarkup(row_width = 2)
		item_trup = types.InlineKeyboardButton(text = 'Трупарка👻', callback_data = 'trup')
		item_lis = types.InlineKeyboardButton(text = 'Лісок🌲🌳', callback_data = 'lis')
		item_petuk = types.InlineKeyboardButton(text = 'Пітух🐔', callback_data = 'petuk')
		item_budya = types.InlineKeyboardButton(text = 'В Буді на 3🏢', callback_data = 'budya')
		item_penb = types.InlineKeyboardButton(text = 'Пєньок🌿', callback_data = 'penb')
		item_trup_2 = types.InlineKeyboardButton(text = 'Трупарка 2👻', callback_data = 'trup_2')
		item_support = types.InlineKeyboardButton(text = '⚠️Поменять состояние мокрого⚠️', callback_data = 'support')
		item_back2 = types.InlineKeyboardButton(text = 'Назад🔙', callback_data = 'back2')

		space_button.add(item_trup, item_trup_2, item_lis, item_petuk, item_budya, item_penb)
		space_button.add(item_support)
		space_button.add(item_back2)
		bot.send_message(call.message.chat.id,'Выбирай место!',
		reply_markup = space_button
		)
		bot.delete_message(call.message.chat.id, call.message.message_id)
	elif call.data == 'penb_support_nothere':
		penb_message = 'Мокренького !НЕТ! на месте😞😭'
		penb1 = 'https://imgur.com/a/9SG0AFH'
		space_button = types.InlineKeyboardMarkup(row_width = 2)
		item_trup = types.InlineKeyboardButton(text = 'Трупарка👻', callback_data = 'trup')
		item_lis = types.InlineKeyboardButton(text = 'Лісок🌲🌳', callback_data = 'lis')
		item_petuk = types.InlineKeyboardButton(text = 'Пітух🐔', callback_data = 'petuk')
		item_budya = types.InlineKeyboardButton(text = 'В Буді на 3🏢', callback_data = 'budya')
		item_penb = types.InlineKeyboardButton(text = 'Пєньок🌿', callback_data = 'penb')
		item_trup_2 = types.InlineKeyboardButton(text = 'Трупарка 2👻', callback_data = 'trup_2')
		item_support = types.InlineKeyboardButton(text = '⚠️Поменять состояние мокрого⚠️', callback_data = 'support')
		item_back2 = types.InlineKeyboardButton(text = 'Назад🔙', callback_data = 'back2')

		space_button.add(item_trup, item_trup_2, item_lis, item_petuk, item_budya, item_penb)
		space_button.add(item_support)
		space_button.add(item_back2)
		bot.send_message(call.message.chat.id,'Выбирай место!',
		reply_markup = space_button
		)
		bot.delete_message(call.message.chat.id, call.message.message_id)
	elif call.data == 'penb':
		j = 0
		back_button3 = types.InlineKeyboardMarkup()
		item_back3 = types.InlineKeyboardButton(text = 'К точкам📍', callback_data = 'torch')
		item_search_penb = types.InlineKeyboardButton(text = 'Найти мокренький',url = 'https://maps.app.goo.gl/UqKqT18vxd1MBUvp8', callback_data = 'search_penb')

		bot.delete_message(call.message.chat.id, call.message.message_id)


		back_button3.add(item_back3, item_search_penb)
		bot.send_photo(call.message.chat.id, penb1, caption = penb_message,
		reply_markup = back_button3
		)
	if call.data == 'petuk_support':
		j = 0
		petuk_suppot_button = types.InlineKeyboardMarkup(row_width = 2)
		item_petuk_support_here = types.InlineKeyboardButton(text = 'Мокренький на месте ;)', callback_data = 'petuk_support_here')
		item_petuk_support_nothere = types.InlineKeyboardButton(text = 'Мокренького нет :(', callback_data = 'petuk_support_nothere')
		item_petuk_support_back = types.InlineKeyboardButton(text = 'Назад', callback_data = 'support')

		bot.delete_message(call.message.chat.id, call.message.message_id)

		petuk_suppot_button.add(item_petuk_support_here, item_petuk_support_nothere)
		petuk_suppot_button.add(item_petuk_support_back)
		bot.send_message(call.message.chat.id, text = 'Ты выбрал пєтух...\nМокрый на месте?',
		reply_markup = petuk_suppot_button
		)
	if call.data == 'petuk_support_here':
		petuk_message = 'Мокренький на месте!🤤'
		petuk1 = 'https://imgur.com/5lMGjHn'
		space_button = types.InlineKeyboardMarkup(row_width = 2)
		item_trup = types.InlineKeyboardButton(text = 'Трупарка👻', callback_data = 'trup')
		item_lis = types.InlineKeyboardButton(text = 'Лісок🌲🌳', callback_data = 'lis')
		item_petuk = types.InlineKeyboardButton(text = 'Пітух🐔', callback_data = 'petuk')
		item_budya = types.InlineKeyboardButton(text = 'В Буді на 3🏢', callback_data = 'budya')
		item_penb = types.InlineKeyboardButton(text = 'Пєньок🌿', callback_data = 'penb')
		item_trup_2 = types.InlineKeyboardButton(text = 'Трупарка 2👻', callback_data = 'trup_2')
		item_support = types.InlineKeyboardButton(text = '⚠️Поменять состояние мокрого⚠️', callback_data = 'support')
		item_back2 = types.InlineKeyboardButton(text = 'Назад🔙', callback_data = 'back2')

		space_button.add(item_trup, item_trup_2, item_lis, item_petuk, item_budya, item_penb)
		space_button.add(item_support)
		space_button.add(item_back2)
		bot.send_message(call.message.chat.id,'Выбирай место!',
		reply_markup = space_button
		)
		bot.delete_message(call.message.chat.id, call.message.message_id)
	elif call.data == 'petuk_support_nothere':
		petuk_message = 'Мокренького !НЕТ! на месте😞😭'
		petuk1 = 'https://imgur.com/a/9SG0AFH'
		space_button = types.InlineKeyboardMarkup(row_width = 2)
		item_trup = types.InlineKeyboardButton(text = 'Трупарка👻', callback_data = 'trup')
		item_lis = types.InlineKeyboardButton(text = 'Лісок🌲🌳', callback_data = 'lis')
		item_petuk = types.InlineKeyboardButton(text = 'Пітух🐔', callback_data = 'petuk')
		item_budya = types.InlineKeyboardButton(text = 'В Буді на 3🏢', callback_data = 'budya')
		item_penb = types.InlineKeyboardButton(text = 'Пєньок🌿', callback_data = 'penb')
		item_trup_2 = types.InlineKeyboardButton(text = 'Трупарка 2👻', callback_data = 'trup_2')
		item_support = types.InlineKeyboardButton(text = '⚠️Поменять состояние мокрого⚠️', callback_data = 'support')
		item_back2 = types.InlineKeyboardButton(text = 'Назад🔙', callback_data = 'back2')

		space_button.add(item_trup, item_trup_2, item_lis, item_petuk, item_budya, item_penb)
		space_button.add(item_support)
		space_button.add(item_back2)
		bot.send_message(call.message.chat.id,'Выбирай место!',
		reply_markup = space_button
		)
		bot.delete_message(call.message.chat.id, call.message.message_id)
	elif call.data == 'petuk':
		j = 0

		#petuk2 = 'https://imgur.com/jzoBatc'
		#petuk3 = 'https://imgur.com/mZLbZ5q'
		back_button3 = types.InlineKeyboardMarkup()
		item_back3 = types.InlineKeyboardButton(text = 'К точкам📍', callback_data = 'torch')

		bot.delete_message(call.message.chat.id, call.message.message_id)

		#bot.send_photo(call.message.chat.id, petuk3)
		#bot.send_photo(call.message.chat.id, petuk2)
		back_button3.add(item_back3)
		bot.send_photo(call.message.chat.id, petuk1, caption = petuk_message,
		reply_markup = back_button3
		)
	if call.data == 'budya_support':
		j = 0
		budya_suppot_button = types.InlineKeyboardMarkup(row_width = 2)
		item_budya_support_here = types.InlineKeyboardButton(text = 'Мокренький на месте ;)', callback_data = 'budya_support_here')
		item_budya_support_nothere = types.InlineKeyboardButton(text = 'Мокренького нет :(', callback_data = 'budya_support_nothere')
		item_budya_support_back = types.InlineKeyboardButton(text = 'Назад', callback_data = 'support')

		bot.delete_message(call.message.chat.id, call.message.message_id)

		budya_suppot_button.add(item_budya_support_here, item_budya_support_nothere)
		budya_suppot_button.add(item_budya_support_back)
		bot.send_message(call.message.chat.id, text = 'Ты выбрал мокрий в Буді на 3...\nМокрый на месте?',
		reply_markup = budya_suppot_button
		)
	if call.data == 'budya_support_here':
		budya_message = 'Мокренький на месте!🤤'
		budya1 = 'https://imgur.com/kqt2APT'
		space_button = types.InlineKeyboardMarkup(row_width = 2)
		item_trup = types.InlineKeyboardButton(text = 'Трупарка👻', callback_data = 'trup')
		item_lis = types.InlineKeyboardButton(text = 'Лісок🌲🌳', callback_data = 'lis')
		item_petuk = types.InlineKeyboardButton(text = 'Пітух🐔', callback_data = 'petuk')
		item_budya = types.InlineKeyboardButton(text = 'В Буді на 3🏢', callback_data = 'budya')
		item_penb = types.InlineKeyboardButton(text = 'Пєньок🌿', callback_data = 'penb')
		item_trup_2 = types.InlineKeyboardButton(text = 'Трупарка 2👻', callback_data = 'trup_2')
		item_support = types.InlineKeyboardButton(text = '⚠️Поменять состояние мокрого⚠️', callback_data = 'support')
		item_back2 = types.InlineKeyboardButton(text = 'Назад🔙', callback_data = 'back2')

		space_button.add(item_trup, item_trup_2, item_lis, item_petuk, item_budya, item_penb)
		space_button.add(item_support)
		space_button.add(item_back2)
		bot.send_message(call.message.chat.id,'Выбирай место!',
		reply_markup = space_button
		)
		bot.delete_message(call.message.chat.id, call.message.message_id)
	elif call.data == 'budya_support_nothere':
		budya_message = 'Мокренького !НЕТ! на месте😞😭'
		budya1 = 'https://imgur.com/a/3uM3hVM'
		space_button = types.InlineKeyboardMarkup(row_width = 2)
		item_trup = types.InlineKeyboardButton(text = 'Трупарка👻', callback_data = 'trup')
		item_lis = types.InlineKeyboardButton(text = 'Лісок🌲🌳', callback_data = 'lis')
		item_petuk = types.InlineKeyboardButton(text = 'Пітух🐔', callback_data = 'petuk')
		item_budya = types.InlineKeyboardButton(text = 'В Буді на 3🏢', callback_data = 'budya')
		item_penb = types.InlineKeyboardButton(text = 'Пєньок🌿', callback_data = 'penb')
		item_trup_2 = types.InlineKeyboardButton(text = 'Трупарка 2👻', callback_data = 'trup_2')
		item_support = types.InlineKeyboardButton(text = '⚠️Поменять состояние мокрого⚠️', callback_data = 'support')
		item_back2 = types.InlineKeyboardButton(text = 'Назад🔙', callback_data = 'back2')

		space_button.add(item_trup, item_trup_2, item_lis, item_petuk, item_budya, item_penb)
		space_button.add(item_support)
		space_button.add(item_back2)
		bot.send_message(call.message.chat.id,'Выбирай место!',
		reply_markup = space_button
		)
		bot.delete_message(call.message.chat.id, call.message.message_id)
	elif call.data == 'budya':
		j = 0

		back_button3 = types.InlineKeyboardMarkup()
		item_back3 = types.InlineKeyboardButton(text = 'К точкам📍', callback_data = 'torch')

		bot.delete_message(call.message.chat.id, call.message.message_id)

		back_button3.add(item_back3)
		bot.send_photo(call.message.chat.id, budya1, caption = budya_message,
		reply_markup = back_button3
		)
	if call.data == 'menu':
		welcome_img = 'https://imgur.com/7rgyF0O'
		start_button = types.InlineKeyboardMarkup()
		item_cont = types.InlineKeyboardButton(text = '👉Продолжить👈', callback_data = 'cont')

		bot.delete_message(call.message.chat.id, call.message.message_id)

		start_button.add(item_cont)
		bot.send_photo(call.message.chat.id, welcome_img, caption='Привет👋, это бот поиска водных апаратов🤤🥵!\nНажимай на кнопку "Прододжить", и выбирай город... \n',
		reply_markup = start_button
		)
	#if call.data == 'trup':
		#dlid = 2
	#elif call.data == 'petuk':
		#dlid = 3
	#elif call.data == 'lis':
		#dlid = 2
@bot.message_handler(content_types = ['text'])
def pashalka(message):
	dlid = 1

	if message.text == '420':
		pashalka_button = types.InlineKeyboardMarkup()
		item_garash = types.InlineKeyboardButton(text = 'Показать секретный мокрый', url = 'https://goo.gl/maps/yLjit8ws2HGUBjBn7', callback_data = 'garash')
		item_menu = types.InlineKeyboardButton(text = 'Меню', callback_data = 'menu')

		for id in range((message.message_id-dlid), message.message_id):
			bot.delete_message(message.chat.id, id)

		pashalka_button.add(item_garash)
		pashalka_button.add(item_menu)
		bot.send_message(message.chat.id, '🥳 Поздравляю, ты нашёл секретное место😈',
		reply_markup = pashalka_button)
bot.polling(none_stop = True, interval = 0)
