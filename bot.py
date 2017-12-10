import telebot
from db import *
import log
import feedback
import feedback_full
import config
import maps_info
import weather
import time
import basicMarkup

bot = telebot.TeleBot(config.token)
basicMarkup = basicMarkup.basicMarkup(bot)
global weatherMessage, MESSAGE
weatherMessage = ""
MESSAGE = ""
currentTime = time.ctime(time.time())
rebootmsg = ("I've been rebooted: %s" % currentTime)
bot.send_message(config.telegramID, rebootmsg)
print("Messages".center(50, '~'))

def log_info(message, answer):
    from _datetime import datetime
    print(datetime.now())
    str_message = "Message from {0} {1},id = {2},\nText of message: {3}".format(message.from_user.first_name,
                                                                             message.from_user.last_name,
                                                                             str(message.from_user.id), message.text)
    print(str_message)
    print("Text of answer: ", answer)
    print("~" * 50, "\n")

def download_pdf(message, doc_name):
    directory = './documents'
    doc_name = str(doc_name)
    doc = open(directory + '/' + doc_name + '.pdf', 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_document')
    bot.send_document(message.from_user.id, doc)
    log_info(message, 'Result: '+str(bot.send_chat_action(message.from_user.id, 'upload_document')))
    doc.close()
def download_doc(message, doc_name):
    directory = './documents'
    doc_name = str(doc_name)
    doc = open(directory + '/' + doc_name + '.doc', 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_document')
    bot.send_document(message.from_user.id, doc)
    log_info(message, 'Result: '+str(bot.send_chat_action(message.from_user.id, 'upload_document')))
    doc.close()


@bot.message_handler(commands=['start'])
def start(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        basicMarkup.mainMenu(message)
    elif isUserInDB(message) and not isUserLoggedIn(message):
        basicMarkup.singInMenu(message)
    else:
        basicMarkup.singUpMenu(message)
    log.logging(message)

@bot.message_handler(regexp='Что делать, если наступил страховой случай' + ' ' + '\U0001F3E5')
def insurance_occurRequest(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        basicMarkup.insurance_occurMenu(message)
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Произошел страховой случай, что делать?")
def insurance_occur0Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        basicMarkup.insurance_occurMenu(message)
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Медицинские расходы")
def medical_refund00Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        basicMarkup.medical_refundMenu(message)
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Несчастный случай")
def accident01Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        basicMarkup.accidentMenu(message)
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Пропажа багажа")
def luggage_dissapearance02Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        basicMarkup.luggage_dissapearanceMenu(message)
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Отмена поездки")
def trip_canceled03Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        basicMarkup.trip_canceledMenu(message)
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Вызов врача")
def maps000Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        bot.send_message(message.from_user.id, "Выберете то, что вас интересует:",
                         reply_markup=basicMarkup.mapsMenu(message))
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Амбулаторное или стационарное лечение")
def maps001Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        bot.send_message(message.from_user.id, "Выберете то, что вас интересует:",
                         reply_markup=basicMarkup.mapsMenu(message))
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Проведение операции")
def maps002Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        bot.send_message(message.from_user.id, "Выберете то, что вас интересует:",
                         reply_markup=basicMarkup.mapsMenu(message))
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Стоматологические услуги")
def maps003Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        bot.send_message(message.from_user.id, "Выберете то, что вас интересует:",
                         reply_markup=basicMarkup.mapsMenu(message))
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Врачебные услуги (перевязки)")
def maps004Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        bot.send_message(message.from_user.id, "Выберете то, что вас интересует:",
                         reply_markup=basicMarkup.mapsMenu(message))
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Ранение")
def maps010Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        bot.send_message(message.from_user.id, "Выберете то, что вас интересует:",
                         reply_markup=basicMarkup.mapsMenu(message))
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Ушиб, вывих или растяжение")
def maps011Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        bot.send_message(message.from_user.id, "Выберете то, что вас интересует:",
                         reply_markup=basicMarkup.mapsMenu(message))
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Ожог")
def maps012Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        bot.send_message(message.from_user.id, "Выберете то, что вас интересует:",
                         reply_markup=basicMarkup.mapsMenu(message))
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Перелом")
def maps013Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        bot.send_message(message.from_user.id, "Выберете то, что вас интересует:",
                         reply_markup=basicMarkup.mapsMenu(message))
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Заявление об утере багажа")
def docs020Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        basicMarkup.docsMenu(message)
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Акт перевозчика")
def docs021Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        basicMarkup.docsMenu(message)
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Бирки")
def docs022Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        basicMarkup.docsMenu(message)
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Расходный кассовый ордер")
def docs023Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        basicMarkup.docsMenu(message)
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Полис")
def docs024Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        basicMarkup.docsMenu(message)
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Заявление об отмене поездки")
def docs0300Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        basicMarkup.docsMenu(message)
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Полис")
def docs0301Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        basicMarkup.docsMenu(message)
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Загранпаспорт")
def docs0302Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        basicMarkup.docsMenu(message)
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Договор")
def docs0303Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        basicMarkup.docsMenu(message)
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Подтверждение расходов")
def docs0304Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        basicMarkup.docsMenu(message)
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Другие")
def docs0305Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        basicMarkup.docsMenu(message)
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Список необходимых документов")
def treaty_cancel03003Request(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        basicMarkup.open_doc_cancelMenu(message)
    else:
        pass
    log.logging(message)





@bot.message_handler(regexp='Погода' +' '+'\U00002614')
def weatherRequest(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        basicMarkup.weatherMenu(message)
    else:
        pass
    log.logging(message)



@bot.message_handler(regexp='Наши организации на карте' + ' ' + '\U0001F5FA')
def mapsRequest(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        #global MESSAGE
        #MESSAGE = "MAPS"
        bot.send_message(message.from_user.id, "Выберете то, что вас интересует:", reply_markup=basicMarkup.mapsMenu(message))
    else:
        pass
    log.logging(message)



@bot.message_handler(regexp='Контакты'+' \U0000260E')
def contactRequest(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        basicMarkup.contactMenu(message)
    else:
        pass
    log.logging(message)
@bot.message_handler(regexp='Стикеры'+' '+'\U0001F426')
def stickerRequest(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        basicMarkup.stickerMenu(message)
    else:
        pass
    log.logging(message)
@bot.message_handler(regexp='Обратная связь'+' \U0001F4DD')
def feedbackRequest(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        bot.send_message(message.from_user.id, "Оцените, пожалуйста, работу нашего чат-бота", reply_markup=basicMarkup.one_Menu(message))
        markup = basicMarkup.feedbackMenu(message)
        bot.send_message(message.from_user.id, "Поставьте нам оценку:", reply_markup=markup)

        @bot.callback_query_handler(func=lambda call: call.data[0:4] == 'vote')
        def get_result(call):
            answer = call.data[4:]
            log_info(message, call.data[4:])
            bot.answer_callback_query(call.id, text="Спасибо за ваш ответ")
            if (answer is not None):
                feedback.log_feedback(message, answer)
                bot.send_message(message.from_user.id,
                                      "Вы можете еще немного нам помочь:",
                                      reply_markup=basicMarkup.answer_feedback_Menu(message))

    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Сейчас")
def weatherRequestLater(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        global weatherMessage
        weatherMessage = "Сейчас"
        bot.send_message(message.from_user.id, 'Как я могу вас найти?', reply_markup=basicMarkup.MenuTwo_city_loc(message))
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Оставить свои пожелания по работе чат-бота")
def feedback_answer_full(message):
    def feedback(message):
        if isUserInDB(message) and isUserLoggedIn(message):
            answer = message.text
            bot.send_message(message.chat.id, 'Спасибо за ваш ответ', reply_markup=basicMarkup.backButton())
            feedback_full.log_feedback_full(message, answer)
        else:
            pass

    if isUserInDB(message) and isUserLoggedIn(message):
        bot.register_next_step_handler(message, feedback)
    log.logging(message)

@bot.message_handler(regexp="Через три часа")
def weatherRequestLater(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        global weatherMessage
        weatherMessage = "Через три часа"
        bot.send_message(message.from_user.id, 'Как я могу вас найти?', reply_markup=basicMarkup.MenuTwo_city_loc(message))
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Завтра утром")
def weatherRequestLater(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        global weatherMessage
        weatherMessage = "Завтра утром"
        bot.send_message(message.from_user.id, 'Как я могу вас найти?', reply_markup=basicMarkup.MenuTwo_city_loc(message))
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp="Указать город")
def weatherByCity(message):
    def weatherCityNow(message):
        try:
            if isUserInDB(message) and isUserLoggedIn(message):
                city = message.text
                cityName, county, main, description, celsius, humidity, wind = weather.byCity(city)
                bot.send_message(message.from_user.id, "Вот какая погода для твоего города: %s, %s \nТемпература: %d%s \nВлажность: %i%s \nВетер: %s м/с \nОписание: %s%s " % (cityName, county, celsius, ' \U000000B0'+'C', humidity, "%", wind, main, description), reply_markup=basicMarkup.backButton())
                log.logging(message)
            else:
                pass
        except UnicodeEncodeError:
            bot.send_message(message.from_user.id, "Пожалуйста, введите по английски")
            log.logging(message)
    def weatherCityLater(message):
        try:
            if isUserInDB(message) and isUserLoggedIn(message):
                city = message.text
                cityName, county, main, description, celsius, humidity, wind = weather.byCityLater(city)
                bot.send_message(message.from_user.id, "Вот какая погода для твоего города: %s, %s \nТемпература: %d%s \nВлажность: %i%s \nВетер: %s м/с \nОписание: %s%s " % (cityName, county, celsius, ' \U000000B0'+'C', humidity, "%", wind, main, description), reply_markup=basicMarkup.backButton())
                log.logging(message)
            else:
                pass
        except UnicodeEncodeError:
            bot.send_message(message.from_user.id, "Пожалуйста, введите по английски")
            log.logging(message)
    def weatherCityTomorow(message):
        try:
            if isUserInDB(message) and isUserLoggedIn(message):
                city = message.text
                cityName, county, main, description, celsius, humidity, wind = weather.byCityTomorow(city)
                bot.send_message(message.from_user.id, "Вот какая погода для твоего города: %s, %s \nТемпература: %d%s \nВлажность: %i%s \nВетер: %s м/с \nОписание: %s%s " % (cityName, county, celsius, ' \U000000B0'+'C', humidity, "%", wind, main, description), reply_markup=basicMarkup.backButton())
                log.logging(message)
            else:
                pass
        except UnicodeEncodeError:
            bot.send_message(message.from_user.id, "Пожалуйста, введите по английски")
            log.logging(message)
    if isUserInDB(message) and isUserLoggedIn(message):
        msg = bot.send_message(message.from_user.id, "Какой город?")
        global weatherMessage
        if weatherMessage == "Сейчас":
            bot.register_next_step_handler(msg, weatherCityNow)
        elif weatherMessage == "Через три часа":
            bot.register_next_step_handler(msg, weatherCityLater)
        elif weatherMessage == "Завтра утром":
            bot.register_next_step_handler(msg, weatherCityTomorow)
        weatherMessage = ""
    else:
        pass
    log.logging(message)

@bot.message_handler(regexp='Клиники "Будь здоров" \U0001F98B')
def office_clinic(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        global MESSAGE
        MESSAGE = 'Клиники Будь Здоров'
        bot.send_message(message.from_user.id, 'Как я могу вас найти?', reply_markup=basicMarkup.Menu_map_loc(message))
    else:
        pass
    log.logging(message)
@bot.message_handler(regexp="Другие медицинские учреждения рядом \U0001F691")
def med(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        global MESSAGE
        MESSAGE = 'Все клиники'
        bot.send_message(message.from_user.id, 'Как я могу вас найти?',
                         reply_markup=basicMarkup.Menu_map_loc(message))
    else:
        pass
    log.logging(message)
@bot.message_handler(regexp="Офисы Ингосстрах \U0001F3E6")
def office(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        global MESSAGE
        MESSAGE = 'Офисы'
        bot.send_message(message.from_user.id, 'Как я могу вас найти?',
                         reply_markup=basicMarkup.Menu_map_loc(message))
    else:
        pass
    log.logging(message)

@bot.message_handler(content_types=['location'])
def LOCATION(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        global weatherMessage, MESSAGE
        if weatherMessage == "Сейчас":
            cityName, county, main, description, celsius, humidity, wind = weather.byGeo(message)
            bot.send_message(message.from_user.id,
                             "Вот какая погода для твоего местонахождения: %s, %s \nТемпература: %d%s \nВлажность: %i%s \nВетер: %s м/с \nОписание: %s%s " % (
                             cityName, county, celsius, ' \U000000B0' + 'C', humidity, "%", wind, main, description),
                             reply_markup=basicMarkup.backButton())

        elif weatherMessage == "Через три часа":
            cityName, county, main, description, celsius, humidity, wind = weather.byGeoLater(message)
            bot.send_message(message.from_user.id,
                             "Вот какая погода для твоего местонахождения: %s, %s \nТемпература: %d%s \nВлажность: %i%s \nВетер: %s м/с \nОписание: %s%s " % (
                             cityName, county, celsius, ' \U000000B0' + 'C', humidity, "%", wind, main, description),
                             reply_markup=basicMarkup.backButton())

        elif weatherMessage == "Завтра утром":
            cityName, county, main, description, celsius, humidity, wind = weather.byGeoTomorow(message)
            bot.send_message(message.from_user.id,
                             "Вот какая погода для твоего местонахождения: %s, %s \nТемпература: %d%s \nВлажность: %i%s \nВетер: %s м/с \nОписание: %s%s " % (
                             cityName, county, celsius, ' \U000000B0' + 'C', humidity, "%", wind, main, description),
                             reply_markup=basicMarkup.backButton())

        elif MESSAGE == "Все клиники":
            bot.send_message(message.from_user.id, "Вот, что я нашел для тебя:")
            for i in range(4):
                try:
                    name, vicinity, open, rating, dist = maps_info.MAPS(message, i, MESSAGE)
                    bot.send_message(message.from_user.id,
                                     "Название: %s \nАдрес: %s \nСтатус: %s \nРейтинг: %s \nРасстояние: %s км\n\n " % (
                                         name, vicinity, open, rating, dist),
                                     reply_markup=basicMarkup.backButton())
                except IndexError:
                    pass
        elif MESSAGE == "Клиники Будь Здоров":
            bot.send_message(message.from_user.id, "Вот, что я нашел для тебя:")
            for i in range(4):
                try:
                    name, vicinity, open, rating, dist = maps_info.MAPS(message, i, MESSAGE)
                    bot.send_message(message.from_user.id,
                                     "Название: %s \nАдрес: %s \nСтатус: %s \nРейтинг: %s \nРасстояние: %s км\n\n " % (
                                         name, vicinity, open, rating, dist),
                                     reply_markup=basicMarkup.backButton())
                except IndexError:
                    pass
        elif MESSAGE == "Офисы":
            bot.send_message(message.from_user.id, "Вот, что я нашел для тебя:")
            for i in range(4):
                try:
                    name, vicinity, open, rating, dist = maps_info.MAPS(message, i, MESSAGE)
                    bot.send_message(message.from_user.id,
                                     "Название: %s \nАдрес: %s \nСтатус: %s \nРейтинг: %s \nРасстояние: %s км\n\n " % (
                                         name, vicinity, open, rating, dist),
                                     reply_markup=basicMarkup.backButton())
                except IndexError:
                    pass
        else:
            pass
        weatherMessage = ""
        MESSAGE = ""
    else:
        pass
    log.logging(message)


@bot.message_handler(regexp="Главное меню \U0001F3E0")
def handle_text(message):
    basicMarkup.mainMenu(message)
    log.logging(message)

@bot.message_handler(regexp="Sign in")
def sgnIN(message):
    def signin(message):
        authorization(message)
        if isUserInDB(message) and isUserLoggedIn(message):
            bot.send_message(message.from_user.id, "Welcome back!")
            basicMarkup.mainMenu(message)
        else:
            bot.send_message(message.from_user.id, "Failed, try again!")
    msg = bot.send_message(message.from_user.id, "Enter your password")
    try:
        bot.register_next_step_handler(msg, signin)
    except Exception as e:
        bot.send_message(message.from_user.id, "Failed, try again!")
    log.logging(message)

@bot.message_handler(regexp="Sign up")
def sgnUP(message):
    def signup(message):
        createNewUser(message)
        if isUserLoggedIn(message):
            bot.send_message(message.from_user.id, "Welcome!")
            basicMarkup.mainMenu(message)
        else:
            bot.send_message(message.from_user.id, "Failed, try again!")
    msg = bot.send_message(message.from_user.id, "Enter your password")
    try:
        bot.register_next_step_handler(msg, signup)
    except Exception as e:
        bot.send_message(message.from_user.id, "Failed, try again!")
    log.logging(message)


@bot.message_handler(commands=['stop'])
def handle_stop(message):
    bot.send_message(message.from_user.id, 'Bye...', reply_markup=telebot.types.ReplyKeyboardRemove())
    log.logging(message)


@bot.message_handler(regexp ='Документы'+' '+'\U0001F4D2')
def docs(message):
    if isUserInDB(message) and isUserLoggedIn(message):
        basicMarkup.docsMenu(message)
    else:
        pass
    log.logging(message)


@bot.message_handler(content_types=['text'])
def handle_command(message):
    if message.text =="Привет" or  message.text =="Здравствуйте" or message.text =="Hello" or message.text =="Hi":
        answer = "Hello"
        bot.send_message(message.from_user.id, answer)
        log_info(message, answer)

    elif message.text =="Пока" or  message.text =="До свидания" or message.text =="Bye" or message.text =="See you again":
        answer = "See you again"
        bot.send_message(message.from_user.id, answer)
        log_info(message, answer)

    elif message.text == 'Образцы заявлений':
        doc_user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        doc_user_markup.row('1)Заявлeние по медицинским расходам')
        doc_user_markup.row('2)Если вы потеряли багаж')
        doc_user_markup.row('3)Случился невыезд')
        doc_user_markup.row('4)Страховой случай, связанный с невыездом вашего ребенка')
        doc_user_markup.row("Главное меню \U0001F3E0")
        bot.send_message(message.from_user.id, 'Set of documents:', reply_markup=doc_user_markup)
    elif message.text == 'Правила страхования':
        doc_user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        doc_user_markup.row('1)Правила страхования медицинских расходов')
        doc_user_markup.row('2)Правила страхования гражданской ответственности физических лиц')
        doc_user_markup.row('3)Правила страхования багажа')
        doc_user_markup.row('4)Правила страхования от отмены поездки')
        doc_user_markup.row('5)Правила страхования от несчастных случаев')
        doc_user_markup.row('6)Таблица размеров страховых выплат по страхованию от НС')
        doc_user_markup.row("Главное меню \U0001F3E0")
        bot.send_message(message.from_user.id, 'Set of documents:', reply_markup=doc_user_markup)
    elif message.text == '1)Заявлeние по медицинским расходам':
        download_doc(message, 'zvl_na_vplt_med')
    elif message.text == '2)Если вы потеряли багаж':
        download_doc(message, 'luggage1')
    elif message.text == '3)Случился невыезд':
        download_doc(message, 'nvzd')
    elif message.text == '4)Страховой случай, связанный с невыездом вашего ребенка':
        download_doc(message, 'nvzd-child')
    elif message.text == '1)Правила страхования медицинских расходов':
        download_pdf(message, 'med_abroad')
    elif message.text == '2)Правила страхования гражданской ответственности физических лиц':
        download_pdf(message, 'go_fiz')
    elif message.text == '3)Правила страхования багажа':
        download_pdf(message, 'luggage2')
    elif message.text == '4)Правила страхования от отмены поездки':
        download_pdf(message, 'NeviezdPravila')
    elif message.text == '5)Правила страхования от несчастных случаев':
        download_pdf(message, 'nc_abroad')
    elif message.text == '6)Таблица размеров страховых выплат по страхованию от НС':
        download_pdf(message, 'table_nc')
    log.logging(message)

bot.polling(none_stop=True)
