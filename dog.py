from animal import Animal


class Dog(Animal):
    def __init__(self, name, age, breed='Dog'):
        super().__init__(name, age, breed)

    def speak(self):
        print(f'{self.name}: Гав-гав!')

    def move(self):
        print(f'{self.name} радостно бежит')

    def defend(self):
        print('ГАВГАВГАВГАВГАВ')
