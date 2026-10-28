from animal import Animal


class Cat(Animal):
    def __init__(self, name, age, breed='Cat'):
        super().__init__(name, age, breed)

    def speak(self):
        print(f'{self.name}: Мяу-мяу!')

    def move(self):
        print(f'{self.name} бесшумно крадётся')
