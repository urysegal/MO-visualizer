from pyevtk.hl import gridToVTK
import numpy
import logging
class Plot_File:
    def __init__(self, filename: str, dimension: int):
        assert isinstance(filename, str)
        self.filename = filename
        self.dimension = dimension
        self.x = []
        self.y = []
        self.z = []
        self.value = []

    def add_plot_point(self, x: float, y: float, z: float, value: float):
        self.x.append(x)
        self.y.append(y)
        self.z.append(z)
        self.value.append(value)

    def close(self):
        pointData = numpy.array(self.value).reshape((self.dimension, self.dimension, self.dimension))
        x = numpy.array(self.x).reshape((self.dimension, self.dimension, self.dimension))
        y = numpy.array(self.y).reshape((self.dimension, self.dimension, self.dimension))
        z = numpy.array(self.z).reshape((self.dimension, self.dimension, self.dimension))
        logging.info(f"{pointData.shape}")
        gridToVTK(self.filename, x, y, z,  pointData={"value": pointData})
