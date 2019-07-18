class Animal:
    # animals_list = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.animals_list.append(self)


class Dog(Animal):
    def __init__(self, name, age, number_of_legs):
        super().__init__(name, age)
        self.number_of_legs = number_of_legs

    @staticmethod
    def produce_sound():
        return "I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau."


class Cat(Animal):
    def __init__(self, name, age, intelligence_quotient):
        super().__init__(name, age)
        self.intelligence_quotient = intelligence_quotient

    @staticmethod
    def produce_sound():
        return "I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau."


class Snake(Animal):
    def __init__(self, name, age, cruelty_coefficient):
        super().__init__(name, age)
        self.cruelty_coefficient = cruelty_coefficient

    @staticmethod
    def produce_sound():
        return "I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home."


def create_object(data):
    cls, name, age, param = data
    animal = eval(cls)(name, int(age), int(param))
    return animal


def main():
    animals_list = []
    data = input()
    while data != "I'm your Huckleberry":
        try:
            animals_list.append(create_object(data.split(' ')))
        except ValueError:
            animal_name = data.split(' ')[1]
            for animal in animals_list:
                # print(animal.__class__.__name__)   getting the class name of an instance
                if animal_name == animal.name:
                    print(animal.produce_sound())
                    # Class data can be accessed using object_name.property or <classname>.<attribute>
                    # example: Dog.produce_sound(animal)
        data = input()

    for animal in animals_list:
        if isinstance(animal, Dog):
            print(f"Dog: {animal.name}, Age: {animal.age}, Number Of Legs: {animal.number_of_legs}")

    for animal in animals_list:
        if isinstance(animal, Cat):
            print(f"{animal.__class__.__name__}: {animal.name}, Age: {animal.age}, IQ: {animal.intelligence_quotient}")

    for animal in animals_list:
        if isinstance(animal, Snake):
            print(f"Snake: {animal.name}, Age: {animal.age}, Cruelty: {animal.cruelty_coefficient}")


if __name__ == '__main__':
    main()
