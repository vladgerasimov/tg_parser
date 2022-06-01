import json
from pathlib import Path


class ReceiverBotConfig:
    chats_to_monitor = None

    def __init__(self):
        self.chats_path = Path(__file__).parent.joinpath('chats_to_monitor.json')
        self.load_chats_to_monitor()

    def load_chats_to_monitor(self):
        with open(self.chats_path) as file:
            self.chats_to_monitor = json.load(file)

