import dotenv
import telebot
import os
import sys

print(sys.executable)
dotenv.load_dotenv('.env')

sender_bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))


@sender_bot.message_handler(commands=['start', 'help'])
def greet(message):
    sender_bot.reply_to(message, "Hello mate! Just getting started")


@sender_bot.message_handler(func=lambda message: 'nft' in message.text.lower())
def check_nft(message):
    sender_bot.reply_to(message, 'I like nft!')


sender_bot.infinity_polling()
