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

    # method by which rows are transposed to columns and back
    def rows_to_cols_and_back(self):
        [aa, ba, ca, da, ea, fa, ga, ha, ja] = self.sol_array[0]
        [ab, bb, cb, db, eb, fb, gb, hb, jb] = self.sol_array[1]
        [ac, bc, cc, dc, ec, fc, gc, hc, jc] = self.sol_array[2]
        [ad, bd, cd, dd, ed, fd, gd, hd, jd] = self.sol_array[3]
        [ae, be, ce, de, ee, fe, ge, he, je] = self.sol_array[4]
        [af, bf, cf, df, ef, ff, gf, hf, jf] = self.sol_array[5]
        [ag, bg, cg, dg, eg, fg, gg, hg, jg] = self.sol_array[6]
        [ah, bh, ch, dh, eh, fh, gh, hh, jh] = self.sol_array[7]
        [aj, bj, cj, dj, ej, fj, gj, hj, jj] = self.sol_array[8]

        self.sol_array[0] = [aa, ab, ac, ad, ae, af, ag, ah, aj]
        self.sol_array[1] = [ba, bb, bc, bd, be, bf, bg, bh, bj]
        self.sol_array[2] = [ca, cb, cc, cd, ce, cf, cg, ch, cj]
        self.sol_array[3] = [da, db, dc, dd, de, df, dg, dh, dj]
        self.sol_array[4] = [ea, eb, ec, ed, ee, ef, eg, eh, ej]
        self.sol_array[5] = [fa, fb, fc, fd, fe, ff, fg, fh, fj]
        self.sol_array[6] = [ga, gb, gc, gd, ge, gf, gg, gh, gj]
        self.sol_array[7] = [ha, hb, hc, hd, he, hf, hg, hh, hj]
        self.sol_array[8] = [ja, jb, jc, jd, je, jf, jg, jh, jj]

    # method by which rows are transposed to groups and back
    def rows_to_groups_and_back(self):
        [aa, ab, ac, ba, bb, bc, ca, cb, cc] = self.sol_array[0]
        [ad, ae, af, bd, be, bf, cd, ce, cf] = self.sol_array[1]
        [ag, ah, aj, bg, bh, bj, cg, ch, cj] = self.sol_array[2]
        [da, db, dc, ea, eb, ec, fa, fb, fc] = self.sol_array[3]
        [dd, de, df, ed, ee, ef, fd, fe, ff] = self.sol_array[4]
        [dg, dh, dj, eg, eh, ej, fg, fh, fj] = self.sol_array[5]
        [ga, gb, gc, ha, hb, hc, ja, jb, jc] = self.sol_array[6]
        [gd, ge, gf, hd, he, hf, jd, je, jf] = self.sol_array[7]
        [gg, gh, gj, hg, hh, hj, jg, jh, jj] = self.sol_array[8]

        self.sol_array[0] = [aa, ab, ac, ad, ae, af, ag, ah, aj]
        self.sol_array[1] = [ba, bb, bc, bd, be, bf, bg, bh, bj]
        self.sol_array[2] = [ca, cb, cc, cd, ce, cf, cg, ch, cj]
        self.sol_array[3] = [da, db, dc, dd, de, df, dg, dh, dj]
        self.sol_array[4] = [ea, eb, ec, ed, ee, ef, eg, eh, ej]
        self.sol_array[5] = [fa, fb, fc, fd, fe, ff, fg, fh, fj]
        self.sol_array[6] = [ga, gb, gc, gd, ge, gf, gg, gh, gj]
        self.sol_array[7] = [ha, hb, hc, hd, he, hf, hg, hh, hj]
        self.sol_array[8] = [ja, jb, jc, jd, je, jf, jg, jh, jj]

    # method converts an input string solution into an array of arrays
    def define_solution_from_string(self, input_sol: str):

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

    # method populates a list of lists containing row
    def define_list_of_lists(self):
        # this function picks the correct row, column, or group array from the solution array, based on the cell
        # location, and assigns those values to a specific cell within the "list-of-lists"
        def pick_array_by_location(location: int, format: str):
            if format == 'row':
                key = [1, 1, 1, 1, 1, 1, 1, 1, 1,
                       2, 2, 2, 2, 2, 2, 2, 2, 2,
                       3, 3, 3, 3, 3, 3, 3, 3, 3,
                       4, 4, 4, 4, 4, 4, 4, 4, 4,
                       5, 5, 5, 5, 5, 5, 5, 5, 5,
                       6, 6, 6, 6, 6, 6, 6, 6, 6,
                       7, 7, 7, 7, 7, 7, 7, 7, 7,
                       8, 8, 8, 8, 8, 8, 8, 8, 8,
                       9, 9, 9, 9, 9, 9, 9, 9, 9]
            elif format == 'col':
                key = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                       1, 2, 3, 4, 5, 6, 7, 8, 9,
                       1, 2, 3, 4, 5, 6, 7, 8, 9,
                       1, 2, 3, 4, 5, 6, 7, 8, 9,
                       1, 2, 3, 4, 5, 6, 7, 8, 9,
                       1, 2, 3, 4, 5, 6, 7, 8, 9,
                       1, 2, 3, 4, 5, 6, 7, 8, 9,
                       1, 2, 3, 4, 5, 6, 7, 8, 9,
                       1, 2, 3, 4, 5, 6, 7, 8, 9]
            else:
                key = [1, 1, 1, 2, 2, 2, 3, 3, 3,
                       1, 1, 1, 2, 2, 2, 3, 3, 3,
                       1, 1, 1, 2, 2, 2, 3, 3, 3,
                       4, 4, 4, 5, 5, 5, 6, 6, 6,
                       4, 4, 4, 5, 5, 5, 6, 6, 6,
                       4, 4, 4, 5, 5, 5, 6, 6, 6,
                       7, 7, 7, 8, 8, 8, 9, 9, 9,
                       7, 7, 7, 8, 8, 8, 9, 9, 9,
                       7, 7, 7, 8, 8, 8, 9, 9, 9]

            target_array = self.sol_array[key[location - 1] - 1]
            return target_array

        for location in range(1, 82):
            self.list_of_lists_by_location.append([])

        # for each row, populate the list of lists with the correct row array based on cell location
        for location in range(1, 82):
            row = pick_array_by_location(location, 'row')
            self.list_of_lists_by_location[location - 1].append(row)

        # for each column, populate the list of lists with the correct column array based on cell location
        self.rows_to_cols_and_back()
        for location in range(1, 82):
            col = pick_array_by_location(location, 'col')
            self.list_of_lists_by_location[location - 1].append(col)
        self.rows_to_cols_and_back()

        # for each group, populate the list of lists with the correct group array based on cell location
        self.rows_to_groups_and_back()
        for location in range(1, 82):
            group = pick_array_by_location(location, 'group')
            self.list_of_lists_by_location[location - 1].append(group)
        self.rows_to_groups_and_back()

    def __repr__(self):
        print(f'Solution({self.sol_array}')
