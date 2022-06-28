import numpy


class Global_Grid:
    def __init__(self, radius, grid_dimension):
        assert isinstance(radius, float)
        assert isinstance(grid_dimension, int)
        self.radius = radius
        self.grid_dimension = grid_dimension
        self.theta_coordinates = numpy.linspace(0, numpy.pi, self.grid_dimension)
        self.phi_coordinates = numpy.linspace(0, 2 * numpy.pi, self.grid_dimension)
        self.cartesian_coordinates = numpy.array([numpy.sin(self.theta_coordinates) * numpy.sin(self.phi_coordinates),
                                                  numpy.sin(self.theta_coordinates) * numpy.cos(self.phi_coordinates),
                                                  numpy.cos(self.theta_coordinates)])
