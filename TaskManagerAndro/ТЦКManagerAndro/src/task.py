"""Модель одной задачи."""
from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class Task:
    title: str
    description: str = ''
    status: str = 'Новая'
    author: str = 'Пользователь'
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec='seconds'))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'author': self.author,
            'created_at': self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        if isinstance(data, str):
            return cls(title=data)
        if not isinstance(data, dict) or not isinstance(data.get('title'), str):
            raise ValueError('Некорректная запись задачи')
        description = data.get('description', data.get('content', ''))
        if not isinstance(description, str):
            raise ValueError('Описание задачи должно быть строкой')
        status = data.get('status', 'Новая')
        author = data.get('author', 'Пользователь')
        if not isinstance(status, str) or not isinstance(author, str):
            raise ValueError('Некорректные поля задачи')
        return cls(
            title=data['title'], description=description,
            status=status, author=author,
            id=str(data.get('id') or uuid4()),
            created_at=str(data.get('created_at') or datetime.now().isoformat(timespec='seconds')),
        )
