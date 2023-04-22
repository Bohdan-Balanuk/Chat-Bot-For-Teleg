# Ключ для доступу і керування ботом
BOT_TOKEN = '6055763111:AAFMbPP0-q3w_dA4E-xwf8H2W7hnwYrA3VI'

import telebot 
 
# Створюємо обект бот і даємо токен
bot = telebot.TeleBot(BOT_TOKEN)

# обробник повідомлень
@bot.message_handler(commands=['start'])
def start_function(message):
    # reply_to відповісти на 
    bot.reply_to(message, "Привіт я бот який показує погоду в певному місті")

# Обробник повідомлень яка відповідає на будь-яке повідомлення
@bot.message_handler(content_types=['text'])
def react_on_message(message):
    if message.text == "повтори":
        bot.reply_to(message, message.text)

    if message.text == "Привіт" or message.text == "привіт":
        text = "Привіт як в тебе справи?"
        # бот, відправ повідомлення в цей чат з таким текстом і зчитай відповідь
        sent_msg = bot.send_message(message.chat.id, text, parse_mode='Markdown')
        # бот, зареєструй наступний крок
        bot.register_next_step_handler(sent_msg, mode_react)

    if message.text == "Не хочу спілкуватися!" or message.text == "не хочу спілкуватися":
        text = "Чому?"
        sent_msg = bot.send_message(message.chat.id, text, parse_mode='Markdown')
        bot.register_next_step_handler(sent_msg, mode_react)

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