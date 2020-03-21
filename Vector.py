from math import sqrt

class Vector:
    
    def __init__(self, x=0, y=0, z=0):
        if type(x) == Vector:
            self.x = x.x
            self.y = x.y
            self.z = x.z
        else:
            # Default is a zero vector
            self.x = x
            self.y = y
            self.z = z

    def mag(self):
        # Length of the vector using Pythagorean theorem
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    # Vector multiplication by a scalar
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)
    __rmul__ = __mul__
    
    def __truediv__(self, scalar):
        # Division of vector by a scalar
        return self * (1/scalar)

    # Vector operations
    def __eq__(self, other):
        # Vectors are equal if the components are all equal
        return self.x == other.x and self.y == other.y and self.z == other.z

    def norm(self):
        # Return a new vector that is normalized
        return Vector(self / self.mag())

    @staticmethod
    def dotProd(v1, v2):
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

    @staticmethod
    def crossProd(v1, v2):
        x = v1.y * v2.z - v1.z * v2.y
        y = v1.z * v2.x - v1.x * v2.z
        z = v1.x * v2.y - v1.y * v2.x
        return Vector(x, y, z)

    # Display
    def __str__(self):
        return "[{0}, {1}, {2}]".format(self.x, self.y, self.z)

class Point(Vector):
    pass
