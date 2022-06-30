from MOvisualizer import GTO_Basis_Function
from MOvisualizer import GTO_Basis_Set
from MOvisualizer.grid_coordinates import Grid_Coordinates
from MOvisualizer.geometry import Geometry


class Basis_Set_Loader:

    def __init__(self):
        self.basis_set = GTO_Basis_Set.GTO_Basis_Set()

    def load(self, geometry: Geometry):
        for center in geometry.centers():
            self.load_sto3g(center.coordinates, center.atomic_number)
        return self.basis_set

    def load_sto3g(self, center: Grid_Coordinates, atomic_number: int):
        if atomic_number == 1:
            self.load_sto3g_hydrogen(center)
        elif atomic_number == 6:
            self.load_sto3g_carbon(center)
        else:
            raise RuntimeError(f"Atoms with atomic number {atomic_number} not supported")

        return self.basis_set

    def load_s_orbital(self, center: Grid_Coordinates, parameters):
        func = GTO_Basis_Function.GTO_Basis_Function(0, 0, center)
        for primitive in parameters:
            func.add_contraction(GTO_Basis_Function.GTO_Primitive(primitive[0], primitive[1]))
        self.basis_set.append(func)

    def load_p_orbital(self, center: Grid_Coordinates, parameters):
        for magnetic_principal_number in [-1, 0, 1]:
            func = GTO_Basis_Function.GTO_Basis_Function(1, magnetic_principal_number, center)
            for primitive in parameters:
                func.add_contraction(GTO_Basis_Function.GTO_Primitive(primitive[0], primitive[1]))
            self.basis_set.append(func)

    def load_sto3g_hydrogen(self, center: Grid_Coordinates):
        hydrogen_s_primitives = [
            [0.3425250914E+01, 0.1543289673E+00],
            [0.6239137298E+00, 0.5353281423E+00],
            [0.1688554040E+00, 0.4446345422E+00]
        ]
        self.load_s_orbital(center, hydrogen_s_primitives)

    def load_sto3g_carbon(self, center: Grid_Coordinates):
        carbon_s_primitives = [
            [
                [0.7161683735E+02, 0.1543289673E+00],
                [0.1304509632E+02, 0.5353281423E+00],
                [0.3530512160E+01, 0.4446345422E+00]
            ],
            [
                [0.2941249355E+01, -0.9996722919E-01],
                [0.6834830964E+00, 0.3995128261E+00],
                [0.2222899159E+00, 0.7001154689E+00]
            ]
        ]

        for prims in carbon_s_primitives:
            self.load_s_orbital(center, prims)

        carbon_p_primitives = [
            [0.2941249355E+01, 0.1559162750E+00],
            [0.6834830964E+00, 0.6076837186E+00],
            [0.2222899159E+00, 0.3919573931E+00]
        ]

        self.load_p_orbital(center, carbon_p_primitives)
