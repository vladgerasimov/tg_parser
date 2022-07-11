from dataclasses import dataclass


@dataclass
class Message:
    sender_nickname: str
    message_chat: str
    message_text: str
    media: str
    sender_id: int

    def __str__(self):
        tag = '@'
        if not self.sender_nickname:
            self.sender_nickname = 'unknown'
            tag = ''

        return (f'{self.message_text}\n\n'
                f'by {tag}{self.make_bold(self.sender_nickname)}'
                # f'{self.make_user_id_link(self.sender_id, self.sender_nickname)}'
                )

    @staticmethod
    def make_bold(text: str):
        return '<b>' + text + '</b>'

    @staticmethod
    def make_italic(text: str):
        return '<i>' + text + '</i>'

    # @staticmethod
    # def make_user_id_link(sender_id: int, user_name: str):
    #     return f'<a href="tg://user?id={sender_id}">{user_name}</a>'
