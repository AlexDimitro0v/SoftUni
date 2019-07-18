from math import sqrt
import itertools


class Point:
    list_of_points = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.list_of_points.append(self)  # or the equivalent Point.list_of_points.append(self)

    def distance_to_another_point(self, p2):
        side_a = p2.x - self.x
        side_b = p2.y - self.y
        distance = sqrt(side_a**2 + side_b**2)
        return distance


def read_point():
    data = map(int, input().split())
    Point(*data)


def main():
    n = int(input())
    for times in range(n):
        read_point()           # abstraction

    shortest_distance = float('Infinity')
    closest_points = iter([None, None])     # iter() saves memory for us
    for p1, p2 in itertools.product(Point.list_of_points, Point.list_of_points[1:]):   # simulating a cross-product
        current_distance = p1.distance_to_another_point(p2)
        if current_distance < shortest_distance and p1 is not p2:                 # should avoid having the same points
            shortest_distance = current_distance
            closest_points = p1, p2     # keep memory of the points which have the shortest distance between each other

    print(f"{shortest_distance:.3f}")
    for point in closest_points:
        print(f"({point.x}, {point.y})")


if __name__ == '__main__':
    main()
