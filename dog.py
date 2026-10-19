from Animal import Animal

class Dog():
    def __init__(self, name, age, breed):
     super().__init__(name, age, breed)

    def defend(self):
        print('ГАВГАВГАВГАВГАВ')

dog = Dog("Eater of Galaxy", 1000000, "Chihuiahuia")
print(dog.__str__())
