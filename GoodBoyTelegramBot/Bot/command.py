import telebot
from GoodBoyTelegramBot import bot

print("call test command")
@bot.message_handler(commands=['text'])
def send_test(message):
    bot.send_message(message, f'''testtesttesttest 👋''')
    print("call test command")

