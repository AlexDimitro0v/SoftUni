from abc import ABC, abstractmethod


class BaseMonster(ABC):
    @abstractmethod
    def __init__(self, name, id_num, strength, ugliness):
        self.name = name
        self.id = int(id_num)
        self.strength = int(strength)
        self.ugliness = int(ugliness)


class Hydralisk(BaseMonster):
    count = 0
    total_strength = 0

    def __init__(self, name, id_num, strength, ugliness, range):
        super().__init__(name, id_num, strength, ugliness)
        self.range = range
        Hydralisk.count += 1
        Hydralisk.total_strength += strength

    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, value):
        if str(value).isdigit():
            raise Exception('Range must be string')
        self.__range = value

    @staticmethod
    def set_range(range_value):                 # ALTERNATIVE WAY
        if not isinstance(range_value, str):
            raise Exception('Range must be string')
        return range_value


class Zergling(BaseMonster):
    count = 0
    total_speed = 0
    total_strength = 0

    def __init__(self, name, id_num, strength, ugliness, speed):
        super().__init__(name, id_num, strength, ugliness)
        self.speed = speed
        Zergling.count += 1
        Zergling.total_speed += speed
        Zergling.total_strength += strength

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        try:
            self.__speed = int(value)
        except ValueError:
            raise Exception('Speed must be integer')

    @staticmethod
    def set_speed_value(speed):                        # ALTERNATIVE WAY
        if not isinstance(speed, int):
            raise Exception('Speed must be integer')
        return speed


def main():
    data = input()
    while data != 'stopAddingArmy':
        try:
            eval(data)
        except Exception as e:
            print(e)
        data = input()

    print(f"Overall speed of army: {Zergling.total_speed}")
    print(f"Overall stength: {Hydralisk.total_strength + Zergling.total_strength}")
    print(f"Hydralisk: {Hydralisk.count}; Zergling: {Zergling.count}")


if __name__ == '__main__':
    main()
