"""Основной файл приложения
    версия 0.0.2
"""
from random import choice

collection = ['task1', 'task2', 'task3']
is_start = True

while (is_start):
    print("2 - показать задачи \ 1 - добавить заметку")
    choice_user = input('введите ваш выбор (1 или 2)')
    match int(choice_user):
        case 1:
            print(collection[0])
        case 2:
            collection.append('task5')
            print(collection)
        case _:
            print('такого пункта нет...')
