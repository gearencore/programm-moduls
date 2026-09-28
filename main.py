"""Основной файл приложения

    версия 0.0.8

    === Описание ===
        Приложение может сохранять задачи, выдает список задач,
        может удалять и редактировать задачи
"""

collection = []
is_running = True
name_file = "saves.txt"


def show_collection(task_collection):
    print("=" * 45)
    if not task_collection:
        print("Список задач пуст!")
    else:
        for number, content in enumerate(task_collection):
            parts = content.strip().split("|", 1)
            task_name = parts[0].strip()
            if len(parts) > 1:
                task_content = parts[1].strip()
            else:
                task_content = ""
            print(f"{number + 1}. {task_name}")
            print(f"   Содержание: {task_content}")
    print("=" * 45)


def show_menu():
    print("1 - Показать задачи")
    print("2 - Добавить задачу")
    print("3 - Редактировать задачу")
    print("4 - Удаление задачи")
    print("5 - Выход")


def check_confirm(select_task, task_list):
    if select_task.isdigit():
        if 0 < int(select_task) <= len(task_list):
            return True
        else:
            print(f"Задачи с номером {select_task} нет в списке!")
            return False
    else:
        print("Введите именно номер задачи!")
        return False


def delete_tasks(task_collection):
    delete_task = input("Введите номер задачи: ")

    if check_confirm(delete_task, task_collection):
        task_collection.pop(int(delete_task) - 1)
        print(f"Задача {delete_task} удалена!")
    else:
        print("Неверный номер задачи!")


def edit_task(task_collection):
    edit_task_number = input("Введите номер задачи: ")

    if check_confirm(edit_task_number, task_collection):
        edit_name = input("Новое имя задачи: ").strip()
        edit_content = input("Новое содержимое задачи: ").strip()

        if not edit_name:
            print("Название задачи не может быть пустым!")
            return

        if not edit_content:
            print("Содержимое задачи не может быть пустым!")
            return

        task_collection[int(edit_task_number) - 1] = (
            f"{edit_name} | {edit_content}\n"
        )

        print(f"Задача «{edit_name}» успешно изменена!")


def add_task(task_collection):
    task_name = input("Введите имя задачи: ").strip()
    task_content = input("Введите содержимое задачи: ").strip()

    if not task_name:
        print("Имя задачи не может быть пустым!")
        return

    if not task_content:
        print("Содержимое задачи не может быть пустым!")
        return

    full_task = f"{task_name} | {task_content}"

    task_collection.append(full_task + "\n")

    print(f"Задача «{task_name}» успешно добавлена!")


def save_tasks(task_collection):
    with open(name_file, "w", encoding="utf-8") as file:
        file.writelines(task_collection)


def load_tasks():
    try:
        with open(name_file, "r", encoding="utf-8") as file:
            return file.readlines()

    except FileNotFoundError:
        return []


def main():
    global is_running

    collection.extend(load_tasks())

    while is_running:
        show_menu()
        choice_user = input("Введите ваш выбор: ")

        match choice_user:

            case "1":
                show_collection(collection)

            case "2":
                add_task(collection)
                save_tasks(collection)

            case "3":
                show_collection(collection)
                edit_task(collection)
                save_tasks(collection)

            case "4":
                show_collection(collection)
                delete_tasks(collection)
                save_tasks(collection)

            case "5":
                save_tasks(collection)
                is_running = False
                print("До свидания!")

            case _:
                print("Такого пункта нет...")


if __name__ == "__main__":
    main()
