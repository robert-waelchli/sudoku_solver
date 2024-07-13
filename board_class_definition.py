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
        solution.rows_to_groups_and_back()
        for group in range(1, 10):
            for cell in range(1, 10):
                if solution.sol_array[group - 1][cell - 1] != 0:
                    self.return_group(group).return_cell(cell).solve_cell(solution.sol_array[group - 1][cell - 1])
        solution.rows_to_groups_and_back()

    # method by which pencil marks are updated, row-by-row
    def reduce_rows(self, solution: Solution):
        def reducer(group_start: int, cell_start: int, array_number: int):
            for group in range(group_start, group_start + 3):
                for cell in range(cell_start, cell_start + 3):
                    self.return_group(group).return_cell(cell).reduce_values(solution.sol_array[array_number])

        reducer(1, 1, 0)
        reducer(1, 4, 1)
        reducer(1, 7, 2)
        reducer(4, 1, 3)
        reducer(4, 4, 4)
        reducer(4, 7, 5)
        reducer(7, 1, 6)
        reducer(7, 4, 7)
        reducer(7, 7, 8)

    # method by which pencil marks are updated, column-by-column
    def reduce_columns(self, solution: Solution):
        def reducer(group_start: int, cell_start: int, array_number: int):
            for group in range(group_start, group_start + 7, 3):
                for cell in range(cell_start, cell_start + 7, 3):
                    self.return_group(group).return_cell(cell).reduce_values(solution.sol_array[array_number])

        solution.rows_to_cols_and_back()
        reducer(1, 1, 0)
        reducer(1, 2, 1)
        reducer(1, 3, 2)
        reducer(2, 1, 3)
        reducer(2, 2, 4)
        reducer(2, 3, 5)
        reducer(3, 1, 6)
        reducer(3, 2, 7)
        reducer(3, 3, 8)
        solution.rows_to_cols_and_back()

    # method by which pencil marks are updated, group-by-group
    def reduce_groups(self, solution: Solution):
        solution.rows_to_groups_and_back()
        for group in range(1, 10):
            for cell in range(1, 10):
                self.return_group(group).return_cell(cell).reduce_values(solution.sol_array[group - 1])
        solution.rows_to_groups_and_back()

    def __repr__(self):
        print(f'Board()')
