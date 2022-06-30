import sys
import logging
import argparse
import MOvisualizer.plot_file_generator
import MOvisualizer.Basis_Set_Loader


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
    basis_set = MOvisualizer.Basis_Set_Loader.Basis_Set_Loader().load()
    plot.generate(basis_set, [1])


if __name__ == '__main__':
    main()
