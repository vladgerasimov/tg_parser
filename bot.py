import dotenv
import telebot
import os
import sys

print(sys.executable)
dotenv.load_dotenv('.env')

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))


@bot.message_handler(commands=['start', 'help'])
def greet(message):
    bot.reply_to(message, "Hello mate! Just getting started")


@bot.message_handler(func=lambda message: 'nft' in message.text.lower())
def check_nft(message):
    bot.reply_to(message, 'I like nft!')


bot.infinity_polling()
