from src.board import Board

def test_board_initialization_has_nine_empty_spaces():
    board = Board()
    assert len(board.grid) == 9
    assert all(cell is None for cell in board.grid)


def test_make_valid_move_places_player_mark():
    board = Board()
    success = board.make_move(0, "X")
    assert success is True
    assert board.grid[0] == "X"