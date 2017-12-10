import telebot


class basicMarkup():
    def __init__(self, bot):
        super(basicMarkup, self).__init__()
        self.bot = bot

    def insurance_occurMenu(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        keyboard.row("Медицинские расходы")
        keyboard.row("Несчастный случай")
        keyboard.row("Пропажа багажа")
        keyboard.row("Отмена поездки")
        keyboard.row("Главное меню \U0001F3E0")
        self.bot.send_message(message.from_user.id, "Выберите страховой случай", reply_markup=keyboard)

    def medical_refundMenu(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        keyboard.row("Вызов врача")
        keyboard.row("Амбулаторное или стационарное лечение")
        keyboard.row("Проведение операции")
        keyboard.row("Стоматологические услуги")
        keyboard.row("Врачебные услуги (перевязки)")
        keyboard.row("Главное меню \U0001F3E0")
        self.bot.send_message(message.from_user.id, "Выбор характера требуемой помощи", reply_markup=keyboard)

    def accidentMenu(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        keyboard.row("Ранение")
        keyboard.row("Ушиб, вывих или растяжение")
        keyboard.row("Ожог")
        keyboard.row("Перелом")
        keyboard.row("Главное меню \U0001F3E0")
        self.bot.send_message(message.from_user.id, "Выбор характера требуемой помощи", reply_markup=keyboard)

    def luggage_dissapearanceMenu(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        keyboard.row("Заявление об утере багажа")
        keyboard.row("Акт перевозчика")
        keyboard.row("Бирки")
        keyboard.row("Расходный кассовый ордер")
        keyboard.row("Полис")
        keyboard.row("Главное меню \U0001F3E0")
        self.bot.send_message(message.from_user.id,
                              "Необходимо сообщить о пропаже сотрудникам транспортной организации, получить документы пропажи багажа или письменный отказ",
                              reply_markup=keyboard)

    def trip_canceledMenu(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        keyboard.row("Список необходимых документов")
        keyboard.row("Главное меню \U0001F3E0")
        self.bot.send_message(message.from_user.id,
                              "Напишите заявление в страховую о наступлении страхового случая в течении 7 дней с момента наступления",
                              reply_markup=keyboard)

    def open_doc_cancelMenu(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        keyboard.row("Заявление об отмене поездки")
        keyboard.row("Полис")
        keyboard.row("Загранпаспорт")
        keyboard.row("Договор")
        keyboard.row("Подтверждение расходов")
        keyboard.row("Другие")
        keyboard.row("Главное меню \U0001F3E0")
        self.bot.send_message(message.from_user.id, "Выберите необходимый документ", reply_markup=keyboard)

    def mainMenu(self, message):
        self.message = message
        user_markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        #user_markup.row('/start', '/stop')
        user_markup.row('Что делать, если наступил страховой случай' + ' ' + '\U0001F3E5')
        user_markup.row('Наши организации на карте' + ' ' + '\U0001F5FA', 'Документы' + ' ' + '\U0001F4D2')
        user_markup.row('Погода' +' '+'\U00002614', 'Стикеры'+' '+'\U0001F426')
        user_markup.row('Контакты'+' \U0000260E', 'Обратная связь'+' \U0001F4DD')
        self.bot.send_message(message.from_user.id, 'Выберете из меню то, что вас интересует', reply_markup=user_markup)

    def singUpMenu(self, message):
        self.message = message
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("Sign up")
        self.bot.send_message(message.from_user.id, "I don't know you!", reply_markup=user_markup)

    def singInMenu(self, message):
        self.message = message
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("Sign up")
        self.bot.send_message(message.from_user.id, "I can't remember you..", reply_markup=user_markup)

    def weatherMenu(self, message):
        self.message = message
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("Сейчас")
        user_markup.row("Через три часа")
        user_markup.row("Завтра утром")
        user_markup.row("Главное меню \U0001F3E0")
        self.bot.send_message(message.from_user.id, "Когда?", reply_markup=user_markup)


    def mapsMenu(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button1 = telebot.types.KeyboardButton(text="Офисы Ингосстрах \U0001F3E6")
        button2 = telebot.types.KeyboardButton(text='Клиники "Будь здоров" \U0001F98B')
        button3 = telebot.types.KeyboardButton(text="Другие медицинские учреждения рядом \U0001F691")
        back_btn = telebot.types.KeyboardButton(text="Главное меню \U0001F3E0")
        keyboard.add(button1)
        keyboard.add(button2)
        keyboard.add(button3)
        keyboard.add(back_btn)
        return keyboard
    def one_Menu(self, message):
        self.message = message
        keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        back_main = telebot.types.KeyboardButton(text="Главное меню \U0001F3E0")
        keyboard.add(back_main)
        return keyboard

    def stickerMenu(self, message):
        self.message = message
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Наши стикеры", url="https://t.me/addstickers/hackingos")
        keyboard.add(url_button)

        self.bot.send_message(message.chat.id, "Посмотрите какие красивые стикеры мы для вас сделали \U0001F308 \n",
                              reply_markup=keyboard)



    def answer_feedback_Menu(self, message):
        self.message = message
        keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button_answer = telebot.types.KeyboardButton(text="Оставить свои пожелания по работе чат-бота")
        back_main = telebot.types.KeyboardButton(text="Главное меню \U0001F3E0")
        keyboard.add(button_answer)
        keyboard.add(back_main)
        return keyboard


    def feedbackMenu(self, message):
        self.message = message
        markup = telebot.types.InlineKeyboardMarkup()
        row = []
        row.append(telebot.types.InlineKeyboardButton("\U00002B50" * 5, callback_data="vote5"))
        row.append(telebot.types.InlineKeyboardButton("\U00002B50" * 4, callback_data="vote4"))
        markup.row(*row)
        row = []
        row.append(telebot.types.InlineKeyboardButton("\U00002B50"*3, callback_data="vote3"))
        row.append(telebot.types.InlineKeyboardButton("\U00002B50"*2, callback_data="vote2"))
        row.append(telebot.types.InlineKeyboardButton("\U00002B50"*1, callback_data="vote1"))
        markup.row(*row)

        return markup

    def contactMenu(self, message):
        self.message = message
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("Главное меню \U0001F3E0")
        self.bot.send_message(message.from_user.id, "Наши контакты \U00002139  \n \n"
                                                    "Телефон контакт-центра \U0001F4DE \n"
                                                    "+7(495)956−55−55 \n \n"
                                                    "Мы в соцсетях: \n"
                                                    "https://www.facebook.com/ingos.ru \n"
                                                    "https://vk.com/ingos9565555 \n"
                                                    "https://www.youtube.com/user/IngosTV ", reply_markup=user_markup)

    def MenuTwo_city_loc(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button_geo = telebot.types.KeyboardButton(text="Отправить локацию", request_location=True)
        button_city = telebot.types.KeyboardButton(text="Указать город")
        back_btn = telebot.types.KeyboardButton(text="Главное меню \U0001F3E0")
        keyboard.add(button_geo)
        keyboard.add(button_city)
        keyboard.add(back_btn)
        return keyboard

    def Menu_map_loc(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button_geo = telebot.types.KeyboardButton(text="Отправить локацию", request_location=True)
        back_btn = telebot.types.KeyboardButton(text="Главное меню \U0001F3E0")
        keyboard.add(button_geo)
        keyboard.add(back_btn)
        return keyboard

    def backButton(self):
        keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        back_btn = telebot.types.KeyboardButton(text="Главное меню \U0001F3E0")
        keyboard.add(back_btn)
        return keyboard

    def docsMenu(self, message):
        doc_user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        doc_user_markup.row('Образцы заявлений')
        doc_user_markup.row('Правила страхования')
        doc_user_markup.row("Главное меню \U0001F3E0")
        self.bot.send_message(message.from_user.id, 'Выберете то, что вас интересует:', reply_markup=doc_user_markup)
