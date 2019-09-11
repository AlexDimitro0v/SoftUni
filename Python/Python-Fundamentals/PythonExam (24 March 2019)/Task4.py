from abc import ABC, abstractmethod


class Apartment(ABC):
    def __init__(self, id_n, rooms, baths, square_meters, price):
        self.id_n = id_n
        self.rooms = int(rooms)
        self.baths = int(baths)
        self.square_meters = float(square_meters)
        self.price = float(price)

    @abstractmethod
    def __str__(self):
        return f"{self.rooms} rooms place with {self.baths} bathroom/s.\n{self.square_meters} sq. meters for {self.price} lv."


class LivingApartment(Apartment):
    def __init__(self, id_n, rooms, baths, square_meters, price):
        super().__init__(id_n, rooms, baths, square_meters, price)
        self.availability = 'free'

    def __str__(self):
        return super().__str__()


class OfficeApartment(Apartment):
    def __init__(self, id_n, rooms, baths, square_meters, price):
        super().__init__(id_n, rooms, baths, square_meters, price)
        self.availability = 'free'

    def __str__(self):
        return super().__str__()


def feeding():
    db = []
    data = input()
    while data != 'start_selling':
        inputs = data.split()
        findex = data.find('(')
        class_type = data[:findex]
        try:
            ap = eval(data)
            db += [ap]
        except TypeError as e:
            if len(inputs) == 4 or class_type == "Apartment":
                print(e)
        data = input()
    return db


def selling(db):
    data = input()
    stop = ['free', 'taken']
    while data not in stop:
        command, id_number = data.split()

        if command == 'rent':
            flag = False
            for obj in db:
                if obj.id_n == id_number:
                    flag = True
                    if obj.availability == 'free':
                        if isinstance(obj, LivingApartment):
                            print(f"Apartment with id - {id_number} is only for selling!")
                            break
                        elif isinstance(obj, OfficeApartment):
                            obj.availability = 'taken'
                            break
                    elif obj.availability == 'taken':
                        print(f"Apartment with id - {id_number} is already taken!")
                        break
            if not flag:
                print(f"Apartment with id - {id_number} does not exist!")
        elif command == 'hire' or command == 'buy':         # NOTE: MISTAKE BY SOFTUNI
            flag = False
            for obj in db:
                if obj.id_n == id_number:
                    flag = True
                    if obj.availability == 'free':
                        if isinstance(obj, LivingApartment):
                            obj.availability = 'taken'
                            break
                        elif isinstance(obj, OfficeApartment):
                            print(f"Apartment with id - {id_number} is only for renting!")
                            break
                    elif obj.availability == 'taken':
                        print(f"Apartment with id - {id_number} is already taken!")
                        break
            if not flag:
                print(f"Apartment with id - {id_number} does not exist!")
        data = input()

    if data == 'free':
        free_aps = list(filter(lambda x: x.availability == 'free', db))
        free_aps = sorted(free_aps, key=lambda el: (-el.price, el.square_meters))
        if free_aps:
            for element in free_aps:
                print(element)
        else:
            print("No information for this query")

    elif data == 'taken':
        taken_apps = sorted(list(filter(lambda x: x.availability == 'taken', db)), key=lambda el: (el.price, -el.square_meters))
        if taken_apps:
            for element in taken_apps:
                print(element)
        else:
            print("No information for this query")


def main():
    db = feeding()
    selling(db)


if __name__ == '__main__':
    main()
