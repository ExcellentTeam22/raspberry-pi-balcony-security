FLT_MAX = 10 ** 9
# Python program to find the point of
# intersection of two lines


# Class used to  used to store the X and Y
# coordinates of a point respectively
class Point:
    """
    Class to represent point in the picture.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Method used to display X and Y coordinates
    # of a point
    def displayPoint(self, p):
        print(f"({p.x}, {p.y})")

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y


def line_line_intersection(line_start: Point,
                           line_end: Point,
                           rectangle_top_left: Point,
                           rectangle_bottom_right: Point):
    # Line AB represented as a1x + b1y = c1
    a1 = line_end.get_y() - line_start.get_y()
    b1 = line_start.get_x() - line_end.get_x()
    c1 = a1 * line_start.get_x() + b1 * line_start.get_y()

    # Line CD represented as a2x + b2y = c2
    a2 = rectangle_bottom_right.get_y() - rectangle_top_left.get_y()
    b2 = rectangle_top_left.get_x() - rectangle_bottom_right.get_x()
    c2 = a2 * rectangle_top_left.get_x() + b2 * rectangle_top_left.get_y()

    determinant = a1 * b2 - a2 * b1

    if determinant == 0:
        # The lines are parallel. This is simplified
        # by returning a pair of FLT_MAX
        return Point(FLT_MAX, FLT_MAX)
    else:
        x = (b2 * c1 - b1 * c2) / determinant
        y = (a1 * c2 - a2 * c1) / determinant
        if x < line_start.get_x() or x > line_end.get_x():
            if y < line_start.get_y() or y > line_end.get_y():
                return Point(FLT_MAX, FLT_MAX)
        return Point(x, y)
