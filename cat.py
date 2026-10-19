from Animal import Animal

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

cat = Cat("Муся", 10)
cat2 = Cat("Буся", 4)
print(cat.__str__(), cat2.__str__())
cat.speak("Мур, Мур")
cat2.speak("Мяу, мяу")
