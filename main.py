# PROGRAM:  Sudoku Solver Version 1.0
# AUTHOR:   Robert Waelchli
# DATE:     2024 06 23
# PURPOSE:  This program takes a Sudoku game board as input and returns a solution. This program borrows some code
#           written initially as partial fulfillment of a final project requirement for Advanced Python, CSC 2017 X40.

# !/usr/bin/env python3

# imports
from board_class_definition import Board
from solution_class_definition import Solution
import display_functions as display


# main function if run as main
def main():

    # display a title
    print("\nSudoku Solver Version 1.0")
    print("*************************")
    print()

    # board input
    input_board = (
                 '| 5 . 9 | 2 . . | . 1 . |\n'
                 '| 4 . . | 1 . . | . 8 5 |\n'
                 '| . . 1 | 8 . 5 | . 9 . |\n'
                 '+-------+-------+-------+\n'
                 '| 7 5 6 | . . . | . . 1 |\n'
                 '| . . 3 | . 1 6 | 8 . . |\n'
                 '| . . . | 3 7 . | 5 . 6 |\n'
                 '+-------+-------+-------+\n'
                 '| . 7 . | . . 4 | 2 . 8 |\n'
                 '| 3 6 . | . 5 . | . . . |\n'
                 '| . 4 . | . 8 . | 3 5 . |\n'
                 )

    # display the board as entered
    print(f'This is the board as entered: \n{input_board}')

    # instantiate a new solution object and use the definition method to populate the solution--once
    # populated, the solution object will contain an array of nine arrays that contain the information
    # provided in the input string.
    solution = Solution(input_board)

    # instantiate a new game board object
    my_board = Board()

    # update the game board with known values provided in the solution object
    my_board.apply_solution(solution)

    # for group in range(1, 10):
    #     for cell in range(1, 10):
    #         cell_in_question = my_board.return_group(group).return_cell(cell)
    #         print(f'Group: {group} Cell: {cell} Group Address: {cell_in_question.group_address}, Row: {cell_in_question.row_address}, Col: {cell_in_question.col_address}')

    # iterate one loop, counting the changes
    change_counter = my_board.single_iteration_loop()
    print(f'Change Counter: {change_counter}')
    print()

    # if no changes took place, exit the loop, else repeat

    # print the output game board including the pencil marks
    print()
    print(f'This is the final board including all pencil marks:')
    display.print_full_board(my_board)

    # print a goodbye message and terminate the program
    print()
    print("End of program. Bye!")


# if started in the main module, call the main() function
if __name__ == "__main__":
    main()
