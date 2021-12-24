import telebot
from telebot import types

token = '2128043749:AAH5r9m23eTiMcgT5LdzEPmbF3qScPXsrEU'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row('Хочу', '/DEP', '/ADR')
    keyboard.row('/help', '/LMS')

    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую инфорацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def helping(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row('Хочу', '/DEP', '/ADR')
    keyboard.row('/help', '/LMS')

    bot.send_message(message.chat.id, 'Нажми на кнопки, получи информацию, которая тебя интересует', reply_markup=keyboard)


@bot.message_handler(commands=['LMS'])
def start_message(message):
    bot.send_message(message.chat.id, 'LMS — https://lms.mtuci.ru/lms/login/index.php')


@bot.message_handler(commands=['DEP'])
def dep(message):
    bot.send_message(message.chat.id, 'Все факультеты МТУСИ — https://mtuci.ru/')


@bot.message_handler(commands=['ADR'])
def address(message):
    bot.send_message(message.chat.id, 'Все факультеты МТУСИ — https://yandex.ru/maps/-/CCUuVJccgC')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда — https://mtuci.ru/')


bot.infinity_polling()
