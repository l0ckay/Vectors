from Vector import *
from Plane import *

# Example of a plane through 3 points
A = Point(1, 2, 0)
B = Point(3, -5, -2)
C = Point(1, -1, 4)

p = Plane.planeThrough3Points(A, B, C)

print(p)
