from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name, age, gender):
        self.name = name
        self.age = int(age)
        self.gender = gender

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise Exception('Invalid input!')
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0 or not age:
            raise Exception("Invalid input!")
        self._age = age

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        if not gender:
            raise Exception('Invalid input!')
        self._gender = gender

    @abstractmethod
    def produce_sound(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}\n{self.name} {self.age} {self.gender}\n{self.produce_sound()}"


class Dog(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def produce_sound(self):
        return "Woof!"


class Frog(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def produce_sound(self):
        return "Ribbit"


class Cat(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def produce_sound(self):
        return "Meow meow"


class Kitten(Cat):
    def __init__(self, name, age, gender):
        super().__init__(name, age, 'Female')

    def produce_sound(self):
        return "Meow"


class Tomcat(Cat):
    def __init__(self, name, age, gender):
        super().__init__(name, age, 'Male')

    def produce_sound(self):
        return "MEOW"


def main():
    while True:
        cls = input()
        if cls == 'Beast!':
            return
        try:
            params = input().split()              # name, age, gender
            animal = eval(cls)(*params)
            print(animal)
        except Exception as e:
            if cls not in ['Dog', 'Cat', 'Frog', 'Rabbit', 'Kitten', 'Tomcat']:
                print('Invalid input!')
            else:
                print(e)


if __name__ == '__main__':
    main()
