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


def test_no_winner_on_empty_or_ongoing_board():
    board = Board()
    assert board.check_winner() is None

    board.make_move(0, "X")
    board.make_move(1, "O")
    assert board.check_winner() is None

def test_top_row_win():
    board = Board()
    for pos in [0, 1, 2]:
        board.make_move(pos, "X")
    assert board.check_winner() == "X"

def test_left_column_win():
    board = Board()
    for pos in [0, 3, 6]:
        board.make_move(pos, "O")
    assert board.check_winner() == "O"

def test_diagonal_win():
    board = Board()
    for pos in [0, 4, 8]:
        board.make_move(pos, "X")
    assert board.check_winner() == "X"