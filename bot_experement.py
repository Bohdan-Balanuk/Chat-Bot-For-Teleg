# Ключ для доступу і керування ботом
BOT_TOKEN = '6055763111:AAFMbPP0-q3w_dA4E-xwf8H2W7hnwYrA3VI'

import telebot 
from telebot import types # для указание типов
import requests
import sys 

# Створюємо обект бот і даємо токен
bot = telebot.TeleBot(BOT_TOKEN)

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

citi = ''
retry = 0
# Обробник повідомлень яка відповідає на будь-яке повідомлення
@bot.message_handler(content_types=['text'])
def react_on_message(message):
    global citi, retry
    if message.text == "СТАРТ":
        bot.reply_to(message, "Напишіть місто на латині")
    elif message.text == "СТОП":
        bot.reply_to(message, "Бувай")        

    else:
        if message.text == "1":
            choose = 1
            retry = 1
        elif message.text == "2":
            choose = 2
            retry = 1
        elif message.text == "3":
            choose = 3
            retry = 1
        elif message.text == "4":
            choose = 4
            retry = 1
        elif message.text == "5":
            choose = 5
            retry = 1
        elif message.text == "6":
            choose = 6
            retry = 1
        elif message.text == "7":
            choose = 7
            retry = 1
        elif message.text == "8":
            choose = 8
            retry = 1
        elif message.text == "9":
            choose = 9
            retry = 1
        elif message.text == "10":
            choose = 10
            retry = 1

        else:           
            town = message.text
            citi = town
        
        location_perms = {
            'name': citi,
        }

        response = requests.get('https://geocoding-api.open-meteo.com/v1/search', params=location_perms)
        data = response.json()
        i = 0

        if retry == 0:
            for i in range(len(data['results'])):
                bot.send_message(message.chat.id, data['results'][i]['name'] + ' - ' + str(i+1))

            bot.send_message(message.chat.id, 'Виберіть місто, яке вам потрібне, з цих перерахованих')#, reply_markup = markup)

        location_citit = [
                data['results'][int(choose)-1]['latitude'],
                data['results'][int(choose)-1]['longitude']
            ]

        temperatura_citi = get_info_about_weather(location_citit)

        bot.reply_to(message, "Місце знаходження: " +str(location_citit))
        bot.reply_to(message, "Температура в місті" + str(temperatura_citi))


bot.infinity_polling() # працювати завжди
