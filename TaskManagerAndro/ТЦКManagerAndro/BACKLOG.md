# BACKLOG — Task Manager

## Выполнено (модульная архитектура)

- [x] Создан класс Task с полями id, title, description, status, author, created_at.
- [x] Добавлены методы to_dict() и from_dict().
- [x] Создан StorageManager: load, save, add, update, delete и toggle_status.
- [x] Сохранение перенесено в JSON; старые записи поддерживаются.
- [x] Создана прослойка Interface с AppButton, AppListbox, AppEntry, AppLabel.
- [x] В TaskView реализованы build, get_input, show_tasks, ask_confirm.
- [x] Создан TaskManager, управляющий созданием, редактированием, удалением и статусом задач.
- [x] Точка входа main.py создаёт TaskManager и вызывает run().
- [x] Удалены неиспользуемые учебные примеры, калькулятор, кэш и дублирующие файлы.
- [x] Исправлены небольшие ошибки сохранения и обновления списка.
