import sys
import logging
import MOvisualizer.plot_file_generator
import MOvisualizer.Basis_Set_Loader


def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.debug(f"Command line arguments: {sys.argv}")
    plot = MOvisualizer.plot_file_generator.Plot_File_Generator(5.0, 100, "/tmp/plot.txt")
    basis_set = MOvisualizer.Basis_Set_Loader.Basis_Set_Loader().load()
    plot.generate(basis_set, [1])


if __name__ == '__main__':
    main()
