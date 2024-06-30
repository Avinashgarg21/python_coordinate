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
```
```
Coordinate(x, y)
#### Creates a coordinate with the given x and y values.

distance_to_line(line)
#### Calculates the perpendicular distance from the point to a line.

is_point_on_line(line)
#### Checks if the point lies on the given line.

@staticmethod
distance_between_parallel_lines(line1, line2)
#### Computes the distance between two parallel lines.

distance_to_point(other)
#### Calculates the distance between the current point and another point.

@staticmethod
are_points_equilateral(p1, p2, p3)
#### Determines if three points form an equilateral triangle.

@staticmethod
centroid_of_triangle(p1, p2, p3)
#### Calculates the area of a triangle formed by three points.

@staticmethod
area_of_triangle(p1, p2, p3)
#### Calculates the area of a triangle formed by three points.

midpoint_to(other)
#### Computes the midpoint between the current point and another point.

angle_to(other)
#### Calculates the angle between the current point and another point.

@staticmethod
intersection_of_lines(line1, line2)
#### Finds the intersection point of two lines.

@staticmethod
are_points_collinear(p1, p2, p3)
#### Checks if three points are collinear.


slope_to(other)
#### Calculates the slope between the current point and another point.

Line(slope, intercept)
#### Creates a line with the given slope and intercept.

## Installation

1. **Download the Library**

   Download the `coordinate.py` file from the repository or copy the code into a file named `coordinate.py`.

2. **Include the Library in Your Project**

   Place the `coordinate.py` file in your project directory.

## Usage

1. **Import the Library**

   In your Python script, import the `Coordinate` and `Line` classes from the `coordinate` module:

   ```python
   from coordinate import Coordinate, Line

### Here's a complete example demonstrating the usage of the Coordinate and Line classes with the appropriate comments:
```python
from coordinate import Coordinate, Line

# Create coordinates
point1 = Coordinate(3, 4)
point2 = Coordinate(6, 8)
point3 = Coordinate(9, 12)

# Create a line
line = Line(2, 3)  # y = 2x + 3

# Calculate and print various geometric properties
distance_to_line = point1.distance_to_line(line)
print(f"Distance from point to line: {distance_to_line}")

is_on_line = point1.is_point_on_line(line)
print(f"Is the point on the line? {is_on_line}")

distance_between_points = point1.distance_to_point(point2)
print(f"Distance between points: {distance_between_points}")

is_equilateral = Coordinate.are_points_equilateral(point1, point2, point3)
print(f"Are the points equilateral? {is_equilateral}")

centroid = Coordinate.centroid_of_triangle(point1, point2, point3)
print(f"Centroid of the triangle: ({centroid.x}, {centroid.y})")

area = Coordinate.area_of_triangle(point1, point2, point3)
print(f"Area of the triangle: {area}")

# Calculate distance between parallel lines
line1 = Line(1, 2)  # y = x + 2
line2 = Line(1, 5)  # y = x + 5
distance_between_lines = Coordinate.distance_between_parallel_lines(line1, line2)
print(f"Distance between parallel lines: {distance_between_lines}")


