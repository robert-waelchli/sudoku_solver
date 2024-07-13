# NAME:     Sudoku Cell Class Definition File
# AUTHOR:   Robert Waelchli
# DATE:     2024 04 27
# PURPOSE:  This file only defines a Cell class. This file is part of Sudoku Pencil Marker Version 1.0.

class Cell:
    def __init__(self, position):               # constructor
        self.position: int = position           # position on Sudoku board
        self.rows = [0, 1, 2, 3, 4,             # other row possibilities (based on other row values)
                     5, 6, 7, 8, 9]
        self.columns = [0, 1, 2, 3, 4,          # other column possibilities (based on other column values)
                        5, 6, 7, 8, 9]
        self.groups = [0, 1, 2, 3, 4,           # other group possibilities (based on other group values)
                       5, 6, 7, 8, 9]
        self.possibles = [0, 1, 2, 3, 4,        # overall possibility array, where first digit serves as a boolean flag
                          5, 6, 7, 8, 9]

    # method to return the value--either an int or a dash--from a given cell location
    def return_value(self, position: int):
        value = 0
        if self.possibles[position] == 0:
            value = '-'
        else:
            value = str(self.possibles[position])

        return value

    # solving method that sets cell's final value
    def solve_cell(self, solution: int):
        # when solved all the pencil marks become empty spaces and the first element = 1 (boolean flag)
        self.possibles = [1, ' ', ' ', ' ', ' ', solution, ' ', ' ', ' ', ' ']

    # method by which pencil marks are updated
    # values in the list argument are replaced with zeros in the possibles array, already solved arrays are ignored
    def reduce_values(self, values: list):
        for value in values:
            if self.possibles[0] == 0:
                if value in self.possibles:
                    index = self.possibles.index(value)
                    self.possibles[index] = 0

    def __repr__(self):
        print(f'Cell({self.position}, {self.possibles})')
