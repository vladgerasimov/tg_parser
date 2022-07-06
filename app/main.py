from telethon import TelegramClient, events
import logging
import dotenv
import os
from receiver_conf import ReceiverBotConfig
from sender_bot import SenderBotConfig
from pathlib import Path
from message import Message
from threading import Thread

images_path = Path(__file__) / 'images'

logger = logging.getLogger('Receiver')
dotenv.load_dotenv(Path(__file__).parent.joinpath('.env'))
receiver_bot = TelegramClient('nft_parser', int(os.getenv('API_ID')), os.getenv('API_HASH'))

receiver_config = ReceiverBotConfig()

sender_config = SenderBotConfig()
sender_bot = sender_config.get_bot_instance()


def get_media_paths(media_path):
    if not media_path:
        return None
    name = media_path.split(' ')[0].rstrip('.jpg')
    return [img for img in images_path.iterdir() if str(img).startswith(name)]


def send_message(parsed_message: Message):
    # TODO: update channels to share parsed message
    if parsed_message.media:
        with open(parsed_message.media, 'rb') as file:
            sender_bot.send_photo(chat_id='-1001753902997',
                                  photo=file,
                                  caption=str(parsed_message),
                                  parse_mode='HTML')
    else:
        sender_bot.send_message(chat_id='-1001753902997',
                                text=str(parsed_message),
                                parse_mode='HTML')


@receiver_bot.on(events.NewMessage(chats=receiver_config.chats_to_monitor))
async def handle_nft(event):
    # TODO: sometimes sender_name is None
    message_chat = event.chat.username # if event.chat.username else await event.get_sender().username
    message_text = event.message.message
    sender = await event.message.get_sender()
    if event.sender.username:
        sender_name = event.sender.username
    elif sender.username:
        sender_name = sender.username
    else:
        sender_name = sender.first_name

    if not message_text:
        return
    media_path = await receiver_bot.download_media(event.message.media, str(images_path))

    # media_path = get_media_paths(media_path)

    message = Message(
        sender_nickname=sender_name,
        message_chat=message_chat,
        message_text=message_text,
        media=media_path
    )

    print('Message parsed')

    send_message(message)

    if media_path:
        Path(media_path).unlink(missing_ok=True)


@sender_bot.message_handler(func=lambda message: 'nft' in message.text.lower())
def check_nft(message):
    sender_bot.reply_to(message, 'I like nft!')


@sender_bot.message_handler(func=sender_config.validate_sender)
def test(message):
    sender_bot.reply_to(message, 'user is valid')


Thread(target=sender_bot.infinity_polling).start()

receiver_bot.start()
receiver_bot.run_until_disconnected()
