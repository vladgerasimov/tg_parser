import json
import dotenv
import telebot
import os
import sys
from pathlib import Path
directory = Path(__file__).parent


dotenv.load_dotenv(directory / '.env')

# sender_bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))


class SenderBotConfig:
    def __init__(self):
        self.allowed_senders = self.get_allowed_senders()
        self.bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))

    def validate_sender(self, message: telebot.types.Message) -> bool:
        user_nickname = message.from_user.username
        return user_nickname in self.allowed_senders

    @staticmethod
    def get_allowed_senders() -> set:
        with open(directory / 'allowed_senders.json') as file:
            allowed_users = json.load(file)
        return set(allowed_users)

    def add_allowed_sender(self, user: str) -> None:
        """
        Updates JSON file and self.allowed_senders field
        :param user:
        :return: None
        """
        allowed_senders = self.get_allowed_senders()
        allowed_senders.add(user)
        with open(directory / 'allowed_senders.json', 'w') as file:
            json.dump(list(allowed_senders), file)

        self.allowed_senders = allowed_senders

    def drop_allowed_sender(self, user: str) -> None:
        """
        Updates JSON file and self.allowed_senders field
        :param user:
        :return: None
        """
        allowed_senders = self.get_allowed_senders()
        allowed_senders.remove(user)
        with open(directory / 'allowed_senders.json', 'w') as file:
            json.dump(list(allowed_senders), file)

        self.allowed_senders = allowed_senders

    def get_bot_instance(self):
        return self.bot


if __name__ == '__main__':
    sender_bot_config = SenderBotConfig()
    sender_bot = sender_bot_config.get_bot_instance()


    @sender_bot.message_handler(func=lambda message: 'nft' in message.text.lower())
    def check_nft(message):
        sender_bot.reply_to(message, 'I like nft!')


    @sender_bot.message_handler(func=sender_bot_config.validate_sender)
    def test(message):
        sender_bot.reply_to(message, 'user is valid')


    sender_bot.infinity_polling()