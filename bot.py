"""Simple bot implementation"""
import telebot
import os
from dotenv import load_dotenv

load_dotenv('.env')
bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Sends a greeting to user"""
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """Answers the message"""
    bot.reply_to(message, message.text)


bot.infinity_polling()
