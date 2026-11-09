"""Чтение и сохранение задач с названием и содержимым в JSON."""
import json
from pathlib import Path


def load_tasks(filename):
    """Загрузить задачи. Старый формат (список строк) тоже поддерживается."""
    path = Path(filename)
    if not path.exists():
        return []
    with path.open('r', encoding='utf-8') as source:
        data = json.load(source)
    if not isinstance(data, list):
        raise ValueError('Файл задач должен содержать JSON-массив')
    tasks = []
    for item in data:
        if isinstance(item, str):
            tasks.append({'title': item, 'content': ''})
        elif (isinstance(item, dict) and isinstance(item.get('title'), str)
              and isinstance(item.get('content', ''), str)):
            tasks.append({'title': item['title'], 'content': item.get('content', '')})
        else:
            raise ValueError('Каждая задача должна быть строкой или объектом с title и content')
    return tasks


def save_tasks(filename, tasks):
    """Сохранить задачи в UTF-8 JSON."""
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8') as target:
        json.dump(tasks, target, ensure_ascii=False, indent=4)
