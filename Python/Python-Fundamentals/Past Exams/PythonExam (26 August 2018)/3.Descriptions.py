import re


class Person:
    def __init__(self, name, age, birthdate):
        self.name = name
        self.age = age
        self.birthdate = birthdate


database = []

while True:
    inp = input()
    if inp == "make migrations":
        break

    result = re.findall("(?<=name is )([A-Z][a-z]+)\s([A-Z]+[a-z]+)", inp)
    if not result:
        continue
    name = " ".join(result[0])

    result = re.findall("\s\d{2}\s(?=years)", inp)
    if not result:
        continue
    age = int(result[0])

    result = re.findall("on\s\d{2}-\d{2}-\d{4}", inp)
    if not result:
        continue
    birthdate = result[0].strip('on ')

    database.append(Person(name, age, birthdate))

if not database:
    print("DB is empty")
else:
    for person in database:
        print(f"Name of the person: {person.name}.")
        print(f"Age of the person: {person.age}.")
        print(f"Birthdate of the person: {person.birthdate}.")
