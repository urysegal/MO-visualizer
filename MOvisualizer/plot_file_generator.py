from typing import List
import MOvisualizer.global_grid
import MOvisualizer.plot_file
from MOvisualizer import GTO_Basis_Set
import logging


class Plot_File_Generator:
    def __init__(self, radius: float, grid_dimension: int, filename: str):
        self.global_grid = MOvisualizer.global_grid.Global_Grid(radius, grid_dimension)
        self.plot_file = MOvisualizer.plot_file.Plot_File(filename)

    def generate(self, basis_set: GTO_Basis_Set.GTO_Basis_Set, coefficients: List[float]):
        self.plot_file.open()
        for point in self.global_grid.points():
            logging.debug(f"{point.x} {point.y} {point.z} {point.phi} {point.r} {point.theta}")
            val = basis_set.calculate(coefficients, point)
            self.plot_file.add_plot_point(point.x, point.y, point.z, val)
        self.plot_file.close()
