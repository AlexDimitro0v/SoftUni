class Rectangle:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top

        self.width = width
        self.height = height

        self.right = self.left + self.width
        self.bottom = self.top + self.height

    def is_inside(self, r2):
        """Checks if the current rectangle object is inside another rectangle object. Returns a boolean value."""
        if type(r2) is not type(self):
            raise TypeError('other_rect is not a Rectangle!')

        # Boolean Values
        is_left = self.left >= r2.left
        is_right = self.right <= r2.right

        is_inside_horizontal = is_left and is_right         # T/F and T/F

        is_top = self.top >= r2.top
        is_bottom = self.bottom <= r2.bottom

        is_inside_vertical = is_top and is_bottom           # T/F and T/F

        return is_inside_horizontal and is_inside_vertical  # T/F and T/F        -> (T or F) as a return value


def read_rectangle():
    coords = map(int, input().split())
    left, top, width, height = coords

    rect = Rectangle(left, top, width, height)
    # rect = Rectangle(*coords) works the same
    return rect


if __name__ == '__main__':
    rect1 = read_rectangle()
    rect2 = read_rectangle()
    print('Inside' if rect1.is_inside(rect2) else 'Not inside')
