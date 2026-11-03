"""Список задач с методом отображения текущих данных."""
import tkinter as tk


class AppListbox(tk.Listbox):
    def __init__(self, master):
        super().__init__(
            master, font=('Arial', 11), bg='#303030', fg='white',
            selectbackground='#555555', height=12
        )

    def show_tasks(self, tasks):
        self.delete(0, tk.END)
        for task in tasks:
            self.insert(tk.END, task)
