

from openpyxl import NUMPY


def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    reader = reader(csv_file_path)
    matrix = None
    first_row = True
    for row_index, row in enumerate(reader):
        if first_row:
            size = len(row)
            matrix = NUMPY.zeros((size, size), dtype=int)
            first_row = False
            # matrix[row_index] = [int(item) for item in row]
        matrix[row_index] = row

    return matrix