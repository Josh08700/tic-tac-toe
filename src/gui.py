from nicegui import ui
from src.board import Board


class TicTacToeGame:
    def __init__(self, parent, board_index: int):
        self.parent = parent
        self.board = Board()
        self.buttons = {}
        self.board_index = board_index
        with ui.card().classes("p-4 flex flex-col items-center shadow-lg"):
            with ui.grid(columns=3).classes("gap-2 w-48 h-48"):
                for i in range(9):
                    self.buttons[i] = ui.button(
                        "",
                        on_click=lambda pos=i: self.make_move(pos),
                    ).classes("w-14 h-14 text-xl font-bold")

    def make_move(self, pos: int):

        if self.board.is_cell_occupied(pos):
            ui.notify("That cell is already taken.")
            return

        # Its impossible to run invalid move at the moment but this a failsafe.
        player = self.parent.current_turn
        if not self.board.make_move(pos, player):
            ui.notify("Invalid move.")
            return

        self.buttons[pos].text = player

        winner = self.board.check_winner()
        if winner:
            ui.notify(f"Player {winner} wins!")
            self.disable_all_buttons()
            self.parent.big_board_resolved[self.board_index] = True
            self.parent.big_board.make_move(self.board_index, winner)
            if self.parent.check_and_update_global_win():
                return
            print(f"Big Board State: {self.parent.big_board}")

        if self.board.is_draw():
            ui.notify("It's a draw!")
            self.disable_all_buttons()
            self.parent.big_board_resolved[self.board_index] = True
            if self.parent.check_and_update_global_win():
                return
            

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
        self.big_board = Board()
        self.big_board_resolved = [False] * 9

        ui.label("Dual Tic-Tac-Toe Demo").classes("text-2xl font-bold mb-4")

        ui.button("Reset Entire Game", on_click=self.reset_all_games).classes(
            "mb-4 bg-red-600 text-white font-bold"
        )

        self.global_turn_label = ui.label("Player X's Turn").classes(
            "text-md mb-2 text-gray-800"
        )

        self.games = []
        with ui.grid(columns=3).classes("gap-4 items-start"):
            for board_index in range(9):
                self.games.append(TicTacToeGame(self, board_index))

        ui.run(host="0.0.0.0", port=8080, title="Tic-Tac-Toe Demo", reload=False)

    def update_global_turn_label(self):
        self.global_turn_label.text = f"Player {self.current_turn}'s Turn"

    def check_and_update_global_win(self):
        winner = self.check_big_win()
        if winner:
            self.global_turn_label.text = f"Player {winner} wins the big game!"
            self.disable_all_buttons()
            return True

        if all(self.big_board_resolved):
            self.global_turn_label.text = "The big game is a draw!"
            self.disable_all_buttons()
            return True

        return False

    def reset_all_games(self):
        self.current_turn = "X"
        self.big_board = Board()
        self.big_board_resolved = [False] * 9
        for game in self.games:
            game.reset_game()
        self.update_global_turn_label()

    def check_big_win(self):
        return self.big_board.check_winner()
        
    def disable_all_buttons(self):
        for game in self.games:
            game.disable_all_buttons()

if __name__ == "__main__":
    multi_board()
