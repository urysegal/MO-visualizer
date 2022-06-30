import sys
import logging
import argparse
import MOvisualizer.plot_file_generator
import MOvisualizer.Basis_Set_Loader
from MOvisualizer.geometry import Geometry, Center
from MOvisualizer.grid_coordinates import Grid_Coordinates

geometry = Geometry()
methane_info = [
    [6, 0.0000, 0.0000, 0.0000],
    [1, 0.6314, 0.6314, 0.6314],
    [1, -0.6314, -0.6314, 0.6314],
    [1, -0.6314, 0.6314, -0.6314],
    [1, 0.6314, -0.6314, -0.6314]
]

for c in methane_info:
    geometry.add_center(
        Center().set_atomic_number(c[0]).set_coordinates(Grid_Coordinates().set_cartesian(c[1], c[2], c[3])))


def main():
    logging.basicConfig(level=logging.INFO)
    logging.info(f"Command line arguments: {sys.argv}")
    parser = argparse.ArgumentParser()
    parser.add_argument("radius", help="radius of volume around origin to display",
                        type=float)
    parser.add_argument("grid", help="number of axis subdivisions",
                        type=int)
    parser.add_argument("output_file", help="output file name",
                        type=str)
    args = parser.parse_args()
    plot = MOvisualizer.plot_file_generator.Plot_File_Generator(args.radius, args.grid, args.output_file)
    basis_set = MOvisualizer.Basis_Set_Loader.Basis_Set_Loader().load(geometry)
    plot.generate(basis_set, [1])


if __name__ == '__main__':
    main()
