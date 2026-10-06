"""Shared persistent task storage for both user interfaces."""
import sqlite3
from pathlib import Path

DEFAULT_DB = Path(__file__).resolve().parents[1] / 'data' / 'tasks.sqlite3'


class TaskStore:
    def __init__(self, path=DEFAULT_DB):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(path)
        self.db.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT NOT NULL, done INTEGER NOT NULL DEFAULT 0)')
        self.db.commit()

    def list_tasks(self):
        return self.db.execute('SELECT id, title, done FROM tasks ORDER BY id').fetchall()

    def add(self, title):
        title = title.strip()
        if not title:
            raise ValueError('Enter a task title.')
        with self.db:
            cursor = self.db.execute('INSERT INTO tasks(title) VALUES (?)', (title,))
        return cursor.lastrowid

    def toggle(self, task_id):
        with self.db:
            self.db.execute('UPDATE tasks SET done = 1 - done WHERE id = ?', (task_id,))

    def delete(self, task_id):
        with self.db:
            self.db.execute('DELETE FROM tasks WHERE id = ?', (task_id,))

    def close(self):
        self.db.close()
