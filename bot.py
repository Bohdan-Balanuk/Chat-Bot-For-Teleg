# Ключ для доступу і керування ботом
BOT_TOKEN = '6055763111:AAFMbPP0-q3w_dA4E-xwf8H2W7hnwYrA3VI'

import telebot 
from telebot import types # для указание типов
import requests
 
# Створюємо обект бот і даємо токен
bot = telebot.TeleBot(BOT_TOKEN)

weather = []

@bot.message_handler(commands=['start'])
def start_function(message):
    bot.reply_to(message, "Привіт, я Бот який показую місце та температуру любого міста!")
    bot.send_message(message.chat.id, text = "Для того, щоб почати натисни на команду: /weather")

@bot.message_handler(commands=['weather'])
def ping(message):
    # приймаєш відповідь
    answer = bot.send_message(message.chat.id, text = "Напиши назву міста, яке тебе цікавить.")
    # після того, як користувач щось відповів - запускається функція choose_city і передається їх месседж який написав користувач
    bot.register_next_step_handler(answer, choose_city)
    
    # відправити в чат, звідки прийшло повідомлення месседж "pong"
    

@bot.message_handler(content_types=['text'])
def choose_city(message):
    global weather
    citi = message.text

    location_perms = {
            'name': citi,
        }
    
    request_settings = {
        'latitude': 50.45,
        'longitude': 30.52,
        'current_weather': True
    }
    weather = requests.get('https://geocoding-api.open-meteo.com/v1/search', params=location_perms).json()
    
    
    for i in range(len(weather['results'])):
            bot.send_message(message.chat.id, weather['results'][i]['name'] + ' - ' + str(i+1))

    answer = bot.send_message(message.chat.id, 'Виберіть місто, яке вам потрібне, з цих перерахованих')


    bot.register_next_step_handler(answer, lookfor_where)

def lookfor_where(message):
    global weather
    choose = message.text

    location_citi = [
        weather['results'][int(choose)-1]['latitude'],
        weather['results'][int(choose)-1]['longitude']
    ]

    wether_params = {
         'latitude': location_citi[0],
         'longitude': location_citi[1],
         'current_weather': True
     }
    
    response = requests.get('https://api.open-meteo.com/v1/forecast', params=wether_params).json()
    temperatura_citi = response['current_weather']['temperature']

    bot.send_message(message.chat.id, "Місце знаходження: " +str(location_citi))
    bot.send_message(message.chat.id, "Температура в місті: " + str(temperatura_citi))

# def get_info_about_weather(location):
#     location_perms = {
#             'name': citi,
#         }
#     wether_params = {
#         'latitude': location[0],
#         'longitude': location[1],
#         'current_weather': True
#     }

#     # запитати і зберегти відповідь у змінну response
#     response = requests.get('https://api.open-meteo.com/v1/forecast', params=wether_params)
#     data = response.json() # зберігається json-відповідь

#     tmperatura_citi = data['current_weather']['temperature']

#     return tmperatura_citi



bot.infinity_polling() # працювати завжди







