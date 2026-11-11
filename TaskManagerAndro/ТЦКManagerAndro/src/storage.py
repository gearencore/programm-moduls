"""Хранение задач в JSON и операции с ними."""
import json
import os
import tempfile
from pathlib import Path

from task import Task


class StorageManager:
    def __init__(self, filename):
        self.filename = Path(filename)
        self.tasks = []

    def load(self):
        if not self.filename.exists():
            self.tasks = []
            return self.tasks
        with self.filename.open('r', encoding='utf-8-sig') as source:
            data = json.load(source)
        if not isinstance(data, list):
            raise ValueError('Файл задач должен содержать JSON-массив')
        # Сначала преобразуем всё, чтобы при ошибке не потерять старое состояние.
        loaded = [Task.from_dict(item) for item in data]
        ids = [task.id for task in loaded]
        if len(ids) != len(set(ids)):
            raise ValueError('В файле повторяются идентификаторы задач')
        self.tasks = loaded
        return self.tasks

    def save(self):
        self.filename.parent.mkdir(parents=True, exist_ok=True)
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(
                mode='w', encoding='utf-8', dir=self.filename.parent,
                prefix='.task_', suffix='.tmp', delete=False,
            ) as target:
                temporary = Path(target.name)
                json.dump([task.to_dict() for task in self.tasks], target,
                          ensure_ascii=False, indent=4)
                target.flush()
                os.fsync(target.fileno())
            os.replace(temporary, self.filename)
        finally:
            if temporary is not None and temporary.exists():
                temporary.unlink()

    def add(self, task):
        self.tasks.append(task)
        try:
            self.save()
        except OSError:
            self.tasks.pop()
            raise
        return task

    def update(self, task_id, title, description, author):
        for task in self.tasks:
            if task.id == task_id:
                previous = (task.title, task.description, task.author)
                task.title, task.description, task.author = title, description, author
                try:
                    self.save()
                except OSError:
                    task.title, task.description, task.author = previous
                    raise
                return task
        raise ValueError('Задача не найдена')

    def delete(self, task_id):
        for index, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks.pop(index)
                try:
                    self.save()
                except OSError:
                    self.tasks.insert(index, task)
                    raise
                return
        raise ValueError('Задача не найдена')

    def toggle_status(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                previous = task.status
                task.status = 'Выполнена' if previous != 'Выполнена' else 'Новая'
                try:
                    self.save()
                except OSError:
                    task.status = previous
                    raise
                return task
        raise ValueError('Задача не найдена')
