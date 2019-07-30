# _____________________________________________________________________________________________________________________


# Proper Python getters and setters solution  -> props is a shortcut for displaying all the getter and setters
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise Exception("Age must be positive!")
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) < 3:
            raise Exception("Name's length should not be less than 3 symbols!")
        self._name = name

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise Exception("Age must be positive!")
        elif age > 15:
            raise Exception("Child's age must be less than 15!")
        self._age = age


def main():
    name = input()
    age = int(input())
    try:
        child = Child(name, age)
        print(child)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
