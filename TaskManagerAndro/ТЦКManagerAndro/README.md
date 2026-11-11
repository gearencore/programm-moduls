# Task Manager

Учебный менеджер задач на Python и Tkinter. Для работы требуется Python с поддержкой Tkinter.

## Запуск

Из корня проекта:

```bash
python src/main.py
```

## Использование

Введите название, автора и содержимое задачи и нажмите «Добавить». Выберите запись в списке для редактирования или удаления. Кнопка «Статус» переключает задачу между «Новая» и «Выполнена». Все изменения автоматически сохраняются в `src/task.json`.

## Структура

- `src/task.py` — класс Task с полями id, title, description, status, author, created_at и методами to_dict()/from_dict().
- `src/storage.py` — класс StorageManager с методами load(), save(), add(), update(), delete(), toggle_status().
- `src/ui/Interface.py` — прослойка Tkinter и общие виджеты.
- `src/ui/AppLabel.py`, `src/ui/AppListbox.py`, `src/ui/AppEntry.py`, `src/ui/Button.py` — собственные классы виджетов.
- `src/view.py` — окно TaskView с build(), get_input(), show_tasks(), ask_confirm().
- `src/core.py` — класс TaskManager, основная логика CRUD и run ().
- `src/main.py` — точка входа.
- `src/task.json` — задачи в JSON.

Старые записи JSON со строками либо полями `title` и `content` поддерживаются при загрузке; после следующего сохранения они преобразуются в новый формат.
