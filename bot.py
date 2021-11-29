import telebot
import random
from telebot import types
import time
import os
bot = telebot.TeleBot('2056524233:AAHByC9POMbG-JEQTXS8EGMVaPmsoAXk8ew')
APP_URL = 'https://herokubotpypy.herokuapp.com/'

@bot.message_handler(commands=['stop'])
def welcomme(message):
    bot.send_message(message.chat.id, 'Не уходи пожалусто !!!')
    bot.send_message(message.chat.id, '😢НУПОЖАЛУСТО😢')
@bot.message_handler(commands=['start'])
def welcome(message): 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("😊 Как дела?")
    markup.add(item1, item2)
    
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ {1.first_name}".format(message.from_user, bot.get_me()),
    reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(50,100)))
        if message.text == '😊 Как дела?':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            item3 = types.InlineKeyboardButton("нормально", callback_data='normal')
            markup.add(item1, item2, item3)
        
            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        if message.text == 'Как дела?':  
            time.sleep(2)
            cic = ['Просто вибухово як гарно', 'Погано мої друзі зїли все печиво', 'мені нормально']
            bot.send_message(message.chat.id, random.choice(cic))

        if message.text == 'Привет':  
            bot.send_message(message.chat.id, 'Привет')
            time.sleep(2)
            bot.send_message(message.chat.id, 'Хочеш узнать сколько мне лет ?')
        if message.text == 'Да':
            bot.send_message(message.chat.id, 'О а мне забила пойду надо вспомнить' )
            time.sleep(130)
            bot.send_message(message.chat.id, 'Вспомнила 12 или нет')

        if message.text == 'Нет':
            bot.send_message(message.chat.id, 'Ну ладно' )

        if message.text == 'да':
            bot.send_message(message.chat.id, 'О а мне забила пойду надо вспомнить' )
            time.sleep(130)
            bot.send_message(message.chat.id, 'Вспомнила 12 или нет')

        if message.text == 'нет':
            bot.send_message(message.chat.id, 'Ну ладно' )

    else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
        

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            if call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Буває 😢')
            if call.data == 'normal':
                bot.send_message(call.message.chat.id, 'Чому не вибухово ?')
 
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                reply_markup=None)
 
     
         
    except Exception as e:
        print(repr(e))




bot.polling(none_stop=True)