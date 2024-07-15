# NAME:     Solution Class Definition File
# AUTHOR:   Robert Waelchli
# DATE:     2024 04 28
# PURPOSE:  This file only defines a Solution class. This file is part of Sudoku Pencil Marker Version 1.0.

class Solution:
    def __init__(self, input_sol: str):                             # constructor
        self.sol_array = [[], [], [], [], [], [], [], [], []]
        self.list_of_lists_by_location = []
        self.define_solution_from_string(input_sol)
        self.define_list_of_lists()

    # method returns a solution array but formatted by rows (as opposed to groups)
    def solution_array_row_format(self):
        [aa, ab, ac, ba, bb, bc, ca, cb, cc] = self.sol_array[0]
        [ad, ae, af, bd, be, bf, cd, ce, cf] = self.sol_array[1]
        [ag, ah, aj, bg, bh, bj, cg, ch, cj] = self.sol_array[2]
        [da, db, dc, ea, eb, ec, fa, fb, fc] = self.sol_array[3]
        [dd, de, df, ed, ee, ef, fd, fe, ff] = self.sol_array[4]
        [dg, dh, dj, eg, eh, ej, fg, fh, fj] = self.sol_array[5]
        [ga, gb, gc, ha, hb, hc, ja, jb, jc] = self.sol_array[6]
        [gd, ge, gf, hd, he, hf, jd, je, jf] = self.sol_array[7]
        [gg, gh, gj, hg, hh, hj, jg, jh, jj] = self.sol_array[8]

        new_array = [[], [], [], [], [], [], [], [], []]

        new_array[0] = [aa, ab, ac, ad, ae, af, ag, ah, aj]
        new_array[1] = [ba, bb, bc, bd, be, bf, bg, bh, bj]
        new_array[2] = [ca, cb, cc, cd, ce, cf, cg, ch, cj]
        new_array[3] = [da, db, dc, dd, de, df, dg, dh, dj]
        new_array[4] = [ea, eb, ec, ed, ee, ef, eg, eh, ej]
        new_array[5] = [fa, fb, fc, fd, fe, ff, fg, fh, fj]
        new_array[6] = [ga, gb, gc, gd, ge, gf, gg, gh, gj]
        new_array[7] = [ha, hb, hc, hd, he, hf, hg, hh, hj]
        new_array[8] = [ja, jb, jc, jd, je, jf, jg, jh, jj]

        return new_array

    # method returns a solution array but formatted by columns (as opposed to groups)
    def solution_array_column_format(self):
        [aa, ba, ca, ab, bb, cb, ac, bc, cc] = self.sol_array[0]
        [da, ea, fa, db, eb, fb, dc, ec, fc] = self.sol_array[1]
        [ga, ha, ja, gb, hb, jb, gc, hc, jc] = self.sol_array[2]
        [ad, bd, cd, ae, be, ce, af, bf, cf] = self.sol_array[3]
        [dd, ed, fd, de, ee, fe, df, ef, ff] = self.sol_array[4]
        [gd, hd, jd, ge, he, je, gf, hf, jf] = self.sol_array[5]
        [ag, bg, cg, ah, bh, ch, aj, bj, cj] = self.sol_array[6]
        [dg, eg, fg, dh, eh, fh, dj, ej, fj] = self.sol_array[7]
        [gg, hg, jg, gh, hh, jh, gj, hj, jj] = self.sol_array[8]

        new_array = [[], [], [], [], [], [], [], [], []]

        new_array[0] = [aa, ab, ac, ad, ae, af, ag, ah, aj]
        new_array[1] = [ba, bb, bc, bd, be, bf, bg, bh, bj]
        new_array[2] = [ca, cb, cc, cd, ce, cf, cg, ch, cj]
        new_array[3] = [da, db, dc, dd, de, df, dg, dh, dj]
        new_array[4] = [ea, eb, ec, ed, ee, ef, eg, eh, ej]
        new_array[5] = [fa, fb, fc, fd, fe, ff, fg, fh, fj]
        new_array[6] = [ga, gb, gc, gd, ge, gf, gg, gh, gj]
        new_array[7] = [ha, hb, hc, hd, he, hf, hg, hh, hj]
        new_array[8] = [ja, jb, jc, jd, je, jf, jg, jh, jj]

        return new_array

    # method converts an input string solution into an array of arrays
    def define_solution_from_string(self, input_sol: str):
        def rows_to_groups(sol_array):
            [aa, ab, ac, ba, bb, bc, ca, cb, cc] = sol_array[0]
            [ad, ae, af, bd, be, bf, cd, ce, cf] = sol_array[1]
            [ag, ah, aj, bg, bh, bj, cg, ch, cj] = sol_array[2]
            [da, db, dc, ea, eb, ec, fa, fb, fc] = sol_array[3]
            [dd, de, df, ed, ee, ef, fd, fe, ff] = sol_array[4]
            [dg, dh, dj, eg, eh, ej, fg, fh, fj] = sol_array[5]
            [ga, gb, gc, ha, hb, hc, ja, jb, jc] = sol_array[6]
            [gd, ge, gf, hd, he, hf, jd, je, jf] = sol_array[7]
            [gg, gh, gj, hg, hh, hj, jg, jh, jj] = sol_array[8]

            sol_array[0] = [aa, ab, ac, ad, ae, af, ag, ah, aj]
            sol_array[1] = [ba, bb, bc, bd, be, bf, bg, bh, bj]
            sol_array[2] = [ca, cb, cc, cd, ce, cf, cg, ch, cj]
            sol_array[3] = [da, db, dc, dd, de, df, dg, dh, dj]
            sol_array[4] = [ea, eb, ec, ed, ee, ef, eg, eh, ej]
            sol_array[5] = [fa, fb, fc, fd, fe, ff, fg, fh, fj]
            sol_array[6] = [ga, gb, gc, gd, ge, gf, gg, gh, gj]
            sol_array[7] = [ha, hb, hc, hd, he, hf, hg, hh, hj]
            sol_array[8] = [ja, jb, jc, jd, je, jf, jg, jh, jj]

            return sol_array

        # start by removing all '+', '-', and '\n' characters
        input_sol = input_sol.replace('+', "")
        input_sol = input_sol.replace('-', "")
        input_sol = input_sol.replace('\n', "")

        # then crawl through the string and store the relevant characters as integer arrays
        start_index = 0
        end_index = 25
        for array_index in range(0, 9):
            for character in input_sol[start_index:end_index]:
                if character == '.':
                    self.sol_array[array_index].append(0)
                if character.isdigit():
                    self.sol_array[array_index].append(int(character))
            start_index = end_index
            end_index = end_index + 25

        # put the solution in the format of 9 arrays where each array represents the groups--this is the default format
        # for the solution array
        self.sol_array = rows_to_groups(self.sol_array)

    # method populates a list of lists containing row
    def define_list_of_lists(self):
        # this function picks the correct row or column array from the solution array, based on the input cell
        # location, and assigns those values to a specific cell within the "list-of-lists"
        def pick_array_by_location(group: int, cell: int, format: str, solution_array: list):
            if format == 'row':
                key = [[1, 1, 1, 2, 2, 2, 3, 3, 3],
                       [1, 1, 1, 2, 2, 2, 3, 3, 3],
                       [1, 1, 1, 2, 2, 2, 3, 3, 3],
                       [4, 4, 4, 5, 5, 5, 6, 6, 6],
                       [4, 4, 4, 5, 5, 5, 6, 6, 6],
                       [4, 4, 4, 5, 5, 5, 6, 6, 6],
                       [7, 7, 7, 8, 8, 8, 9, 9, 9],
                       [7, 7, 7, 8, 8, 8, 9, 9, 9],
                       [7, 7, 7, 8, 8, 8, 9, 9, 9]]
            else:
                key = [[1, 2, 3, 1, 2, 3, 1, 2, 3],
                       [4, 5, 6, 4, 5, 6, 4, 5, 6],
                       [7, 8, 9, 7, 8, 9, 7, 8, 9],
                       [1, 2, 3, 1, 2, 3, 1, 2, 3],
                       [4, 5, 6, 4, 5, 6, 4, 5, 6],
                       [7, 8, 9, 7, 8, 9, 7, 8, 9],
                       [1, 2, 3, 1, 2, 3, 1, 2, 3],
                       [4, 5, 6, 4, 5, 6, 4, 5, 6],
                       [7, 8, 9, 7, 8, 9, 7, 8, 9]]

            target_array = solution_array[key[group][cell] - 1]
            return target_array

        # instantiate a list at each of 81 locations (9 cell locations in 9 group arrays)
        for group in range(0, 9):
            self.list_of_lists_by_location.append([])
            for cell in range(0, 9):
                self.list_of_lists_by_location[group].append([])

        # for each cell, populate the list of lists with the correct group array based on cell location
        for group in range(0, 9):
            for cell in range(0, 9):
                self.list_of_lists_by_location[group][cell].append(self.sol_array[group])

        # for each cell, populate the list of lists with the correct row array based on cell location
        solution_row_array = self.solution_array_row_format()
        for group in range(0, 9):
            for cell in range(0, 9):
                row_array = pick_array_by_location(group, cell, 'row', solution_row_array)
                self.list_of_lists_by_location[group][cell].append(row_array)

        # for each cell, populate the list of lists with the correct column array based on cell location
        solution_column_array = self.solution_array_column_format()
        for group in range(0, 9):
            for cell in range(0, 9):
                col_array = pick_array_by_location(group, cell, 'col', solution_column_array)
                self.list_of_lists_by_location[group][cell].append(col_array)

    def __repr__(self):
        print(f'Solution({self.sol_array}')
