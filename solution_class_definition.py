# NAME:     Solution Class Definition File
# AUTHOR:   Robert Waelchli
# DATE:     2024 04 28
# PURPOSE:  This file only defines a Solution class. This file is part of Sudoku Pencil Marker Version 1.0.

class Solution:
    def __init__(self, input_sol: str):                             # constructor
        self.sol_array = [[], [], [], [], [], [], [], [], []]
        self.define_solution_from_string(input_sol)

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

    def __repr__(self):
        print(f'Solution({self.sol_array}')
