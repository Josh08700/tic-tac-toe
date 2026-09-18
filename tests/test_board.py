from src.board import Board

def test_board_initialization_has_nine_empty_spaces():
    board = Board()
    assert len(board.grid) == 9
    assert all(cell is None for cell in board.grid)

    