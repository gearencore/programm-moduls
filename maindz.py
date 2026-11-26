print("Задание 1")

nums = [i for i in range(1, 11) if i % 2 == 0]
print("Чётные числа:", nums)

print("\nЗадание 2")

user = {
    "Хлеб": 50,
    "Молоко": 100,
    "Сыр": 200
}

user["Хлеб"] = 60

for key, value in user.items():
    print(key, "-", value, "руб.")

print("\nЗадание 3")

products = ["Хлеб", "Молоко", "Хлеб", "Сыр", "Молоко"]

tags = set(products)

print("Исходный список:", products)
print("Без дубликатов:", tags)
print("Есть ли Хлеб?", "Хлеб" in tags)


print("\nЗадание 4")

point = (10, 20)
print("Координаты:", point)

try:
    point[0] = 30
except TypeError:
    print("Ошибка TypeError: кортеж нельзя изменять")


print("\nЗадание 5")

squares1 = []

for i in range(1, 6):
    squares1.append(i ** 2)

squares2 = [i ** 2 for i in range(1, 6)]

print("Через цикл:", squares1)
print("Через comprehension:", squares2)
print("Результаты одинаковые:", squares1 == squares2)



