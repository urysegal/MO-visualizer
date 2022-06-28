class Plot_File:
    def __init__(self, filename: str, delimiter: str = " ", newline: str = "\n"):
        assert isinstance(filename, str)
        self.filename = filename
        self.file_descriptor = None
        self.delimiter = delimiter
        self.newline = newline

    def open(self):
        self.file_descriptor = open(self.filename, "w")

    def add_plot_point(self, x: float, y: float, z: float, value: float):
        assert self.file_descriptor
        self.file_descriptor.write(f"{x}{self.delimiter}{y}{self.delimiter}{z}{self.delimiter}{value}{self.newline}")

    def close(self):
        assert self.file_descriptor
        self.file_descriptor.close()
