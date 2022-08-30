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
                           rectangle_point_a: Point,
                           rectangle_point_b: Point) -> Point:
    """
    A function to check that the intersection point is within the range of points.
    code taken from:
    https://www.geeksforgeeks.org/program-for-point-of-intersection-of-two-lines/
    :param line_start: The line start point.
    :param line_end: The line end point.
    :param rectangle_point_a: a point of the rectangle edge.
    :param rectangle_point_b: b point of the rectangle edge.
    :return: Intersection point if the intersection within the range of points, (FLT_MAX, FLT_MAX) else.
    """
    left_point, right_point = rectangle_point_a, rectangle_point_b
    if rectangle_point_a.get_x() > rectangle_point_b.get_x():
        left_point, right_point = rectangle_point_b, rectangle_point_a

    # Line AB represented as a1x + b1y = c1
    a1 = line_end.get_y() - line_start.get_y()
    b1 = line_start.get_x() - line_end.get_x()
    c1 = a1 * line_start.get_x() + b1 * line_start.get_y()

    # Line CD represented as a2x + b2y = c2
    a2 = rectangle_point_b.get_y() - rectangle_point_a.get_y()
    b2 = rectangle_point_a.get_x() - rectangle_point_b.get_x()
    c2 = a2 * rectangle_point_a.get_x() + b2 * rectangle_point_a.get_y()

    determinant = a1 * b2 - a2 * b1

    if determinant == 0:
        # The lines are parallel. This is simplified
        # by returning a pair of FLT_MAX
        return Point(FLT_MAX, FLT_MAX)
    else:
        x = (b2 * c1 - b1 * c2) / determinant
        y = (a1 * c2 - a2 * c1) / determinant
        if x < left_point.get_x() or x > right_point.get_x():
            return Point(FLT_MAX, FLT_MAX)
        return Point(x, y)
