import telebot
import database as db
import config
from telebot import types
import logging
import time
from threading import Thread

bot = telebot.TeleBot(config.token)
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Меню 🍽️")
item2 = types.KeyboardButton("Расписание 🗓")
res = 0
markup.add(item1, item2)
@bot.message_handler(commands=['test'])
def pap(message):
    print('test')
@bot.message_handler(commands=['start', 'restart'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Я - <b>{1.first_name}</b>, бот созданный чтобы напоминать вам о расписании и меню в столовой".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)
@bot.message_handler(commands=['url'])
def send_url(message):
    bot.send_message(message.chat.id, 'https://docs.google.com/spreadsheets/d/' + config.spreadsheetId)

@bot.message_handler(content_types=['text'])
def lalala(message):
    global res
    if message.chat.type == 'private':
        if message.text == 'Меню 🍽️':
            bot.delete_message(message.chat.id, message.message_id)
            db.getfood(message)
            res += 1
            if res == 2:
                res = 0
                bot.send_message(message.chat.id, "Я ухожу", reply_markup=types.ReplyKeyboardRemove())
                time.sleep(10)
                bot.send_message(message.chat.id, "Я вернулся", reply_markup=markup)
            else:
                pass
        elif message.text == 'Расписание 🗓':
            bot.delete_message(message.chat.id, message.message_id)
            db.getplan(message)
            res += 1
            if res == 2:
                res = 0
                bot.send_message(message.chat.id, "Я ухожу", reply_markup=types.ReplyKeyboardRemove())
                time.sleep(10)
                bot.send_message(message.chat.id, "Я вернулся", reply_markup=markup)
            else:
                pass
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить')
    elif message.reply_to_message is not None: #если это в группе обращение боту
        if message.text == 'Меню 🍽️':
            bot.delete_message(message.chat.id, message.message_id)
            db.getfood(message)
            res += 1
            if res == 2:
                res = 0
                bot.send_message(message.chat.id, "Я ухожу", reply_markup=types.ReplyKeyboardRemove())
                time.sleep(10)
                bot.send_message(message.chat.id, "Я вернулся", reply_markup=markup)
            else:
                pass
        elif message.text == 'Расписание 🗓':
            bot.delete_message(message.chat.id, message.message_id)
            db.getplan(message)
            res += 1
            if res == 2:
                res = 0
                bot.send_message(message.chat.id, "Я ухожу", reply_markup=types.ReplyKeyboardRemove())
                time.sleep(10)
                bot.send_message(message.chat.id, "Я вернулся", reply_markup=markup)
            else:
                pass
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить')

bot.infinity_polling()
