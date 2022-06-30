import numpy
from MOvisualizer.grid_coordinates import Grid_Coordinates


class Global_Grid:
    def __init__(self, radius, grid_dimension):
        assert isinstance(radius, float)
        assert isinstance(grid_dimension, int)
        self.radius = radius
        self.grid_dimension = grid_dimension
        self.cartesian_coordinates = numpy.array([numpy.linspace(-radius, radius, self.grid_dimension),
                                                  numpy.linspace(-radius, radius, self.grid_dimension),
                                                  numpy.linspace(-radius, radius, self.grid_dimension)])

    def points(self):
        for x in self.cartesian_coordinates[0]:
            for y in self.cartesian_coordinates[1]:
                for z in self.cartesian_coordinates[2]:
                    yield Grid_Coordinates().set_cartesian(x, y, z)
