import math

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_line(self, line):
        distance = abs(line.slope * self.x - self.y + line.intercept) / math.sqrt(line.slope ** 2 + 1)
        return distance

    def is_point_on_line(self, line):
        return self.y == line.slope * self.x + line.intercept

    @staticmethod
    def distance_between_parallel_lines(line1, line2):
        distance = abs(line2.intercept - line1.intercept) / math.sqrt(line1.slope ** 2 + 1)
        return distance

    def distance_to_point(self, other):
        distance = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return distance

    @staticmethod
    def are_points_equilateral(p1, p2, p3):
        d1 = p1.distance_to_point(p2)
        d2 = p1.distance_to_point(p3)
        d3 = p2.distance_to_point(p3)
        return math.isclose(d1, d2) and math.isclose(d1, d3)

    @staticmethod
    def centroid_of_triangle(p1, p2, p3):
        centroid_x = (p1.x + p2.x + p3.x) / 3
        centroid_y = (p1.y + p2.y + p3.y) / 3
        return Coordinate(centroid_x, centroid_y)

    @staticmethod
    def area_of_triangle(p1, p2, p3):
        area = 0.5 * abs((p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y)))
        return area

    def midpoint_to(self, other):
        midpoint_x = (self.x + other.x) / 2
        midpoint_y = (self.y + other.y) / 2
        return Coordinate(midpoint_x, midpoint_y)

    def angle_to(self, other):
        angle = math.atan2(other.y - self.y, other.x - self.x)
        return math.degrees(angle)

    @staticmethod
    def intersection_of_lines(line1, line2):
        if line1.slope == line2.slope:
            raise ValueError("Lines are parallel and do not intersect.")
        x = (line2.intercept - line1.intercept) / (line1.slope - line2.slope)
        y = line1.slope * x + line1.intercept
        return Coordinate(x, y)

    @staticmethod
    def are_points_collinear(p1, p2, p3):
        return (p3.y - p1.y) * (p2.x - p1.x) == (p2.y - p1.y) * (p3.x - p1.x)

    def slope_to(self, other):
        if self.x == other.x:
            raise ValueError("Slope is undefined for vertical line.")
        return (other.y - self.y) / (other.x - self.x)

class Line:
    def __init__(self, slope, intercept):
        self.slope = slope
        self.intercept = intercept
