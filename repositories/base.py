from abc import ABC, abstractmethod

class BaseRepository(ABC):
    @abstractmethod
    def create_user(self, name):
        pass

    @abstractmethod
    def get_user(self, user_id):
        pass

    @abstractmethod
    def update_user(self, user_id, name):
        pass

    @abstractmethod
    def delete_user(self, user_id):
        pass
