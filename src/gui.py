from nicegui import ui
from src.board import Board


class TicTacToeGame:
    def __init__(self, parent):
        self.parent = parent
        self.board = Board()
        self.buttons = {}

        with ui.card().classes("p-4 flex flex-col items-center shadow-lg"):
            with ui.grid(columns=3).classes("gap-2 w-48 h-48"):
                for i in range(9):
                    self.buttons[i] = ui.button(
                        "",
                        on_click=lambda pos=i: self.make_move(pos),
                    ).classes("w-14 h-14 text-xl font-bold")

    def make_move(self, pos: int):
        if self.board.grid[pos] is not None:
            ui.notify("That cell is already taken.")
            return

        player = self.parent.current_turn
        if not self.board.make_move(pos, player):
            ui.notify("Invalid move.")
            return

        self.buttons[pos].text = player

        winner = self.board.check_winner()
        if winner:
            ui.notify(f"Player {winner} wins!")
            self.disable_all_buttons()
            #return

        if self.board.is_draw():
            ui.notify("It's a draw!")
            self.disable_all_buttons()
            #return

        self.parent.current_turn = "O" if self.parent.current_turn == "X" else "X"
        self.parent.update_global_turn_label()

    def disable_all_buttons(self):
        for btn in self.buttons.values():
            btn.disable()

    def reset_game(self):
        self.board = Board()
        for btn in self.buttons.values():
            btn.text = ""
            btn.enable()


class multi_board:
    def __init__(self):
        self.current_turn = "X"

        ui.label("Dual Tic-Tac-Toe Demo").classes("text-2xl font-bold mb-4")

        ui.button("Reset Entire Game", on_click=self.reset_all_games).classes(
            "mb-4 bg-red-600 text-white font-bold"
        )

        self.global_turn_label = ui.label("Player X's Turn").classes(
            "text-md mb-2 text-gray-800"
        )

        self.games = []
        with ui.grid(columns=3).classes("gap-4 items-start"):
            for _ in range(9):
                self.games.append(TicTacToeGame(self))

        ui.run(host="0.0.0.0", port=8080, title="Tic-Tac-Toe Demo", reload=False)

    def update_global_turn_label(self):
        self.global_turn_label.text = f"Player {self.current_turn}'s Turn"

    def reset_all_games(self):
        self.current_turn = "X"
        for game in self.games:
            game.reset_game()
        self.update_global_turn_label()


if __name__ == "__main__":
    multi_board()
