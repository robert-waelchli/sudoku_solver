# NAME:     Sudoku Cell Class Definition File
# AUTHOR:   Robert Waelchli
# DATE:     2024 04 27
# PURPOSE:  This file only defines a Cell class. This file is part of Sudoku Pencil Marker Version 1.0.

class Cell:
    def __init__(self, position: int, address_list: list):      # constructor
        self.position = position                                # position on Sudoku board
        self.group_address = address_list[0]                    # "group" list address for this cell
        self.row_address = address_list[1]                      # "row" list address for this cell
        self.col_address = address_list[2]                      # "col" list address for this cell
        self.groups = []                                        # list of already taken group values
        self.rows = []                                          # list of already taken row values
        self.columns = []                                       # list of already taken column values
        self.possibles = [0, 1, 2, 3, 4,                        # overall possibility array, where first digit serves as a boolean flag
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

    # method by which group, row, or column array values are eliminated
    def eliminate_cell_vals(self, input_list: list, input_type: str, optional_counter: int = 0):
        # if the cell hasn't already been solved proceed, otherwise skip this cell
        if self.possibles[0] == 0:
            match input_type:
                case 'group':
                    elimination_array = self.groups
                case 'row':
                    elimination_array = self.rows
                case _:
                    elimination_array = self.columns

            # update the counter, the appropriate array (groups, rows, columns) and the possibles array if needed
            for item in input_list:
                if item not in elimination_array:
                    optional_counter += 1
                    elimination_array.append(item)
                    elimination_array.sort()
                    if item in self.possibles:
                        index = self.possibles.index(item)
                        self.possibles[index] = 0

        # return the option counter if one was provided
        return optional_counter

    def check_and_solve_if_lone_value(self, optional_counter: int = 0):
        posibilites_list = []
        for character in self.possibles:
            if (str(character).isnumeric()) and (character != 0):
                posibilites_list.append(int(character))
        if len(posibilites_list) == 1:
            optional_counter += 1
            self.solve_cell(posibilites_list[0])

        # return the optional counter if one was privided
        return optional_counter

    def __repr__(self):
        print(f'Cell({self.position}, {self.possibles})')
