from telethon import TelegramClient, events
import dotenv
import os
from mongo import MongoDB
import asyncio

dotenv.load_dotenv('.env')
receiver_bot = TelegramClient('nft_parser', int(os.getenv('API_ID')), os.getenv('API_HASH'))
sender_bot = TelegramClient('nft_sender', int(os.getenv('API_ID')), os.getenv('API_HASH'))
client = MongoDB()


@receiver_bot.on(events.NewMessage(chats=client.get_distinct_values('chats_to_monitor', 'chat')))
async def handle_nft(event):
    sender_name = event.sender.username
    message_chat = event.chat.username if event.chat.username else await event.get_sender().username
    message_info = event.message.to_dict()
    text_message = message_info['message']
    data = {
        'chat': message_chat,
        'sender': sender_name,
        'message': text_message,
    }
    client.save_data('messages', data)
    print('Message parsed')
    # await receiver_bot.send_message('etokarinakarina', ev)


receiver_bot.start()

sender_bot.start(bot_token=os.getenv('BOT_TOKEN'))
receiver_bot.run_until_disconnected()


# asyncio.run(main())