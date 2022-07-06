from dataclasses import dataclass


@dataclass
class Message:
    sender_nickname: str
    message_chat: str
    message_text: str
    media: str

    def __str__(self):
        if not self.sender_nickname:
            self.sender_nickname = ''

        return (f'From @{self.make_italic(self.message_chat)}\n\n'
                f'{self.message_text}\n\n'
                f'by @{self.make_bold(self.sender_nickname)}'
                )

    @staticmethod
    def make_bold(text: str):
        return '<b>' + text + '</b>'

    @staticmethod
    def make_italic(text):
        return '<i>' + text + '</i>'
