from random import choice

collection = ["Oreshki BIG BOB","Taraska" ]
is_running = True

def show_collection(task_collection):
    print("============================")
    for i, j in enumerate(task_collection):
        print(i, j)
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
            collection.append(add_task)
        case '3' :
            print("============================")
            show_collection(collection)
            print("============================")
            select_task = int(input("Введите номер задачи для редактирования - "))
            print("============================")
            edit_task = input("Введите новое имя выбранной задачи для редактирования - ")
            collection[select_task - 1] = edit_task
        case '4':
            show_collection(collection)
            delete_task = int(input("Введите номер задачи для удаления - "))
            collection.pop(delete_task - 1)
        case '5':
            is_running = False
            print("============================")
            (print("До свидания!"))
            print("============================")
        case _:
           print("Такого пункта нет!")
