from MOvisualizer import GTO_Basis_Function
from MOvisualizer import GTO_Basis_Set


class Basis_Set_Loader:

    def __init__(self):
        self.basis_set = GTO_Basis_Set.GTO_Basis_Set()

    def load(self):
        func = GTO_Basis_Function.GTO_Basis_Function(0, 0)
        primitive = GTO_Basis_Function.GTO_Primitive(0.5, 0.8)
        func.add_contraction(primitive)
        self.basis_set.append(func)
        return self.basis_set
