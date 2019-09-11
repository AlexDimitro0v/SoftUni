from abc import ABC, abstractmethod


class Item(ABC):
    @abstractmethod
    def __init__(self, id_n, op_system, price):
        self.id_n = id_n
        self.op_system = op_system
        self.price = price

    @property
    def id_n(self):
        return self.__id_n

    @id_n.setter
    def id_n(self, value):
        if not value.isalpha():
            raise Exception('Invalid id!')
        if not len(value) >= 8:
            raise Exception('Invalid id!')
        self.__id_n = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise Exception('Invalid price!')
        if value == 0:
            raise Exception('Invalid price!')
        self.__price = value

    def __str__(self):
        return f'Item id: {self.id_n}\nOperating system: {self.op_system}\nPrice: {self.price}'


class Phone(Item):
    @abstractmethod
    def __init__(self, id_n, op_system, price):
        super().__init__(id_n, op_system, price)

    @staticmethod
    def make_call():
        return 'Making call...'

    @staticmethod
    def receive_call():
        return 'Receiving a call!'

    @staticmethod
    def send_message():
        return 'Sending message...'

    @staticmethod
    def receive_message():
        return 'Receiving a message!'


class Tablet(Item):
    def __init__(self, id_n, op_system, price):
        super().__init__(id_n, op_system, price)

    @staticmethod
    def stream_movie():
        return 'Streaming movie...'


class SmartPhone(Phone):
    def __init__(self, id_n, op_system, price, apps):
        super().__init__(id_n, op_system, price)
        self.apps = apps

    @property
    def apps(self):
        return self.__apps

    @apps.setter
    def apps(self, value: list):
        if not len(value) >= 5:
            raise Exception("Invalid number of applications!")
        self.__apps = value

    @staticmethod
    def browse_internet():
        return 'Browsing...'

    def __str__(self):
        return super().__str__() + f'\nApplications: {", ".join(self.apps)}'


class CellPhone(Phone):
    def __init__(self, id_n, op_system, price):
        super().__init__(id_n, op_system, price)


def reporting(db):
    data = input()
    while data != 'end':
        command = data.split()[0]
        # functionality += '()'
        if command == 'test':
            id_number = data.split()[1]
            functionality = data.split()[2]
            current_items = list(filter(lambda i: i.id_n == id_number, db))
            if current_items:
                for item in current_items:
                    try:
                        result = getattr(item, functionality)()
                        print(result)
                    except:
                        print("Invalid request has been made!")
            else:
                print("Invalid request has been made!")
        else:
            kind = data.split()[1]
            left_items = list(filter(lambda i: i.__class__.__name__ == kind, db))
            if left_items:
                for item in left_items:
                    print(item)
            else:
                print("Invalid request has been made!")

        data = input()


def main():
    db = []
    data = input()
    while data != 'end':
        try:
            obj = eval(data)
            db.append(obj)
        except Exception as e:
            print(e)
        data = input()
    reporting(db)


if __name__ == '__main__':
    main()


"""
Tablet("abcdegee", "iOS", 30)
SmartPhone("abcdefgeeee", "iOS", 20, ["facebook", "messanger", "snapchat", "viber", 'alex'])
SmartPhone("12345", "iOS", 20, ["facebook", "321", "123", "viber", 'alex'])
Item("abcdefge", "iOS", 20)
Phone('fsd', 'IOS', 20)
end
test abcdegee stream_movie
test abcdefgeeee make_call
test abcdefgeeee receive_call
test abcdefgeeee send_message
test abcdefgeeee receive_message
test abcdefgeeee browse_internet
test abcdegee browse_internet
test abcdegee make_call
report SmartPhone
report Tablet
end


•	make_call() you must print - Making call...
•	receive_call() you must print – Receiving a call!
•	send_message() you must print – Sending message...
•	receive_message() you must print – Receiving a message!
•	browse_internet() you must print - Browsing...
•	stream_movie() you should print - Streaming movie...
"""
