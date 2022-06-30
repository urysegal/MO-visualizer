import logging
from typing import List

from MOvisualizer import GTO_Basis_Function
from MOvisualizer.grid_coordinates import Grid_Coordinates


class GTO_Basis_Set:
    def __init__(self):
        self.functions = []

    def append(self, f: GTO_Basis_Function):
        self.functions.append(f)

    def calculate(self, coefficients: List[float], coordinates: Grid_Coordinates):
        logging.info(f"{len(self.functions)} basis functions")
        assert len(coefficients) == len(self.functions)
        result = float(0)
        for function_index in range(0, len(coefficients)):
            result += coefficients[function_index] * self.functions[function_index].calculate(coordinates)
        return result
