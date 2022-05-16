from pymongo import MongoClient


class MongoDB:
    def __init__(self, host='localhost', port=27017):
        self._client = MongoClient(host, port)
        self.db = self._client['nft_parser']
        # self._chats_to_monitor = self.db['_chats_to_monitor']
        # self._users_blacklist = self.db['_users_blacklist']

    def get_data(self, collection: str, **kwargs):
        return self.db[collection].find(kwargs)

    def save_data(self, collection: str, data):
        return self.db[collection].insert_one(data)

    def get_distinct_values(self, collection, key):
        return self.get_data(collection).distinct(key)


if __name__ == '__main__':
    client = MongoDB()
