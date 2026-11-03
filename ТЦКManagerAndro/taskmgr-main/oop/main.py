from animal import Animal


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Кошка")


if __name__ == "__main__":
    cat1 = Cat("Маруся", 10)
    cat2 = Cat("John", 11)
    print(cat1)
    print(cat2)
