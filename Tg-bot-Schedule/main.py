import telebot
from telebot import types
import psycopg2
import datetime

token = "2128043749:AAH5r9m23eTiMcgT5LdzEPmbF3qScPXsrEU"
bot = telebot.TeleBot(token)

conn = psycopg2.connect(database="timetable", user="postgres", password="root")
cursor = conn.cursor()

COMMANDS = ['/week', '/mtuci']


def top_or_bottom():
    now_week = datetime.date.today().isocalendar().week
    if now_week % 2 == 0:
        return 'bottom'
    if now_week % 2 == 1:
        return 'top'


def next_week(eo):
    if eo == 'bottom':
        eo = 'top'
    elif eo == 'top':
        eo = 'bottom'

    return eo


def send_week(eo):
  try:
        msg = []
        cursor.execute(
            "SELECT day, subject, room_numb, start_time FROM timetable.timetable WHERE week='{}' OR week='both'".format(
                eo))
        timetable = list(cursor.fetchall())
        in_one_day = {}
        for timetable_day in timetable:
            if timetable_day[0] not in in_one_day.keys():
                in_one_day[timetable_day[0]] = [timetable_day[1:]]
                continue
            in_one_day[timetable_day[0]] = *in_one_day[timetable_day[0]], timetable_day[1:]
        for day in in_one_day.keys():
            msg.append('\n' + day + '\n')
            msg.append('____________\n')
            for _ in in_one_day[day]:
                msg.append(str(_).replace('(', '').replace(')', '').replace("'", ''))
                msg.append('\n')
        msg.append('____________\n')

        msg = ''.join(msg)
        return msg
  except:
      return 'Пар нет'


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("ПН", "ВТ", "СР", "ЧТ", "ПТ")
    keyboard.add("Расписание на текущую неделю")
    keyboard.add("Расписание на следущую неделю")
    bot.send_message(message.chat.id, 'На какой день интересует рассписание?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Команды:\n'
                                      "/week -- Какая сейчас неделя? \n"
                                      "/mtuci -- Сайт вуза \n")


@bot.message_handler(commands=['mtuci'])
def mtuci_news(message):
    bot.send_message(message.chat.id, 'Вам сюда – https://mtuci.ru/')

@bot.message_handler(commands=['week'])
def which_week(message):
    if top_or_bottom() == "top":
        bot.send_message(message.chat.id, 'верхняя')
    elif top_or_bottom() == "bottom":
        bot.send_message(message.chat.id, 'нижняя')


@bot.message_handler(content_types=['text'])
def text(message):
    global COMMANDS
    DAYS = {'ПН': 'Понедельник', 'ВТ': 'Вторник', 'СР': 'Среда', 'ЧТ': 'Четверг', 'ПТ': 'Пятница'}
    if message.text == 'Расписание на текущую неделю':
        bot.send_message(message.chat.id, send_week(top_or_bottom()))
    elif message.text == 'Расписание на следущую неделю':
        bot.send_message(message.chat.id, send_week(next_week(top_or_bottom())))
    elif message.text in DAYS.keys():
            msg='Пар нет'
            try:
                cursor.execute(
                    "SELECT subject, room_numb, start_time FROM timetable.timetable"
                    " WHERE day='{}' AND (week='{}' OR week='both') ".format(
                        DAYS[message.text], top_or_bottom()))
                timetable = list(cursor.fetchall())
                msg = ''
                for _ in timetable:
                    _ = [str(i) for i in _]
                    msg += ', '.join(_) + '\n'
                bot.send_message(message.chat.id, msg)
            except:
                bot.send_message(message.chat.id, 'Пар нет')

    elif message.text:
        bot.send_message(message.chat.id, "Извините, я Вас не понял")


bot.polling()