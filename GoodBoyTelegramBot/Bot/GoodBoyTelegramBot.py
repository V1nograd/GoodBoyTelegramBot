import telebot
import random
import time

#import mysql.connector


bot = telebot.TeleBot('you token')

#Create Connection
#Start by creating a connection to the database.
#Use the username and password from your MySQL database:

#mydb = mysql.connector.connect(
#  host="localhost",
#  user="yourusername",
#  password="yourpassword"
#)

#print(mydb)


#Обработчик собитий когда 

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Я лох. Приятно познакомиться, {message.from_user.first_name}, список команд в /help')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, f' Сорян {message.from_user.first_name} я еще в бета версии, команды: /start /help /go /incident /kolya')

@bot.message_handler(commands=['go'])
def send_welcome(message):
    bot.send_message(message.chat.id, f'Ты пидор!')

@bot.message_handler(commands=['incident'])
def handle_text(message):
         random.seed()
         chooise = random.randint(1, 6)

         
         bot.send_message(message.chat.id, f'Гадаем на бинарных аукционах :)')
         time.sleep(1)
         bot.send_message(message.chat.id, f'Выдаем ответ из сервера :)')
         time.sleep(1)
         bot.send_message(message.chat.id, f'Ну что кусок мяса ты сегодня работаешь:')
         time.sleep(1)
         if(chooise == 6):
             bot.send_message(message.chat.id, f'Андрей')
         elif(chooise == 5):
             bot.send_message(message.chat.id, f'Оксана')
         elif(chooise == 4):
             bot.send_message(message.chat.id, f'Оксана')
         elif(chooise == 3):
             bot.send_message(message.chat.id, f'Леха')
         elif(chooise == 2):
             bot.send_message(message.chat.id, f'Стас')
         elif(chooise == 1):
             bot.send_message(message.chat.id, f'Жека')
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
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, в жопу иди.')

print("Bot work!")
# бот работает пока работает программа 
bot.polling(none_stop=True)