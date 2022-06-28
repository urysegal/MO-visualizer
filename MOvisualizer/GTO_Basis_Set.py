from typing import List

from MOvisualizer import GTO_Basis_Function


class GTO_Basis_Set:
    def __init__(self):
        self.functions = []

    def append(self, f: GTO_Basis_Function):
        self.functions.append(f)

    def calculate(self, coefficients: List[float], phi: float, theta: float, r: float):
        assert len(coefficients) == len(self.functions)
        result = float(0)
        for function_index in range(0, len(coefficients)):
            result += coefficients[function_index] * self.functions[function_index].calculate(phi, theta, r)
        return result
