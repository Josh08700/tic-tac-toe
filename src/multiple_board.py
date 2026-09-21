from typing import List, Optional


class SmallBoard:
    """Manages a single 3x3 Tic-Tac-Toe sub-board."""

    WINNING_COMBINATIONS = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]

    def __init__(self) -> None:
        self.grid: List[Optional[str]] = [None] * 9
        self.winner: Optional[str] = None

    def make_move(self, pos: int, player: str) -> bool:
        if self.is_finished() or self.grid[pos] is not None:
            return False
        self.grid[pos] = player
        self.check_winner()
        return True

    def check_winner(self) -> Optional[str]:
        if self.winner:
            return self.winner

        for combo in self.WINNING_COMBINATIONS:
            a, b, c = combo
            if self.grid[a] and self.grid[a] == self.grid[b] == self.grid[c]:
                self.winner = self.grid[a]
                return self.winner
        return None

    def is_full(self) -> bool:
        return None not in self.grid

    def is_draw(self) -> bool:
        return self.is_full() and self.winner is None

    def is_finished(self) -> bool:
        return self.winner is not None or self.is_full()


class UltimateBoard:
    """Manages 9 SmallBoard instances and global game state."""

    def __init__(self) -> None:
        self.boards: List[SmallBoard] = [SmallBoard() for _ in range(9)]
        self.active_board_index: Optional[int] = None  # None = Wildcard move
        self.winner: Optional[str] = None

    def get_valid_active_board(self) -> Optional[int]:
        """Returns the active board index, or None if wildcard choice is allowed."""
        if self.active_board_index is not None:
            target_board = self.boards[self.active_board_index]
            if not target_board.is_finished():
                return self.active_board_index
        return None  # Wildcard allowed

    def make_move(self, board_idx: int, cell_idx: int, player: str) -> bool:
        if self.winner is not None:
            return False

        valid_active = self.get_valid_active_board()
        if valid_active is not None and board_idx != valid_active:
            return False  # Player must play in the forced active board

        target_board = self.boards[board_idx]
        if not target_board.make_move(cell_idx, player):
            return False

        # Set the next active board based on the cell played
        next_target = self.boards[cell_idx]
        if next_target.is_finished():
            self.active_board_index = None  # Wildcard for next turn
        else:
            self.active_board_index = cell_idx

        self.check_global_winner()
        return True

    def check_global_winner(self) -> Optional[str]:
        if self.winner:
            return self.winner

        # Form a global 3x3 grid of winning players
        global_grid = [b.winner for b in self.boards]

        for combo in SmallBoard.WINNING_COMBINATIONS:
            a, b, c = combo
            if global_grid[a] and global_grid[a] == global_grid[b] == global_grid[c]:
                self.winner = global_grid[a]
                return self.winner

        return None

    def is_draw(self) -> bool:
        all_finished = all(b.is_finished() for b in self.boards)
        return all_finished and self.winner is None