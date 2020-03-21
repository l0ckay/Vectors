from Vector import *

class Plane:

    def __init__(self, a, b, c, d):
        # Plane in form ax + by + cz + d = 0
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    @staticmethod
    def planeThrough3Points(p1, p2, p3):
        v1_2 = p2 - p1
        v1_3 = p3 - p1
        abc = Vector.crossProd(v1_2, v1_3)
        d = Vector.dotProd(p1, abc)

        return Plane(abc.x, abc.y, abc.z, d)

    # Override
    def __str__(self):
        return "{0}x + {1}y + {2}z + {3} = 0".format(self.a, self.b, self.c, self.d)
