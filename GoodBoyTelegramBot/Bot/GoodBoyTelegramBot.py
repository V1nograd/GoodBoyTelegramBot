import telebot
from telebot import types
import random
import time
import sqlite3
import command
from config import token
bot = telebot.TeleBot(token)

def main():

    @bot.message_handler(commands=['onkeyboard'])
    def keyBoardButton(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard=True)
        first_button_key = types.KeyboardButton(text = "✌ Привет ✌")
        second_button_key = types.KeyboardButton(text = "🎰 Крути барабан 🎲")
        third_button_key = types.KeyboardButton(text = "Close")
        markup.row(first_button_key)
        markup.row(second_button_key)
        markup.row(third_button_key)
        bot.send_message(message, 'Нажми на кнопку' , reply_markup = markup)
    

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
        bot.send_message(message.chat.id, f'Ты ыыыыыыыыыыы! ✅')

    @bot.message_handler(commands=['db'])
    def send_for_Stas(message):
        bot.reply_to(message, f'работать {message.from_user.username} !')

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
            bot.send_message(message, f'Йоу! {message.from_user.username} Если нужна помощь нажми: /help ☺') #message.from_user.username вывод имени пользователя в чате
        elif message.text == "🎰 Крути барабан 🎲":
            chooise_incident(message)
        elif message.text == "hei": 
            bot.send_message(message.chat.id, f'Yamete kudasai {message.from_user.username}!')

#@bot.callback_query_handler(func=lambda call: True)
#def callback_worker(call):
#    if call.data == "first":
#        bot.send_message(call.message.chat.id, f'Йоу! {message.from_user.username} Если нужна помощь нажми: /help ☺') #message.from_user.username вывод имени пользователя в чате
#    elif call.data == "second": 
#        bot.send_message(message.chat.id, f'hello')
#        print("test")
#    elif call.data == "third":
#        bot.send_message(message.chat.id, f'hello 3')


print("Bot work!")
# бот работает пока работает программа
if __name__ == '__main__':
    main()
    bot.polling(none_stop=True)
