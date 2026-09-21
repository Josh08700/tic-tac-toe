import pytest
from src.multiple_board import SmallBoard, UltimateBoard


# --- SmallBoard Tests ---

def test_small_board_initial_state():
    board = SmallBoard()
    assert board.winner is None
    assert board.is_full() is False
    assert board.is_finished() is False


def test_small_board_make_move():
    board = SmallBoard()
    assert board.make_move(4, "X") is True
    assert board.grid[4] == "X"
    # Cannot overwrite an occupied square
    assert board.make_move(4, "O") is False


def test_small_board_win_detection():
    board = SmallBoard()
    for pos in [0, 1, 2]:
        board.make_move(pos, "X")
    assert board.check_winner() == "X"
    assert board.winner == "X"
    assert board.is_finished() is True


def test_small_board_blocks_moves_when_finished():
    board = SmallBoard()
    for pos in [0, 1, 2]:
        board.make_move(pos, "X")
    # Subsequent moves fail on a finished board
    assert board.make_move(3, "O") is False


# --- UltimateBoard Tests ---

def test_ultimate_board_initial_state():
    game = UltimateBoard()
    assert len(game.boards) == 9
    assert game.active_board_index is None  # Wildcard first move
    assert game.winner is None


def test_ultimate_board_target_rule():
    game = UltimateBoard()
    # Move in Board 0, Cell 4 -> Next player MUST play in Board 4
    assert game.make_move(0, 4, "X") is True
    assert game.active_board_index == 4

    # Player O tries to play in Board 0 (illegal)
    assert game.make_move(0, 1, "O") is False

    # Player O plays in forced Board 4, Cell 2 -> Next player MUST play in Board 2
    assert game.make_move(4, 2, "O") is True
    assert game.active_board_index == 2


def test_ultimate_board_wildcard_when_target_board_is_finished():
    game = UltimateBoard()
    # Win Board 1 for X: (Board 1, Cell 0), (Board 1, Cell 1), (Board 1, Cell 2)
    # We navigate moves to fill Board 1
    game.boards[1].make_move(0, "X")
    game.boards[1].make_move(1, "X")
    game.boards[1].make_move(2, "X")
    game.boards[1].check_winner()  # Board 1 is now finished

    # Set active board to Board 1
    game.active_board_index = 1

    # Since Board 1 is finished, active_board_index should resolve to None (Wildcard)
    assert game.get_valid_active_board() is None

    # Player can play in any non-finished board (e.g., Board 3)
    assert game.make_move(3, 0, "O") is True


def test_ultimate_board_global_win():
    game = UltimateBoard()
    # Manually mark Boards 0, 1, 2 as won by X
    for b_idx in [0, 1, 2]:
        game.boards[b_idx].winner = "X"

    assert game.check_global_winner() == "X"