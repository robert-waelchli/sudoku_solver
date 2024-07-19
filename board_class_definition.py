# NAME:     Sudoku Board Class Definition File
# AUTHOR:   Robert Waelchli
# DATE:     2024 04 27
# PURPOSE:  This file only defines a Board class made up of nine groups. This file is part of Sudoku Pencil Marker
#           Version 1.0.

# imports
from group_class_definition import Group
from solution_class_definition import Solution
from summary_board_definition import SummaryBoard


class Board:
    def __init__(self):                 # constructor
        def provide_cell_address(group: int, cell: int, ):
            lookup = [
                [[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 1], [1, 2, 2], [1, 2, 3], [1, 3, 1], [1, 3, 2], [1, 3, 3]],
                [[2, 1, 4], [2, 1, 5], [2, 1, 6], [2, 2, 4], [2, 2, 5], [2, 2, 6], [2, 3, 4], [2, 3, 5], [2, 3, 6]],
                [[3, 1, 7], [3, 1, 8], [3, 1, 9], [3, 2, 7], [3, 2, 8], [3, 2, 9], [3, 3, 7], [3, 3, 8], [3, 3, 9]],
                [[4, 4, 1], [4, 4, 2], [4, 4, 3], [4, 5, 1], [4, 5, 2], [4, 5, 3], [6, 6, 1], [4, 6, 2], [4, 6, 3]],
                [[5, 4, 4], [5, 4, 5], [5, 4, 6], [5, 5, 4], [5, 5, 5], [5, 5, 6], [5, 6, 4], [5, 6, 5], [5, 6, 6]],
                [[6, 4, 7], [6, 4, 8], [6, 4, 9], [6, 5, 7], [6, 5, 8], [6, 5, 9], [6, 6, 7], [6, 6, 8], [6, 6, 9]],
                [[7, 7, 1], [7, 7, 2], [7, 7, 3], [7, 8, 1], [7, 8, 2], [7, 8, 3], [7, 9, 1], [7, 9, 2], [7, 9, 3]],
                [[8, 7, 4], [8, 7, 5], [8, 7, 6], [8, 8, 4], [8, 8, 5], [8, 8, 6], [8, 9, 4], [8, 9, 5], [8, 9, 6]],
                [[9, 7, 7], [9, 7, 8], [9, 7, 9], [9, 8, 7], [9, 8, 8], [9, 8, 9], [9, 9, 7], [9, 9, 8], [9, 9, 9]]]

            return lookup[group - 1][cell - 1]

        def welcome_gift(group: int):
            birth_information = []
            for cell in range(1, 10):
                birth_information.append(provide_cell_address(group, cell))

            return birth_information

        self.group1: Group = Group(1, welcome_gift(1))     # Group in board position 1
        self.group2: Group = Group(2, welcome_gift(2))     # Group in board position 2
        self.group3: Group = Group(3, welcome_gift(3))     # Group in board position 3
        self.group4: Group = Group(4, welcome_gift(4))     # Group in board position 4
        self.group5: Group = Group(5, welcome_gift(5))     # Group in board position 5
        self.group6: Group = Group(6, welcome_gift(6))     # Group in board position 6
        self.group7: Group = Group(7, welcome_gift(7))     # Group in board position 1
        self.group8: Group = Group(8, welcome_gift(8))     # Group in board position 1
        self.group9: Group = Group(9, welcome_gift(9))     # Group in board position 1
        self.summary = SummaryBoard()                             # List of lists, "big picture" game board

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
        self.summary.summary_board = solution.sol_array

    # method does four things:
    #   1. solves any cells that can only be a single value
    #   2. updates the group lists for the latest values
    #   3. updates the row lists for the latest values
    #   4. updates the column lists for the latest values
    #   5. returns a counter showing how many changes were made during the loop
    def single_iteration_loop(self):
        counter = 0

        # first, solve for any cells that can only be a single value, then update the board overview
        for group in range(1, 10):
            for cell in range(1, 10):
                cell_in_question = self.return_group(group).return_cell(cell)
                counter = cell_in_question.check_and_solve_if_lone_value(counter)
                if (self.summary.summary_board[group - 1][cell - 1] == 0) and (cell_in_question.possibles[0] == 1):
                    self.summary.summary_board[group - 1][cell - 1] = cell_in_question.possibles[5]

        # second, update the group, row, and column lists at each location (counting changes)
        for group in range(1, 10):
            for cell in range(1, 10):
                # return the specific cell to update
                cell_in_question = self.return_group(group).return_cell(cell)

                # use the latest summary board to obtain the correct group, row, and column lists for each cell
                group_list = self.summary.query_board_by_group(cell_in_question.group_address)
                row_list = self.summary.query_board_by_row(cell_in_question.row_address)
                column_list = self.summary.query_board_by_col(cell_in_question.col_address)

                # update the cell values to reflect changes
                counter = cell_in_question.eliminate_cell_vals(group_list, 'group', counter)
                counter = cell_in_question.eliminate_cell_vals(row_list, 'row', counter)
                counter = cell_in_question.eliminate_cell_vals(column_list, 'column', counter)

        return counter

    def __repr__(self):
        print(f'Board()')
