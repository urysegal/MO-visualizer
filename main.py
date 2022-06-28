import sys
import logging

def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.debug(f"Command line arguments: {sys.argv}")

if __name__ == '__main__':
    main()
