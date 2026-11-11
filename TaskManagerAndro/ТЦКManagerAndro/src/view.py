"""Создание элементов окна и отображение задач."""
import tkinter as tk

from ui.Interface import Interface


class TaskView(Interface):
    def __init__(self):
        super().__init__()
        self.build()

    def build(self):
        self.label(self.root, 'TASK MANAGER').pack(pady=10)

        self.task_list = self.listbox(self.root)
        self.task_list.pack(fill='both', expand=True, padx=20, pady=(4, 8))

        tk.Label(self.root, text='Название задачи', bg='#202020', fg='white').pack(anchor='w', padx=20)
        self.title_entry = self.entry(self.root)
        self.title_entry.pack(fill='x', padx=20, pady=(2, 8))

        tk.Label(self.root, text='Автор', bg='#202020', fg='white').pack(anchor='w', padx=20)
        self.author_entry = self.entry(self.root)
        self.author_entry.pack(fill='x', padx=20, pady=(2, 8))
        self.author_entry.insert(0, 'Пользователь')

        tk.Label(self.root, text='Содержимое задачи', bg='#202020', fg='white').pack(anchor='w', padx=20)
        self.description = tk.Text(self.root, font=('Arial', 11), height=7,
                                   wrap='word', bg='#303030', fg='white',
                                   insertbackground='white')
        self.description.pack(fill='both', expand=True, padx=20, pady=(2, 8))

        self.buttons = tk.Frame(self.root, bg='#202020')
        self.buttons.pack(pady=(0, 12))

    def set_actions(self, manager):
        self.task_list.bind('<<ListboxSelect>>', manager.select_task)
        for label, action in (
            ('Добавить', manager.create_task),
            ('Сохранить', manager.edit_task),
            ('Статус', manager.toggle_status),
            ('Удалить', manager.delete_task),
            ('Очистить', manager.clear_fields),
        ):
            self.button(self.buttons, label, action).pack(side='left', padx=3)

    def get_input(self):
        return (
            self.title_entry.get().strip(),
            self.description.get('1.0', 'end-1c'),
            self.author_entry.get().strip(),
        )

    def show_tasks(self, tasks, selected_id=None):
        labels = [f"{'✓' if task.status == 'Выполнена' else '○'}  {task.title}" for task in tasks]
        self.task_list.show_tasks(labels)
        if selected_id is not None:
            for index, task in enumerate(tasks):
                if task.id == selected_id:
                    self.task_list.selection_set(index)
                    self.task_list.activate(index)
                    break

    def show_task(self, task):
        self.title_entry.delete(0, tk.END)
        self.title_entry.insert(0, task.title)
        self.author_entry.delete(0, tk.END)
        self.author_entry.insert(0, task.author)
        self.description.delete('1.0', tk.END)
        self.description.insert('1.0', task.description)

    def clear_fields(self):
        self.task_list.selection_clear(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.description.delete('1.0', tk.END)
        self.author_entry.delete(0, tk.END)
        self.author_entry.insert(0, 'Пользователь')

    def ask_confirm(self, title, text):
        return self.confirm(title, text)
