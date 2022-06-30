import sys
import logging
import argparse
import MOvisualizer.plot_file_generator
import MOvisualizer.Basis_Set_Loader
from MOvisualizer.geometry import Geometry,Center
from MOvisualizer.grid_coordinates import Grid_Coordinates

methane_geometry = Geometry()\
    .add_center(Center().set_atomic_number(6).set_coordinates(Grid_Coordinates().set_cartesian(0,0,0))) \
    .add_center(Center().set_atomic_number(1).set_coordinates(Grid_Coordinates().set_cartesian(0.6314,0.6314, 0.6314))) \
    .add_center(Center().set_atomic_number(1).set_coordinates(Grid_Coordinates().set_cartesian(-0.6314, -0.6314, 0.6314)))\
    .add_center(Center().set_atomic_number(1).set_coordinates(Grid_Coordinates().set_cartesian(-0.6314, 0.6314, -0.6314)))\
    .add_center(Center().set_atomic_number(1).set_coordinates(Grid_Coordinates().set_cartesian(0.6314, -0.6314, -0.6314)))

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
    basis_set = MOvisualizer.Basis_Set_Loader.Basis_Set_Loader().load(methane_geometry)
    plot.generate(basis_set, [1])


if __name__ == '__main__':
    main()
