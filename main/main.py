import telebot
from decouple import config
import requests


API_KEY = config("API_KEY")
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"Hi! \n welcome to my bot , this is a simple bot about generate a fake person doesn't exist fast for you\n /generate : click to the command and type generate fake face.")




bot.infinity_polling()