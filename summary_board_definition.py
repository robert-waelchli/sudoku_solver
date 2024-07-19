# NAME:     Sudoku Summary Board Class Definition File
# AUTHOR:   Robert Waelchli
# DATE:     2024 07 17
# PURPOSE:  This file only defines a Summary Board class. This file is part of Sudoku Solver Version 1.0.

# imports

class SummaryBoard:
    def __init__(self):                 # constructor
        self.summary_board = [[],       # representation of the overall game board
                              [],
                              [],
                              [],
                              [],
                              [],
                              [],
                              [],
                              []]

    # method returns a summary board organized by rows (vs. groups)
    def organize_board_by_rows(self):

        [aa, ab, ac, ba, bb, bc, ca, cb, cc] = self.summary_board[0]
        [ad, ae, af, bd, be, bf, cd, ce, cf] = self.summary_board[1]
        [ag, ah, aj, bg, bh, bj, cg, ch, cj] = self.summary_board[2]
        [da, db, dc, ea, eb, ec, fa, fb, fc] = self.summary_board[3]
        [dd, de, df, ed, ee, ef, fd, fe, ff] = self.summary_board[4]
        [dg, dh, dj, eg, eh, ej, fg, fh, fj] = self.summary_board[5]
        [ga, gb, gc, ha, hb, hc, ja, jb, jc] = self.summary_board[6]
        [gd, ge, gf, hd, he, hf, jd, je, jf] = self.summary_board[7]
        [gg, gh, gj, hg, hh, hj, jg, jh, jj] = self.summary_board[8]

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

    # method returns a summary board organized by columns (vs. groups)
    def organize_board_by_columns(self):

        [aa, ba, ca, ab, bb, cb, ac, bc, cc] = self.summary_board[0]
        [da, ea, fa, db, eb, fb, dc, ec, fc] = self.summary_board[1]
        [ga, ha, ja, gb, hb, jb, gc, hc, jc] = self.summary_board[2]
        [ad, bd, cd, ae, be, ce, af, bf, cf] = self.summary_board[3]
        [dd, ed, fd, de, ee, fe, df, ef, ff] = self.summary_board[4]
        [gd, hd, jd, ge, he, je, gf, hf, jf] = self.summary_board[5]
        [ag, bg, cg, ah, bh, ch, aj, bj, cj] = self.summary_board[6]
        [dg, eg, fg, dh, eh, fh, dj, ej, fj] = self.summary_board[7]
        [gg, hg, jg, gh, hh, jh, gj, hj, jj] = self.summary_board[8]

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

    def query_board_by_group(self, group: int):
        # since the board is by default by group, simply pull the group requested
        group_list = self.summary_board[group - 1]

        return group_list

    def query_board_by_row(self, row: int):
        # obtain a row-organized summary board
        row_summary_board = self.organize_board_by_rows()
        # pul the row list requested
        row_list = row_summary_board[row - 1]

        return row_list

    def query_board_by_col(self, col: int):
        # obtain a column-organized summary board
        column_summary_board = self.organize_board_by_columns()
        # pul the column list requested
        col_list = column_summary_board[col - 1]

        return col_list
