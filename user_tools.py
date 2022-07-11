import pickle


def load_chats() -> set:
    with open('chats.pkl', 'rb') as file:
        chats = pickle.load(file)
    return set(chats)


def save_chats(chats) -> None:
    with open('chats.pkl', 'wb') as file:
        pickle.dump(chats, file)


def add_chat(chat) -> None:
    chats = load_chats()
    chats.add(chat)
    save_chats(chats)


def remove_chat(chat) -> None:
    chats = load_chats()
    chats.remove(chat)
    save_chats(chats)


if __name__ == '__main__':
    test = load_chats()
    print(test)
