from typing import List

import pytest

from sudoku_solver import Sudoku, sudoku_solved, get_row, get_column, get_square


class TestUnit:
    @pytest.mark.parametrize(
        ("puzzle", "solved"),
        [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], True,),
            ([[0, 2, 3], [4, 5, 6], [7, 8, 9]], False,),
        ],
    )
    def test_sudoku_solved(self, puzzle: Sudoku, solved: bool) -> None:
        assert sudoku_solved(puzzle) == solved

    @pytest.mark.parametrize(
        ("puzzle", "row_number", "expected_row"),
        [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, [1, 2, 3],),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, [4, 5, 6],),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, [7, 8, 9],),
        ],
    )
    def test_get_row(
        self, puzzle: Sudoku, row_number: int, expected_row: List[int]
    ) -> None:
        assert get_row(puzzle, row_number) == expected_row

    @pytest.mark.parametrize(
        ("puzzle", "column_number", "expected_column"),
        [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, [1, 4, 7],),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, [2, 5, 8],),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, [3, 6, 9],),
        ],
    )
    def test_get_column(
        self, puzzle: Sudoku, column_number: int, expected_column: List[int]
    ) -> None:
        assert get_column(puzzle, column_number) == expected_column

    @pytest.mark.parametrize(
        ("puzzle", "square_number", "expected_square"),
        [
            (
                [[1, 1, 2, 2], [1, 1, 2, 2], [3, 3, 4, 4], [3, 3, 4, 4]],
                0,
                [1, 1, 1, 1],
            ),
            (
                [[1, 1, 2, 2], [1, 1, 2, 2], [3, 3, 4, 4], [3, 3, 4, 4]],
                1,
                [2, 2, 2, 2],
            ),
            (
                [[1, 1, 2, 2], [1, 1, 2, 2], [3, 3, 4, 4], [3, 3, 4, 4]],
                2,
                [3, 3, 3, 3],
            ),
            (
                [[1, 1, 2, 2], [1, 1, 2, 2], [3, 3, 4, 4], [3, 3, 4, 4]],
                3,
                [4, 4, 4, 4],
            ),
        ],
    )
    def test_get_square(
        self, puzzle: Sudoku, square_number: int, expected_square: List[int]
    ) -> None:
        assert get_square(puzzle, square_number) == expected_square

    def test_get_square_raises_if_puzzle_can_not_be_split_to_squares(self) -> None:
        with pytest.raises(ValueError):
            get_square([[1], [2], [3]], 1)
