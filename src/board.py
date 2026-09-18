class Board:
    def __init__(self):
        self.grid = [None] * 9

    def make_move(self, position: int, player: str) -> bool:
        if self.grid[position] is None:
            self.grid[position] = player
            return True
        return False