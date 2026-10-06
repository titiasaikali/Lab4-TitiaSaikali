"""Tkinter task manager; run with python src/tkinter_ui.py."""
import tkinter as tk
from tkinter import ttk, messagebox
from backend import TaskStore


class TaskWindow:
    def __init__(self, root, store):
        self.root, self.store = root, store
        root.title('Lab 4 | Titia Saikali | Tkinter')
        root.geometry('640x420')
        frame = ttk.Frame(root, padding=20)
        frame.pack(fill='both', expand=True)
        ttk.Label(frame, text='Task Manager — Tkinter', font=('Arial', 18)).pack(anchor='w')
        self.entry = ttk.Entry(frame)
        self.entry.pack(fill='x', pady=12)
        self.entry.bind('<Return>', lambda event: self.add())
        self.tree = ttk.Treeview(frame, columns=('title', 'status'), show='headings', selectmode='browse')
        self.tree.heading('title', text='Task')
        self.tree.heading('status', text='Status')
        self.tree.column('title', width=400)
        self.tree.column('status', width=100)
        self.tree.pack(fill='both', expand=True)
        buttons = ttk.Frame(frame)
        buttons.pack(fill='x', pady=12)
        for label, action in [('Add task', self.add), ('Toggle done', lambda: self.change('toggle')), ('Delete', lambda: self.change('delete')), ('Refresh', self.refresh)]:
            ttk.Button(buttons, text=label, command=action).pack(side='left', padx=3)
        self.refresh()

    def refresh(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for task_id, title, done in self.store.list_tasks():
            self.tree.insert('', 'end', iid=str(task_id), values=(title, 'Done' if done else 'Pending'))

    def add(self):
        try:
            self.store.add(self.entry.get())
        except ValueError as error:
            messagebox.showwarning('Task title', str(error))
            return
        self.entry.delete(0, 'end')
        self.refresh()

    def change(self, action):
        selection = self.tree.selection()
        if selection:
            getattr(self.store, action)(int(selection[0]))
            self.refresh()


if __name__ == '__main__':
    store = TaskStore()
    root = tk.Tk()
    TaskWindow(root, store)
    try:
        root.mainloop()
    finally:
        store.close()
