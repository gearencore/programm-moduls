from pathlib import Path

from storage import StorageManager
from task import Task
from view import TaskView


class TaskManager:
    def __init__(self, filename=None, view=None):
        if filename is None:
            filename = Path(__file__).resolve().parent / 'task.json'
        self.storage = StorageManager(filename)
        self.view = view if view is not None else TaskView()
        self.selected_id = None
        self.view.set_actions(self)
        try:
            self.storage.load()
        except (OSError, ValueError) as error:
            self.view.error('Ошибка загрузки', f'Не удалось прочитать задачи:\n{error}')
        self.show_tasks()

    def show_tasks(self):
        self.view.show_tasks(self.storage.tasks, self.selected_id)

    def _selected(self):
        for task in self.storage.tasks:
            if task.id == self.selected_id:
                return task
        return None

    def select_task(self, event=None):
        selection = self.view.task_list.curselection()
        if not selection:
            return
        index = selection[0]
        if index >= len(self.storage.tasks):
            return
        task = self.storage.tasks[index]
        self.selected_id = task.id
        self.view.show_task(task)

    def create_task(self):
        title, description, author = self.view.get_input()
        if not title:
            self.view.warning('Название задачи', 'Введите название задачи.')
            return
        try:
            self.storage.add(Task(title=title, description=description,
                                  author=author or 'Пользователь'))
        except OSError as error:
            self.view.error('Ошибка сохранения', str(error))
            return
        self.clear_fields()
        self.show_tasks()

    def edit_task(self):
        task = self._selected()
        if task is None:
            self.view.warning('Выбор задачи', 'Выберите задачу для редактирования.')
            return
        title, description, author = self.view.get_input()
        if not title:
            self.view.warning('Название задачи', 'Введите название задачи.')
            return
        try:
            self.storage.update(task.id, title, description, author or 'Пользователь')
        except (OSError, ValueError) as error:
            self.view.error('Ошибка сохранения', str(error))
            return
        self.show_tasks()

    def delete_task(self):
        task = self._selected()
        if task is None:
            self.view.warning('Выбор задачи', 'Выберите задачу для удаления.')
            return
        if not self.view.ask_confirm('Удаление', f'Удалить задачу «{task.title}»?'):
            return
        try:
            self.storage.delete(task.id)
        except (OSError, ValueError) as error:
            self.view.error('Ошибка удаления', str(error))
            return
        self.clear_fields()
        self.show_tasks()

    def toggle_status(self):
        task = self._selected()
        if task is None:
            self.view.warning('Выбор задачи', 'Выберите задачу для смены статуса.')
            return
        try:
            self.storage.toggle_status(task.id)
        except (OSError, ValueError) as error:
            self.view.error('Ошибка сохранения', str(error))
            return
        self.show_tasks()

    def clear_fields(self):
        self.selected_id = None
        self.view.clear_fields()

    def run(self):
        self.view.root.mainloop()
