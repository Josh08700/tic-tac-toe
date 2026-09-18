class Board:
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