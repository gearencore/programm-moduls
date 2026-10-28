from cat import Cat
from dog import Dog


def main():
    animals = [
        Cat('Муся', 10),
        Cat('Буся', 4),
        Dog('Eater of Galaxy', 1000000, 'Chihuahua'),]

    for animal in animals:
        print(animal)
        animal.speak()
        animal.move()
        print("=====================")

    animals[-1].defend()


if __name__ == '__main__':
    main()
