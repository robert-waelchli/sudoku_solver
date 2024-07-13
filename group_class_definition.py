# NAME:     Sudoku Group Class Definition File
# AUTHOR:   Robert Waelchli
# DATE:     2024 04 27
# PURPOSE:  This file only defines a Group class made up of nine cells. This file is part of Sudoku Pencil Marker
#           Version 1.0.

# imports
from cell_class_definition import Cell


class Group:
    def __init__(self, group_location: int):    # constructor
        self.group_location = group_location    # location attribute
        self.cell1: Cell = Cell(1)              # instantiate cell in group position 1
        self.cell2: Cell = Cell(2)              # instantiate cell in group position 2
        self.cell3: Cell = Cell(3)              # instantiate cell in group position 3
        self.cell4: Cell = Cell(4)              # instantiate cell in group position 4
        self.cell5: Cell = Cell(5)              # instantiate cell in group position 5
        self.cell6: Cell = Cell(6)              # instantiate cell in group position 6
        self.cell7: Cell = Cell(7)              # instantiate cell in group position 7
        self.cell8: Cell = Cell(8)              # instantiate cell in group position 8
        self.cell9: Cell = Cell(9)              # instantiate cell in group position 9

    # method to return a cell object from a specified location.
    def return_cell(self, position: int):
        if position == 1:
            cell = self.cell1
        elif position == 2:
            cell = self.cell2
        elif position == 3:
            cell = self.cell3
        elif position == 4:
            cell = self.cell4
        elif position == 5:
            cell = self.cell5
        elif position == 6:
            cell = self.cell6
        elif position == 7:
            cell = self.cell7
        elif position == 8:
            cell = self.cell8
        else:
            cell = self.cell9

        return cell

    def __repr__(self):
        print(f'Group({self.group_location})')
