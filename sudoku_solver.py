from typing import List

Sudoku = List[List[int]]


def sudoku_solved(puzzle: Sudoku) -> bool:
    return all(all(row) for row in puzzle)


def sudoku(puzzle: Sudoku) -> Sudoku:
    """return the solved puzzle as a 2d array of 9 x 9"""
    assert len(puzzle) == len(puzzle[0]) == 9
    return puzzle
