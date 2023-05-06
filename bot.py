# Ключ для доступу і керування ботом
BOT_TOKEN = '6055763111:AAFMbPP0-q3w_dA4E-xwf8H2W7hnwYrA3VI'

import telebot 
from telebot import types # для указание типов
import requests
 
# Створюємо обект бот і даємо токен
bot = telebot.TeleBot(BOT_TOKEN)

markup = types.InlineKeyboardMarkup(row_width=1)
first = types.InlineKeyboardButton("1", callback_data="1")
second = types.InlineKeyboardButton("2", callback_data="2")
third = types.InlineKeyboardButton("3", callback_data="3")
fourth = types.InlineKeyboardButton("4", callback_data="4")
fifth = types.InlineKeyboardButton("5", callback_data="5")
sixth = types.InlineKeyboardButton("6", callback_data="6")
seventh = types.InlineKeyboardButton("7", callback_data="7")
eighth = types.InlineKeyboardButton("8", callback_data="8")
nineth = types.InlineKeyboardButton("9", callback_data="9")
tenth = types.InlineKeyboardButton("10", callback_data="10")
markup.add(first, second, third, fourth, fifth, sixth, seventh, eighth, nineth, tenth)

def get_locaion_citi(citi,message):
    location_perms = {
        'name': citi,
    }

    response = requests.get('https://geocoding-api.open-meteo.com/v1/search', params=location_perms)
    data = response.json()
    i = 0
    
    for i in range(len(data['results'])):
        bot.send_message(message.chat.id, data['results'][i]['name'] + ' - ' + str(i+1))

    bot.send_message(message.chat.id, 'Виберіть місто, яке вам потрібне, з цих перерахованих', reply_markup = markup)
    
    location_citit = [
        data['results'][int(choose)-1]['latitude'],
        data['results'][int(choose)-1]['longitude']
    ]

    return location_citit

def get_info_about_weather(location):
    wether_params = {
        'latitude': location[0],
        'longitude': location[1],
        'current_weather': True
    }

    # запитати і зберегти відповідь у змінну response
    response = requests.get('https://api.open-meteo.com/v1/forecast', params=wether_params)
    data = response.json() # зберігається json-відповідь

    tmperatura_citi = data['current_weather']['temperature']

    return tmperatura_citi


# обробник повідомлень
@bot.message_handler(commands=['start'])
def start_function(message):
    # reply_to відповісти на 
    markup = types.ReplyKeyboardMarkup()
    start = types.KeyboardButton("СТАРТ")
    stop = types.KeyboardButton("СТОП")
    markup.add(start, stop)
    bot.send_message(message.chat.id, text = "Привіт, {0.first_name}! Я бот що показує погоду, натисник на кнопку для старту".format(message.from_user), reply_markup=markup)
    #

@bot.callback_query_handler(lambda call: True)
def handle(call):
    bot.send_message(chat_id=call.message.chat.id, message_id=call.message.id, text='It works!')
bot.answer_callback_query(call.id)

# Обробник повідомлень яка відповідає на будь-яке повідомлення
@bot.message_handler(content_types=['text'])
def react_on_message(message):
    if message.text == "СТАРТ":
        bot.reply_to(message, "Напишіть місто на латині")
    if message.text == "СТОП":
        bot.reply_to(message, "Бувай")
        exit()
    
    town = message.text
    location = get_locaion_citi(town, message)
    temperatura_citi = get_info_about_weather(location)

    bot.reply_to(message, "Місце знаходження: " +str(location))
    bot.reply_to(message, "Температура в місті" + str(temperatura_citi))


    
    # if message.text == "повтори":
    #     bot.reply_to(message, message.text)

    # if message.text == "Привіт" or message.text == "привіт":
    #     text = input("Напишіть місто на латині")
    #     sent_msg = bot.send_message(message.chat.id, text, parse_mode='Markdown')
    #     bot.register_next_step_handler(sent_msg, weather(text))

    # if message.text == "Привіт" or message.text == "привіт":
    #     text = "Привіт як в тебе справи?"
    #     # бот, відправ повідомлення в цей чат з таким текстом і зчитай відповідь
    #     sent_msg = bot.send_message(message.chat.id, text, parse_mode='Markdown')
    #     # бот, зареєструй наступний крок
    #     bot.register_next_step_handler(sent_msg, mode_react)

    # if message.text == "Не хочу спілкуватися!" or message.text == "не хочу спілкуватися":
    #     text = "Чому?"
    #     sent_msg = bot.send_message(message.chat.id, text, parse_mode='Markdown')
    #     bot.register_next_step_handler(sent_msg, mode_react)

@bot.message_handler(content_types=['text'])
def mode_react(message):
    # на привіт
    if message.text == "нормально":
        bot.reply_to(message, "Це чудово, зараз буде добре!")
    if message.text == "добре":
        bot.reply_to(message, "Зараз буде ще краще!")
    if message.text == "погано":
        bot.reply_to(message, "Зараз, спробуємо виправити!")

    # на не хочу спіл
    if message.text == "бо":
        bot.reply_to(message, "Не хочеш говорити то й не потрібно!!")
    if message.text == "мені погано":
        bot.reply_to(message, "Повідомь батьків!")
    if message.text == "я розбив річ":
        bot.reply_to(message, "Я куплю тобі нову!")


bot.infinity_polling() # працювати завжди







