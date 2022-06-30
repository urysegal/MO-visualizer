from MOvisualizer.grid_coordinates import Grid_Coordinates


class Center:
    def __init__(self):
        self.atomic_number = None
        self.coordinates = None

    def set_coordinates(self, coordinates: Grid_Coordinates):
        self.coordinates = coordinates
        return self

    def set_atomic_number(self, atomic_number: int):
        self.atomic_number = atomic_number
        return self

class Geometry:
    def __init__(self):
        self.all_centers = []

    def add_center(self, center: Center):
        self.centers.append(center)
        return self

    def centers(self):
        for c in self.all_centers:
            yield c
