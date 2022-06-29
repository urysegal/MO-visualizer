import math


class Grid_Coordinates:

    def __init__(self):
        self.r = None
        self.theta = None
        self.phi = None
        self.x = None
        self.y = None
        self.z = None

    def set_cartesian(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z
        self.recalculate_spherical()
        return self

    def recalculate_spherical(self):
        hypotenuse_squared = self.x ** 2 + self.y ** 2
        self.theta = math.atan2(self.z, math.sqrt(hypotenuse_squared))
        self.phi = math.atan2(self.y, self.x)
        self.r = math.sqrt(hypotenuse_squared + self.z ** 2)
