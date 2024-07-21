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

    # Instantiate a new solution object from the input string "board." The solution object will contain an array of
    # nine arrays that contain the information provided in the input string.
    solution = Solution(input_board)

    # instantiate a new game board object (requires providing the known solution object).
    my_board = Board(solution.sol_array)

    # iterate (using elimination) until the board is no longer changing
    loop_counter = 1
    change_counter = 1

    while change_counter > 0:
        change_counter = my_board.single_iteration_loop()
        # TEST ONLY #
        print(f'!!TEST ONLY!!')
        print(f'Loop Number: {loop_counter}; Change Counter: {change_counter}')
        print()
        # TEST ONLY#
        loop_counter += 1

    # if the puzzle is stagnant, there are only two possibilities, the puzzle is stuck or the puzzle is solved
    solved = True
    for group in range(1, 10):
        for cell in range(1, 10):
            cell_in_question = my_board.return_group(group).return_cell(cell)
            if cell_in_question.possibles[0] == 0:
                solved = False

    # display a message indicating whether the puzzle was solved.
    if solved:
        print(f'A solution has been found!')
    else:
        print(f'No solution was found.')

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
