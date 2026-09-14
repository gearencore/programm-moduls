from random import choice

collection = []
is_running = True

def show_collection(task_collection):
    print("============================")
    for i, j in enumerate(task_collection):
        print(i + 1, j)
    print("============================")

def show_menu():
    print("1 - посмотреть задачи \n"
          "2 - добавить задачи\n"
          "3 - редактировать задачу \n"
          "4 - удаление задачи \n"
          "5 - Выход \n")
while is_running:
    show_menu()
    choice_user = input('Введите ваш выбор - ')

    match str(choice_user):
        case '1':
            show_collection(collection)
        case '2':
            print("============================")
            add_task = input("Введите имя задачи для создания - ")
            if add_task.startswith(' '):
                if len(add_task) < 2:
                    print("Название не может быть пустым!")
                    continue
                else:
                    collection.append(f"Новая задча {len(collection)+1}")
            else:
                collection.append(add_task)
        case '3' :
            show_collection(collection)
            select_task = input("Введите номер задачи для редактирования - ")
            if int(select_task.isdigit()):
                if int(select_task) > 0 and int(select_task) <= len(collection):
                    edit_task = input("Введите новое имя выбранной задачи для редактирования - ")
                    collection[int(select_task) - 1] = edit_task
                    print (f"задача '{int(select_task)} : {edit_task}'")
                else:
                    print("НЕТ ТАКОГО НОМЕРА В СПИСКЕ!")
        case '4':
            show_collection(collection)
            delete_task = int(input("Введите номер задачи для удаления - "))
            if select_task.isdigit():
                if int(delete_task) > 0 and (delete_task <= len(collection)):
                    collection.pop(delete_task - 1)
                    print (f"Задача '{delete_task}' успешно удалена!")
        case '5':
            is_running = False
            print("До свидания!")
        case _:
            print("Такого пункта нет!")
