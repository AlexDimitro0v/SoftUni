from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def read_point():
    """Function to read a point from the user"""
    x, y = map(int, input().split())
    point = Point(x, y)
    return point


def main():
    first_point = read_point()
    second_point = read_point()

    side_a = abs(first_point.x - second_point.x)
    side_b = abs(first_point.y - second_point.y)
    distance = sqrt(side_a**2 + pow(side_b, 2))

    print(f"{distance:.3f}")


# another way
# ________________________________________________________________________________
class Point2(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def distance_to_another_point(self, p2):
        side_a = p2.x - self.x
        side_b = p2.y - self.y
        return sqrt(side_a**2 + side_b**2)
        # In reality we break the OOP concept for reusability in this case:
        #   1. This Class needs something additional to create the method (p2 in our case)
        #   2. We want to create a class Point for a single point (only one x and y), not for many points.


def distance_between_points(p1: Point, p2: Point):  # reusable code (parameters: point1, point2 [both of class Point])
    side_a = p2.x - p1.x
    side_b = p2.y - p1.y
    return sqrt(side_a**2 + side_b**2)


def solve():
    data = map(int, input().split())
    point1 = Point2(*data)
    point2 = read_point()

    print(f"{point1.distance_to_another_point(point2):.3f}")


if __name__ == '__main__':      # Driver code
    main()
