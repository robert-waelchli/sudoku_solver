# NAME:     Sudoku Board Class Definition File
# AUTHOR:   Robert Waelchli
# DATE:     2024 04 27
# PURPOSE:  This file only defines a Board class made up of nine groups. This file is part of Sudoku Pencil Marker
#           Version 1.0.

# imports
from group_class_definition import Group
from solution_class_definition import Solution


class Board:
    def __init__(self):                 # constructor
        self.group1: Group = Group(1)   # Group in board position 1
        self.group2: Group = Group(2)   # Group in board position 2
        self.group3: Group = Group(3)   # Group in board position 3
        self.group4: Group = Group(4)   # Group in board position 4
        self.group5: Group = Group(5)   # Group in board position 5
        self.group6: Group = Group(6)   # Group in board position 6
        self.group7: Group = Group(7)   # Group in board position 7
        self.group8: Group = Group(8)   # Group in board position 8
        self.group9: Group = Group(9)   # Group in board position 9

    # method returns the group object from the indicated position
    def return_group(self, position: int):
        if position == 1:
            group = self.group1
        elif position == 2:
            group = self.group2
        elif position == 3:
            group = self.group3
        elif position == 4:
            group = self.group4
        elif position == 5:
            group = self.group5
        elif position == 6:
            group = self.group6
        elif position == 7:
            group = self.group7
        elif position == 8:
            group = self.group8
        else:
            group = self.group9

        return group

    # method applies a given solution object to the game board, cell-by-cell
    def apply_solution(self, solution: Solution):
        for group in range(1, 10):
            for cell in range(1, 10):
                cell_to_modify = self.return_group(group).return_cell(cell)
                # solve the cell if the value is already known
                if solution.sol_array[group - 1][cell - 1] != 0:
                    cell_to_modify.solve_cell(solution.sol_array[group - 1][cell - 1])
                else:
                    # if cell value is not already know, eliminate values as possibilities in the cell object
                    for number in range(0, 3):
                        array_type = ['group', 'row', 'col']
                        array_string = array_type[number]
                        cell_to_modify.eliminate_cell_vals(solution.list_of_lists_by_location[group - 1][cell - 1]
                                                           [number], array_string)

    def __repr__(self):
        print(f'Board()')
