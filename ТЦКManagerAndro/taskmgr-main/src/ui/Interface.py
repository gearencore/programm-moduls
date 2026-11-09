"""Главное окно графического менеджера задач."""
import tkinter as tk
from pathlib import Path
from tkinter import messagebox

from storage import load_tasks, save_tasks
from view import TaskView


class Interface:
    def __init__(self, windows_w=650, windows_h=630):
        self.root = tk.Tk()
        self.root.title('Task Manager')
        self.root.geometry(f'{windows_w}x{windows_h}')
        self.root.configure(bg='#202020')
        self.root.minsize(480, 480)

        self.tasks_file = Path(__file__).resolve().parents[1] / 'task.json'
        self.tasks = []
        self.view = TaskView(self.root, self.add_task, self.delete_task,
                             self.edit_task, self.clear_entry, self.select_task)
        self.entry = self.view.entry
        self.content = self.view.content
        self.task_list = self.view.task_list
        self.load_tasks()

    def load_tasks(self):
        try:
            self.tasks = load_tasks(self.tasks_file)
        except (OSError, ValueError) as error:
            messagebox.showerror('Ошибка загрузки', f'Не удалось прочитать задачи:\n{error}')
            self.tasks = []
        self.show_tasks()

    def save_tasks(self):
        try:
            save_tasks(self.tasks_file, self.tasks)
            return True
        except OSError as error:
            messagebox.showerror('Ошибка сохранения', f'Не удалось сохранить задачи:\n{error}')
            return False

    def show_tasks(self):
        self.view.show_tasks(self.tasks)

    def _get_fields(self):
        return self.entry.get().strip(), self.content.get('1.0', 'end-1c')

    def add_task(self, event=None):
        title, content = self._get_fields()
        if not title:
            messagebox.showwarning('Название задачи', 'Введите название задачи.')
            return
        self.tasks.append({'title': title, 'content': content})
        if self.save_tasks():
            self.show_tasks()
            self.clear_entry()
        else:
            self.tasks.pop()

    def select_task(self, event=None):
        selected = self.task_list.curselection()
        if not selected:
            return
        task = self.tasks[selected[0]]
        self.entry.delete(0, tk.END)
        self.entry.insert(0, task['title'])
        self.content.delete('1.0', tk.END)
        self.content.insert('1.0', task['content'])

    def edit_task(self):
        selected = self.task_list.curselection()
        if not selected:
            messagebox.showwarning('Выбор задачи', 'Выберите задачу в списке для редактирования.')
            return
        title, content = self._get_fields()
        if not title:
            messagebox.showwarning('Название задачи', 'Введите название задачи.')
            return
        index = selected[0]
        old_task = self.tasks[index]
        self.tasks[index] = {'title': title, 'content': content}
        if self.save_tasks():
            self.show_tasks()
            self.task_list.selection_set(index)
            self.task_list.activate(index)
        else:
            self.tasks[index] = old_task

    def delete_task(self):
        selected = self.task_list.curselection()
        if not selected:
            return
        index = selected[0]
        removed = self.tasks.pop(index)
        if self.save_tasks():
            self.show_tasks()
            self.clear_entry()
        else:
            self.tasks.insert(index, removed)

    def clear_entry(self):
        self.task_list.selection_clear(0, tk.END)
        self.entry.delete(0, tk.END)
        self.content.delete('1.0', tk.END)
