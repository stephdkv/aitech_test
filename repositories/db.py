from .base import BaseRepository
from models import User
import sqlite3

class DBRepository(BaseRepository):
    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL
                )
            ''')

    def create_user(self, name):
        with self.conn:
            cursor = self.conn.execute('INSERT INTO users (name) VALUES (?)', (name,))
        return User(cursor.lastrowid, name)

    def get_user(self, user_id):
        cursor = self.conn.execute('SELECT id, name FROM users WHERE id = ?', (user_id,))
        row = cursor.fetchone()
        if row:
            return User(*row)
        return None

    def update_user(self, user_id, name):
        with self.conn:
            cursor = self.conn.execute('UPDATE users SET name = ? WHERE id = ?', (name, user_id))
            if cursor.rowcount == 0:
                return None
        return self.get_user(user_id)

    def delete_user(self, user_id):
        with self.conn:
            cursor = self.conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
            return cursor.rowcount > 0
