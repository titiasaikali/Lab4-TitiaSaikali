"""PyQt6 task manager using the same database as Tkinter."""
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QListWidget, QListWidgetItem, QPushButton, QMessageBox
from backend import TaskStore


class TaskWindow(QWidget):
    def __init__(self, store):
        super().__init__()
        self.store = store
        self.setWindowTitle('Lab 4 | Titia Saikali | PyQt')
        self.resize(640, 420)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel('Task Manager — PyQt'))
        self.entry = QLineEdit()
        self.entry.setPlaceholderText('Enter a task title')
        self.entry.returnPressed.connect(self.add)
        layout.addWidget(self.entry)
        self.tasks = QListWidget()
        layout.addWidget(self.tasks)
        buttons = QHBoxLayout()
        layout.addLayout(buttons)
        for label, action in [('Add task', self.add), ('Toggle done', lambda: self.change('toggle')), ('Delete', lambda: self.change('delete')), ('Refresh', self.refresh)]:
            button = QPushButton(label)
            button.clicked.connect(action)
            buttons.addWidget(button)
        self.refresh()

    def refresh(self):
        self.tasks.clear()
        for task_id, title, done in self.store.list_tasks():
            item = QListWidgetItem(f"{'[Done]' if done else '[Pending]'} {title}")
            item.setData(Qt.ItemDataRole.UserRole, task_id)
            self.tasks.addItem(item)

    def add(self):
        try:
            self.store.add(self.entry.text())
        except ValueError as error:
            QMessageBox.warning(self, 'Task title', str(error))
            return
        self.entry.clear()
        self.refresh()

    def change(self, action):
        item = self.tasks.currentItem()
        if item is not None:
            getattr(self.store, action)(item.data(Qt.ItemDataRole.UserRole))
            self.refresh()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    store = TaskStore()
    window = TaskWindow(store)
    window.show()
    try:
        sys.exit(app.exec())
    finally:
        store.close()
