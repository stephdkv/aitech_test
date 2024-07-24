from .base import BaseRepository
from models import User

class MemoryRepository(BaseRepository):
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def create_user(self, name):
        user = User(self.next_id, name)
        self.users[self.next_id] = user
        self.next_id += 1
        return user

    def get_user(self, user_id):
        return self.users.get(user_id)

    def update_user(self, user_id, name):
        user = self.get_user(user_id)
        if user:
            user.name = name
            self.users[user_id] = user
            return user
        return None

    def delete_user(self, user_id):
        return self.users.pop(user_id, None) is not None
