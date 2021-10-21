import telebot
from telebot import types
import random
import time
from config import token

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['onkeyboard'])
def keyBoardButton(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard=True)
    itembutton1 = types.KeyboardButton("✌ Привет ✌")
    itembutton2 = types.KeyboardButton("🎰 Крути барабан 🎲")
    itembutton3 = types.KeyboardButton("Close")
    markup.row(itembutton1)
    markup.row(itembutton2)
    markup.row(itembutton3)
    bot.send_message(message.chat.id, reply_markup = markup)
    


#Обработчик собитий когда

@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    user_name = message.new_chat_members[0].first_name
    random.seed()
    chooise = random.randint(0, 1)
    print("new_chat_members random", chooise)
    if(chooise == 0):
        bot.send_message(message.chat.id, f"Добро пожаловать кусок мяса, {user_name}! 👋")
    elif(chooise == 1):
        bot.send_message(message.chat.id, f"Привет, {user_name}! 👋")

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, f'''Приветствую {message.from_user.first_name} 👋''')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, f' Йоу {message.from_user.first_name} уже лучше но я еще в бета версии, команды: \n /start \n /help \n /onkeyboard \n /db \n /go \n')

@bot.message_handler(commands=['go'])
def send_go(message):
    bot.send_message(message.chat.id, f'Ты пидор! ✅')

@bot.message_handler(commands=['db'])
def send_welcome(message):
    bot.reply_to(message, f'Пиздуй работать {message.from_user.username} !')

@bot.message_handler(commands=['incident'])
def chooise_incident(message):
         random.seed()
         chooise = random.randint(1, 7)

         bot.send_message(message.chat.id, f'Начинаем проведения оперативно-розыскных действий 👮')
         time.sleep(1)
         bot.send_message(message.chat.id, f'Сбор улик 🔍')
         time.sleep(1)
         bot.send_message(message.chat.id, f'Опрос свидетелей 🐀')
         time.sleep(1)
         bot.send_message(message.chat.id, f'Ну что кусок мяса ты сегодня работаешь 💻')
         time.sleep(1)
         if(chooise == 7):
             bot.send_message(message.chat.id, f'✌  Димон ✌')
         elif(chooise == 6):
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
             bot.send_message(message.chat.id, f'Братанчик что-то пошло не так обратись к @Alx326')
         print(chooise)

# если бот получает в ответ привет идет вызов обработчика событий

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "✌ Привет ✌":
        bot.reply_to(message, f'Йоу! {message.from_user.username} Если нужна помощь нажми: /help ☺') #message.from_user.username вывод имени пользователя в чате
    elif message.text == "🎰 Крути барабан 🎲":
        bot.send_message(message.chat.id, '/incident')
        bot.message_handler(commands=['incident'])
    else:
        bot.send_message(message.from_user.id, f'{message.from_user.username} что ты там говорил про чик чирик?')

print("Bot work!")
# бот работает пока работает программа
if __name__ == '__main__':
    bot.polling(none_stop=True)
