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

### Start of UI Development, the project is changing from tests and class changes in each
# commit to: Tests, Class Changes and A sharable Demo.

def test_board_string_representation_shows_positions_and_marks():
    board = Board()
    board.make_move(0, "X")
    board.make_move(4, "O")

    expected_output = (
        " X | 1 | 2 \n"
        "---+---+---\n"
        " 3 | O | 5 \n"
        "---+---+---\n"
        " 6 | 7 | 8 "
    )
    assert str(board) == expected_output

### Testing draw logic. 

# def test_is_draw_false_on_empty_board():
#     board = Board()
#     assert board.is_draw() is False

# Same test with printing the board since there was a bug.
def test_is_draw_false_on_empty_board():
    board = Board()
    print("GRID STATE:", board.grid)  # Outputs [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    print("IS FULL?:", board.is_full())  # Should be False
    print("IS Winner?:", board.check_winner())  # Should be None
    assert board.is_draw() is False


def test_is_draw_true_when_board_full_and_no_winner():
    board = Board()
    # Fill board with a draw pattern:
    # X O X
    # X O O
    # O X X
    moves = [
        (0, "X"), (1, "O"), (2, "X"),
        (3, "X"), (4, "O"), (5, "O"),
        (6, "O"), (7, "X"), (8, "X")
    ]
    for pos, player in moves:
        board.make_move(pos, player)

    assert board.check_winner() is None
    assert board.is_draw() is True


def test_is_draw_false_when_board_full_but_winner_exists():
    board = Board()
    # Fill board with a winning line for X:
    # X X X
    # O O X
    # O X O
    moves = [
        (0, "X"), (1, "X"), (2, "X"),
        (3, "O"), (4, "O"), (5, "X"),
        (6, "O"), (7, "X"), (8, "O")
    ]
    for pos, player in moves:
        board.make_move(pos, player)

    assert board.check_winner() == "X"
    assert board.is_draw() is False


