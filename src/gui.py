from nicegui import ui
from src.board import Board

# --- Global Game State ---
current_turn = "X"


def update_all_status_labels():
    for g in games:
        if g.board.check_winner() is None and not g.board.is_draw():
            g.status_label.text = f"Player {current_turn}'s Turn"


class TicTacToeGame:

    def __init__(self, title: str = "Tic-Tac-Toe"):
        self.board = Board()
        self.buttons = {}
        self.status_label = None
        self.reset_button_on_or_off = "off"

        # Build UI for this specific instance
        with ui.card().classes("p-4 flex flex-col items-center shadow-lg"):
            ui.label(title).classes("text-xl font-bold mb-2")
            self.status_label = ui.label("Player X's Turn").classes(
                "text-md mb-2 text-gray-800"
            )

            # 3x3 Grid of Clickable Buttons
            with ui.grid(columns=3).classes("gap-2 w-48 h-48"):
                for i in range(9):
                    self.buttons[i] = ui.button(
                        "", on_click=lambda pos=i: self.make_move(pos)
                    ).classes("w-14 h-14 text-xl font-bold")

            if self.reset_button_on_or_off == "on":
                ui.button("Reset Game", on_click=self.reset_game).classes(
                    "mt-4 text-sm"
                )

    def make_move(self, pos: int):
        global current_turn

        if self.board.check_winner() is not None:
            return

        player = current_turn
        if self.board.make_move(pos, player):
            self.buttons[pos].text = player

            winner = self.board.check_winner()
            if winner:
                self.status_label.text = f"🎉 Player {winner} Wins!"
                self.status_label.classes("text-green-600 font-bold")
            elif self.board.is_draw():
                self.status_label.text = "🤝 It's a Draw / Tie!"
                self.disable_all_buttons()
            else:
                current_turn = "O" if current_turn == "X" else "X"
                update_all_status_labels()

    def disable_all_buttons(self):
        for btn in self.buttons.values():
            btn.disable()

    def reset_game(self):
        self.board = Board()
        self.status_label.text = f"Player {current_turn}'s Turn"
        self.status_label.classes(
            "text-gray-800", remove="text-green-600 font-bold"
        )
        for btn in self.buttons.values():
            btn.text = ""
            btn.enable()


def reset_all_games():
    global current_turn
    current_turn = "X"
    for g in games:
        g.reset_game()
    update_all_status_labels()


# --- Main Application Layout ---
ui.label("Dual Tic-Tac-Toe Demo").classes("text-2xl font-bold mb-4")

ui.button("Reset Entire Game", on_click=reset_all_games).classes(
    "mb-4 bg-red-600 text-white font-bold"
)

games = []
with ui.row().classes("gap-8 items-start flex-wrap"):
    for i in range(2):
        game = TicTacToeGame(title=f"Board {i}")
        games.append(game)

ui.run(host="0.0.0.0", port=8080, title="Tic-Tac-Toe Demo", reload=False)