import telebot
from telebot import types
import random
import time
from config import token

bot = telebot.TeleBot(token)

#Обработчик собитий когда 

def keyboard():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	btn1 = types.KeyboardButton('✌ Привет ✌')
	markup.add(btn1)
	return markup  

# NOT WORKING YET BUT IM IN THE CREATING PROCESS 
#def keyincident():
#	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
#	btn2 = types.KeyboardButton('🎰 Крути барабан 🎲')
#	markup.add(btn2)
#	return markup  

reply_markup=keyboard()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f'''Приветствую {message.from_user.first_name} 👋''', reply_markup=keyboard())


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, f' Сорян {message.from_user.first_name} я еще в бета версии, команды: /start /help /go /incident /kolya')

@bot.message_handler(commands=['go'])
def send_welcome(message):
    bot.send_message(message.chat.id, f'Ты пидор! ✅')

@bot.message_handler(commands=['incident'])
def handle_text(message):
         random.seed()
         chooise = random.randint(1, 6)

         
         bot.send_message(message.chat.id, f'Начинаем проведения оперативно-розыскных действий 👮')
         time.sleep(1)
         bot.send_message(message.chat.id, f'Сбор улик 🔍')
         time.sleep(1)
         bot.send_message(message.chat.id, f'Опрос свидетелей 🐀')
         time.sleep(1)
         bot.send_message(message.chat.id, f'Ну что кусок мяса ты сегодня работаешь 💻')
         time.sleep(1)
         if(chooise == 6):
             bot.send_message(message.chat.id, f'✌ Андрей ✌')
         elif(chooise == 5):
             bot.send_message(message.chat.id, f'💃 Оксана 💃')
         elif(chooise == 4):
             bot.send_message(message.chat.id, f'💂 Юра 💂')
         elif(chooise == 3):
             bot.send_message(message.chat.id, f'😡 Леха 😡')
         elif(chooise == 2):
             bot.send_message(message.chat.id, f'👼 Стас 👼')
         elif(chooise == 1):
             bot.send_message(message.chat.id, f'🏅 Жека 🏅')
         else:
             bot.send_message(message.chat.id, f'Братанчик что-то пошло не так обратись к @Qwerty87230')
         #bot.send_message(message.chat.id, f'random: {chooise}' )
         print(chooise)


@bot.message_handler(commands=['kolya'])
def send_welcome(message):
    bot.reply_to(message, f'Коля лох!')


# если бот получает в ответ привет идет вызов обработчика событий  

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '✌ Привет ✌':
        bot.send_message(message.from_user.id, 'Йоу! Если нужна помощь нажми: /help ☺')
    elif message.text == '🎰 Крути барабан 🎲':
        bot.send_message(message.from_user.id, 'Выбераем жертву 🐀', commands=['incident'])
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, в жопу иди.')

print("Bot work!")
# бот работает пока работает программа 
bot.polling(none_stop=True)