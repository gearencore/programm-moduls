"""Размещение элементов окна и отображение задач."""
import tkinter as tk

from ui.AppLabel import AppLabel
from ui.AppListbox import AppListbox
from ui.Button import AppButton


class TaskView:
    """Создаёт элементы интерфейса; действия выполняются классом Interface."""

    def __init__(self, root, on_add, on_delete, on_save, on_clear, on_select):
        self.title_label = AppLabel(root, 'TASK MANAGER')
        self.title_label.pack(pady=10)

        self.task_list = AppListbox(root)
        self.task_list.pack(fill='both', expand=True, padx=20, pady=(4, 8))
        self.task_list.bind('<<ListboxSelect>>', on_select)

        tk.Label(root, text='Название задачи', bg='#202020', fg='white').pack(anchor='w', padx=20)
        self.entry = tk.Entry(root, font=('Arial', 12))
        self.entry.pack(fill='x', padx=20, pady=(2, 8))

        tk.Label(root, text='Содержимое задачи', bg='#202020', fg='white').pack(anchor='w', padx=20)
        self.content = tk.Text(root, font=('Arial', 11), height=7, wrap='word')
        self.content.pack(fill='both', expand=True, padx=20, pady=(2, 8))

        buttons = tk.Frame(root, bg='#202020')
        buttons.pack(pady=(0, 12))
        AppButton(buttons, 'Добавить', on_add).pack(side='left', padx=4)
        AppButton(buttons, 'Сохранить изменения', on_save).pack(side='left', padx=4)
        AppButton(buttons, 'Удалить', on_delete).pack(side='left', padx=4)
        AppButton(buttons, 'Очистить', on_clear).pack(side='left', padx=4)

    def show_tasks(self, tasks):
        self.task_list.show_tasks([task['title'] for task in tasks])


def task_print(tasks, pause=True):
    """Совместимость с существующими консольными функциями core.py."""
    for number, task in enumerate(tasks, 1):
        print(f'{number} задача: {task}')
    if pause:
        input('Нажмите Enter, чтобы продолжить')
