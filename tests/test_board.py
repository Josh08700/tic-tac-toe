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

def test_cannot_overwrite_occupied_cell():
    board = Board()
    board.make_move(4, "X")
    
    # Try to play in the same occupied spot with 'O'
    success = board.make_move(4, "O")
    
    assert success is False
    assert board.grid[4] == "X"  # Original mark must remain unchanged

def test_out_of_bounds_move_returns_false():
    board = Board()
    success = board.make_move(9, "X")  # Index 9 is outside 0-8 range
    assert success is False