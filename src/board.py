class Board:

    WINNING_COMBINATIONS = [
        # Rows
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        # Columns
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        # Diagonals
        (0, 4, 8), (2, 4, 6)
    ]

    def __init__(self):
        self.grid = [None] * 9


    def make_move(self, position: int, player: str) -> bool:
        # Check if position is within valid board indices (0 to 8)
        if not (0 <= position < 9):
            return False
            
        if self.grid[position] is None:
            self.grid[position] = player
            return True
        return False

    def check_winner(self) -> str | None:
        for a, b, c in self.WINNING_COMBINATIONS:
            if self.grid[a] is not None and self.grid[a] == self.grid[b] == self.grid[c]:
                return self.grid[a]
        return None

    