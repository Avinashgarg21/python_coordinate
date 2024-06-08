# python_coordinate

# Coordinate Geometry Library

This library provides classes and methods for performing various geometric operations with coordinates and lines. It includes features such as distance calculations, midpoint determination, angle computations, line intersection, collinearity checks, and more.

## Features

### Coordinate Class

- **Initialization**: Create a coordinate with x and y values.
- **Distance to Line**: Calculate the perpendicular distance from a point to a line.
- **Point on Line Check**: Verify if a point lies on a given line.
- **Distance Between Parallel Lines**: Compute the distance between two parallel lines.
- **Distance to Another Point**: Calculate the distance between two points.
- **Equilateral Triangle Check**: Determine if three points form an equilateral triangle.
- **Centroid of Triangle**: Find the centroid of a triangle formed by three points.
- **Area of Triangle**: Calculate the area of a triangle formed by three points.
- **Midpoint Calculation**: Compute the midpoint between two points.
- **Angle Calculation**: Calculate the angle between two points with respect to the x-axis.
- **Line Intersection**: Find the intersection point of two lines.
- **Collinearity Check**: Verify if three points are collinear.
- **Slope Calculation**: Calculate the slope between two points.

### Line Class

- **Initialization**: Create a line with a given slope and intercept.

## Classes and Methods

### Coordinate

#### Initialization

```python
Coordinate(x, y)
# Creates a coordinate with the given x and y values.

distance_to_line(line)
# Calculates the perpendicular distance from the point to a line.

is_point_on_line(line)
# Checks if the point lies on the given line.

@staticmethod
distance_between_parallel_lines(line1, line2)
# Computes the distance between two parallel lines.

distance_to_point(other)
# Calculates the distance between the current point and another point.

@staticmethod
are_points_equilateral(p1, p2, p3)
# Determines if three points form an equilateral triangle.

@staticmethod
centroid_of_triangle(p1, p2, p3)
# Calculates the area of a triangle formed by three points.

@staticmethod
area_of_triangle(p1, p2, p3)
# Calculates the area of a triangle formed by three points.

midpoint_to(other)
# Computes the midpoint between the current point and another point.

angle_to(other)
# Calculates the angle between the current point and another point.

@staticmethod
intersection_of_lines(line1, line2)
# Finds the intersection point of two lines.

@staticmethod
are_points_collinear(p1, p2, p3)
# Checks if three points are collinear.

slope_to(other)
# Calculates the slope between the current point and another point.

Line(slope, intercept)
# Creates a line with the given slope and intercept.
