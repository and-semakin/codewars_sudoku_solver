import pytest

from sudoku_solver import Sudoku, sudoku_solved


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

