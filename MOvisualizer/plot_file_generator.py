from typing import List
import MOvisualizer.global_grid
import MOvisualizer.plot_file
from MOvisualizer import GTO_Basis_Set


class Plot_File_Generator:
    def __init__(self, radius: float, grid_dimension: int, filename: str):
        self.global_grid = MOvisualizer.global_grid.Global_Grid(radius, grid_dimension)
        self.plot_file = MOvisualizer.plot_file.Plot_File(filename)

    def generate(self, basis_set: GTO_Basis_Set.GTO_Basis_Set, coefficients: List[float]):
        pass
