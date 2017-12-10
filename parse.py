# -*- coding: utf-8 -*-

def create_text_handler(key, name, expression, reply_message=False):
	'''create code block from given name and message expression as handler'''
	string = ('@bot.message_handler(regexp="' + expression + '")\n'
						'def ' + name + key + 'Request(message):\n'
						'    if isUserInDB(message) and isUserLoggedIn(message):\n')
	if reply_message:
		string += '        bot.send_message(message.from_user.id, "' + reply_message + '", reply_markup=basicMarkup.' + name_m + 'Menu(message))\n'
	else:
		string += (	'        basicMarkup.' + name + 'Menu(message)\n'
							'    else:\n'
							'        pass\n'
							'    log.logging(message)\n\n')
	
	return string
	
def create_text_menu2(name, button_list):
	'''create code block from given name and buttons list as a menu'''
	#button_list: list of tuples, where bl[0] - text, bl[1] - bin location, bl[2] - bin contact
	string = ('def ' + name + 'Menu(self, message):\n'
						'    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)\n')
	for i, button_tuple in enumerate(button_list):
		loc = 'True' if button_tuple[2] == '1' else 'False'
		cont = 'True' if button_tuple[3] == '1' else 'False'
		line += '    button'+str(i)+' = telebot.types.KeyboardButton(text="'+button_tuple[1]+'"\n'
		line += '    keyboard.add(button' + str(i) + ')\n'
		string += line
		
	string += '    return keyboard\n\n'		
	return string
	
def create_text_menu(name, button_list, reply_message):
	'''create code block from given name and buttons list as a menu'''
	if name == 'maps':
		return ''
	#button_list: list of tuples, where bl[0] - text, bl[1] - bin location, bl[2] - bin contact
	string = ('def ' + name + 'Menu(self, message):\n'
						'    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)\n')
	for i, button_tuple in enumerate(button_list):
		string += '    keyboard.row("'+button_tuple[1]+'")\n'

	string += '    keyboard.row("Главное меню' + r' \U0001F3E0")' + "\n"

	string += '    self.bot.send_message(message.from_user.id, "' + reply_message + '", reply_markup=keyboard)\n\n'
	return string
	
def create_answer_menu(name, reply):
	'''create code block from given name and buttons list as a menu'''
	string = ('def ' + name + 'Menu(self, message):\n'
						'    self.bot.send_message(message.from_user.id, "' + reply + '", reply_markup=keyboard)\n\n')
	return string

def parse_file(name):
	'''parsing our menu file'''
	dictionary = {}
	with open(name, 'r', encoding='utf-8') as file:
		for line in file:
			if line.strip():
				line = line.strip('\n')
				split = line.find('|')
				key = line[:split]
				value = line[split + 1:]
				dictionary[key] = value
	return dictionary
		
def parser_button_list(id, menu):
	'''making a button list for this id'''
	button_list = []
	length = len(id)
	for key in menu.keys():
		if len(key) == length + 1 and key[:length] == id:
			button_list.append(tuple(menu[key].strip().split('|')))
	if button_list:
		return button_list
	else:
		return False
		
def parse_helper_id(id, name, button_list, menu, reply):	
	handlers_code = ''
	menu_code = create_text_menu(name, button_list, reply)
	for i, button in enumerate(button_list):
		handlers_code += create_text_handler(id + str(i), button[0], button[1])
	return menu_code, handlers_code
	
def parser():
	'''main function'''
	menu = parse_file('menu.txt')
	menu_code = ''
	handlers_code = ''
	
	button_list = parser_button_list('', menu)
	if button_list:
		m, h = parse_helper_id('', 'main', button_list, menu, '') 
		menu_code += m
		handlers_code += h
			
	for id in menu.keys():
		button_list = parser_button_list(id, menu)
		if button_list:
			name = menu[id].split('|')[0]
			reply = menu[id].split('|')[4]
			m, h = parse_helper_id(id, name, button_list, menu, reply) 
			menu_code += m
			handlers_code += h
		else:
			#return_button = ('return', 'Return to start menu', 0, 0)
			name = menu[id].split('|')[0]
			reply = menu[id].split('|')[4]
			#menu_code += create_answer_menu(name + str(id), reply)
			
	return menu_code, handlers_code
	
m, h = parser()
with open('test_menu.txt', 'w', encoding='utf-8') as file:
	file.write(m)
with open('test_handler.txt', 'w', encoding='utf-8') as file:
	file.write(h)
