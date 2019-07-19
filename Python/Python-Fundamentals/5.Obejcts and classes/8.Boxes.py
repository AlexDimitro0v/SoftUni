from math import sqrt


class Point:
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    @staticmethod
    def distance_to_another_point(p1, p2):
        side_a = p2.x - p1.x
        side_b = p2.y - p1.y
        distance = sqrt(side_a**2 + side_b**2)
        return int(distance)


class Box:
    box_list = []

    def __init__(self, upper_left, upper_right, bottom_left, bottom_right):
        self.upper_left = Point(*upper_left)        # property from class Point
        self.upper_right = Point(*upper_right)
        self.bottom_left = Point(*bottom_left)
        self.bottom_right = Point(*bottom_right)
        self.box_list.append(self)

    def __str__(self):
        return f"Box: {self.width}, {self.height}"

    @property
    def width(self):
        return Point.distance_to_another_point(self.upper_left, self.upper_right)

    @property
    def height(self):
        return Point.distance_to_another_point(self.upper_left, self.bottom_left)

    def calculate_perimeter(self):
        return 2*(self.width+self.height)

    def calculate_area(self):
        return self.width*self.height


def main():
    data = input()
    while data != 'end':
        points = data.split(' | ')
        coords = []                     # clears out at every iteration
        for point in points:
            (x, y) = point.split(':')
            coords.append((x, y))
        Box(*coords)                    # or Box(coords[0], coords[1], coords[2], coords[3])
        data = input()

    for box in Box.box_list:
        print(box)
        print(f"Perimeter: {box.calculate_perimeter()}")
        print(f"Area: {box.calculate_area()}")


if __name__ == '__main__':
    main()
