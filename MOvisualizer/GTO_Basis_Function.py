from typing import List

from scipy.special import sph_harm
import math
from grid_coordinates import Grid_Coordinates

class GTO_Primitive:
    def __init__(self, coefficient: float, exponent: float):
        self.coefficient = coefficient
        self.exponent = exponent

    def calculate(self, r: float):
        return self.coefficient * math.exp(self.exponent * -pow(r, 2))


class GTO_Basis_Function:
    contractions: List[GTO_Primitive]

    def __init__(self, angular_moment_quantum_number: int, magnetic_quantum_number: int, location: Grid_Coordinates):
        assert(abs(magnetic_quantum_number) <= angular_moment_quantum_number)
        self.contractions = []
        self.angular_moment_quantum_number = angular_moment_quantum_number
        self.magnetic_quantum_number = magnetic_quantum_number
        self.location = location

    def add_contraction(self, gto_primitive: GTO_Primitive):
        self.contractions.append(gto_primitive)

    def calculate(self, global_grid_location: Grid_Coordinates):
        assert self.contractions
        #angular_part = sph_harm(abs(self.magnetic_quantum_number), self.angular_moment_quantum_number, phi, theta)
        #radial_part = functools.reduce(lambda result, primitive: result + primitive.calculate(r), self.contractions)
        #return radial_part * angular_part
        pass
