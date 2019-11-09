import copy
import math
from typing import List

Sudoku = List[List[int]]


class SudokuError(Exception):
    """Unable to solve the puzzle."""


def sudoku_solved(puzzle: Sudoku) -> bool:
    return all(all(row) for row in puzzle)


def get_row(puzzle: Sudoku, i: int) -> List[int]:
    return puzzle[i]


def get_column(puzzle: Sudoku, i: int) -> List[int]:
    return [row[i] for row in puzzle]


def get_square(puzzle: Sudoku, i: int) -> List[int]:
    size = len(puzzle)
    if not math.sqrt(size).is_integer():
        raise ValueError("Sudoku can not be splitted to little squares")

    little_square_size = int(math.sqrt(size))

    x, y = divmod(i, little_square_size)
    square = []

    for row in puzzle[x * little_square_size : (x + 1) * little_square_size]:
        square.extend(row[y * little_square_size : (y + 1) * little_square_size])

    return square


def sudoku(puzzle: Sudoku) -> Sudoku:
    """return the solved puzzle as a 2d array of 9 x 9"""
    assert len(puzzle) == len(puzzle[0]) == 9
    puzzle = copy.deepcopy(puzzle)

    while not sudoku_solved(puzzle):
        # try rows
        # try columns
        # try little squares
        raise SudokuError()

    return puzzle
