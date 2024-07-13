# NAME:     Display Functions
# AUTHOR:   Robert Waelchli
# DATE:     2024 04 27
# PURPOSE:  This file contains display functions for my advanced Python final project.

# imports
from group_class_definition import Group
from board_class_definition import Board


# function to print a single group divider row
def print_group_row_divider():
    print(f'+-------+-------+-------+', end='')


def print_board_row_minor_divider():
    print_group_row_divider()
    print_group_row_divider()
    print_group_row_divider()


def print_board_row_major_divider():
    print(f'+=======+=======+=======+', end='')
    print(f'+=======+=======+=======+', end='')
    print(f'+=======+=======+=======+', end='')


# function to print a single group row
def print_group_row(group_object: Group, cell_row: int, num_row: int):
    if cell_row == 1:
        cell_start = 1
        cell_end = 4
    elif cell_row == 2:
        cell_start = 4
        cell_end = 7
    else:
        cell_start = 7
        cell_end = 10

    if num_row == 1:
        num_start = 1
        num_end = 4
    elif num_row == 2:
        num_start = 4
        num_end = 7
    else:
        num_start = 7
        num_end = 10

    for cell in range(cell_start, cell_end):
        print('| ', end='')
        for number in range(num_start, num_end):
            print(f'{group_object.return_cell(cell).return_value(number)} ', end='')
    print('|', end='')


# function to print a single board row
def print_board_row(board_object: Board, board_row: int):
    if board_row == 1:
        group_start = 1
        group_end = 4
    elif board_row == 2:
        group_start = 4
        group_end = 7
    else:
        group_start = 7
        group_end = 10

    print()
    for cell_row in range(1, 4):
        for num_row in range(1, 4):
            for group_row in range(group_start, group_end):
                print_group_row(board_object.return_group(group_row), cell_row, num_row)
            print()
        if cell_row != 3:
            print_board_row_minor_divider()
            print()


# function to display an individual group including all pencil marks;
# this function is not currently used, but was used for testing
def print_full_group(group_object: Group):
    print()
    print_group_row_divider()
    print()
    print_group_row(group_object, 1, 1)
    print()
    print_group_row(group_object, 1, 2)
    print()
    print_group_row(group_object, 1, 3)
    print()
    print_group_row_divider()
    print()
    print_group_row(group_object, 2, 1)
    print()
    print_group_row(group_object, 2, 2)
    print()
    print_group_row(group_object, 2, 3)
    print()
    print_group_row_divider()
    print()
    print_group_row(group_object, 3, 1)
    print()
    print_group_row(group_object, 3, 2)
    print()
    print_group_row(group_object, 3, 3)
    print()
    print_group_row_divider()
    print()


# function to display a game board include all pencil marks
def print_full_board(board_object: Board):
    print_board_row_minor_divider()
    print_board_row(board_object, 1)
    print_board_row_major_divider()
    print_board_row(board_object, 2)
    print_board_row_major_divider()
    print_board_row(board_object, 3)
    print_board_row_minor_divider()
    print()


# function to display all the possibility arrays in a usable format
def print_full_board_array_view(board_object: Board):
    for group in range(1, 10):
        print(f'This is group {group}')
        for cell in range(1, 10):
            group_number = board_object.return_group(group)
            cell_numbers = group_number.return_cell(cell)
            print(cell_numbers.possibles)
    print()