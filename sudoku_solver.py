import copy
import math
from typing import List, Tuple

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
    little_square_size = int(math.sqrt(size))

    x, y = divmod(i, little_square_size)
    square = []

    for row in puzzle[x * little_square_size : (x + 1) * little_square_size]:
        square.extend(row[y * little_square_size : (y + 1) * little_square_size])

    return square


def can_be_placed_in_row(puzzle: Sudoku, row: int, value: int) -> bool:
    return value not in get_row(puzzle, row)


def can_be_placed_in_column(puzzle: Sudoku, column: int, value: int) -> bool:
    return value not in get_column(puzzle, column)


def can_be_placed_in_square(puzzle: Sudoku, square: int, value: int) -> bool:
    return value not in get_square(puzzle, square)


def row_column_by_square(
    little_square_size, square_number, position
) -> Tuple[int, int]:
    row, column = divmod(square_number, little_square_size)
    pos1, pos2 = divmod(position, little_square_size)
    return row + pos1, column + pos2


def sudoku(puzzle: Sudoku) -> Sudoku:
    """return the solved puzzle as a 2d array of 9 x 9"""
    assert len(puzzle) == len(puzzle[0]) == 9
    size = len(puzzle)

    if not math.sqrt(size).is_integer():
        raise ValueError("Sudoku can not be splitted to little squares")

    little_square_size = int(math.sqrt(size))

    puzzle = copy.deepcopy(puzzle)

    while not sudoku_solved(puzzle):
        making_progress = False

        # try rows
        for row_number in range(size):
            if 0 not in get_row(puzzle, row_number):
                continue
            for value in range(1, size + 1):
                if not can_be_placed_in_row(puzzle, row_number, value):
                    continue

                columns = [
                    (
                        not puzzle[row_number][column_number]
                        and can_be_placed_in_column(puzzle, column_number, value)
                        and can_be_placed_in_square(
                            puzzle,
                            (
                                row_number // little_square_size
                                + column_number // little_square_size
                            ),
                            value,
                        )
                    )
                    for column_number in range(size)
                ]
                if columns.count(True) == 1:
                    c = columns.index(True)
                    puzzle[row_number][c] = value
                    making_progress = True

        # try columns
        for column_number in range(size):
            if 0 not in get_column(puzzle, column_number):
                continue
            for value in range(1, size + 1):
                if not can_be_placed_in_column(puzzle, column_number, value):
                    continue

                rows = [
                    (
                        not puzzle[row_number][column_number]
                        and can_be_placed_in_row(puzzle, row_number, value)
                        and can_be_placed_in_square(
                            puzzle,
                            (
                                row_number // little_square_size
                                + column_number // little_square_size
                            ),
                            value,
                        )
                    )
                    for row_number in range(size)
                ]
                if rows.count(True) == 1:
                    r = rows.index(True)
                    puzzle[r][column_number] = value
                    making_progress = True

        # try little squares
        for square_number in range(size):
            if 0 not in get_square(puzzle, square_number):
                continue
            for value in range(1, size + 1):
                if not can_be_placed_in_square(puzzle, square_number, value):
                    continue

                positions = []
                for p in range(size):
                    row_number, column_number = row_column_by_square(
                        little_square_size, square_number, p
                    )
                    positions.append(
                        not puzzle[row_number][column_number]
                        and can_be_placed_in_row(puzzle, row_number, value)
                        and can_be_placed_in_column(puzzle, column_number, value)
                    )

                if rows.count(True) == 1:
                    r = rows.index(True)
                    puzzle[r][column_number] = value
                    making_progress = True

        if not making_progress:
            raise SudokuError()

    return puzzle
