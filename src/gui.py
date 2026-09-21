# from nicegui import ui
# from src.board import Board

# board = Board()
# current_player = ['X']  # Used a list so closure state updates smoothly
# buttons = {}

# def make_move(pos: int):
#     # Ignore clicks if game is already won or cell is taken
#     if board.check_winner() is not None:
#         return

#     player = current_player[0]
#     if board.make_move(pos, player):
#         # Update button text on screen
#         buttons[pos].text = player
        
#         # Check for winner
#         winner = board.check_winner()
#         if winner:
#             status_label.text = f'🎉 Player {winner} Wins!'
#             status_label.classes('text-green-600 font-bold')
#             disable_all_buttons()
#         elif board.is_draw():
#             status_label.set_text("🤝 It's a Draw / Tie!")
#             disable_all_buttons()
#         else:
#             # Switch player turn
#             current_player[0] = 'O' if player == 'X' else 'X'
#             status_label.text = f"Player {current_player[0]}'s Turn"

# def disable_all_buttons():
#     #for btn in buttons:
#     for btn in buttons.values():
#         btn.disable()


# def reset_game():
#     global board
#     board = Board()
#     current_player[0] = 'X'
#     status_label.text = "Player X's Turn"
#     status_label.classes('text-gray-800', remove='text-green-600 font-bold')
#     for pos, btn in buttons.items():
#         btn.text = ''

# # GUI Layout
# ui.label('Tic-Tac-Toe Demo').classes('text-2xl font-bold mb-4')
# status_label = ui.label("Player X's Turn").classes('text-lg mb-2')

# # 3x3 Grid of Clickable Buttons
# with ui.grid(columns=3).classes('gap-2 w-48 h-48'):
#     for i in range(9):
#         buttons[i] = ui.button('', on_click=lambda i=i: make_move(i)).classes('w-14 h-14 text-xl')

# ui.button('Reset Game', on_click=reset_game).classes('mt-4')

# #ui.run(title='Tic-Tac-Toe Demo', reload=False)
# ui.run(host='0.0.0.0', port=8080, title='Tic-Tac-Toe Demo', reload=False)

from nicegui import ui
from src.board import Board


class TicTacToeGame:

    def __init__(self, title: str = "Tic-Tac-Toe"):
        # Instance-specific state (completely separate per board)
        self.board = Board()
        self.current_player = "X"
        self.buttons = {}
        self.status_label = None

        # Build UI for this specific instance
        with ui.card().classes("p-4 flex flex-col items-center shadow-lg"):
            ui.label(title).classes("text-xl font-bold mb-2")
            self.status_label = ui.label("Player X's Turn").classes(
                "text-md mb-2 text-gray-800"
            )

            # 3x3 Grid of Clickable Buttons
            with ui.grid(columns=3).classes("gap-2 w-48 h-48"):
                for i in range(9):
                    # Store buttons in instance dictionary
                    self.buttons[i] = ui.button(
                        "", on_click=lambda pos=i: self.make_move(pos)
                    ).classes("w-14 h-14 text-xl font-bold")

            ui.button("Reset Game", on_click=self.reset_game).classes(
                "mt-4 text-sm"
            )

    def make_move(self, pos: int):
        # Ignore clicks if game is already won
        if self.board.check_winner() is not None:
            return

        player = self.current_player
        if self.board.make_move(pos, player):
            # Update button text on screen
            self.buttons[pos].text = player

            # Check for winner or draw
            winner = self.board.check_winner()
            if winner:
                self.status_label.text = f"🎉 Player {winner} Wins!"
                self.status_label.classes("text-green-600 font-bold")
            elif self.board.is_draw():
                self.status_label.text = "🤝 It's a Draw / Tie!"
                self.disable_all_buttons()
            else:
                # Switch player turn
                self.current_player = "O" if player == "X" else "X"
                self.status_label.text = f"Player {self.current_player}'s Turn"

    def disable_all_buttons(self):
        for btn in self.buttons.values():
            btn.disable()

    def reset_game(self):
        self.board = Board()
        self.current_player = "X"
        self.status_label.text = "Player X's Turn"
        self.status_label.classes(
            "text-gray-800", remove="text-green-600 font-bold"
        )
        for btn in self.buttons.values():
            btn.text = ""
            btn.enable()


# --- Main Application Layout ---
ui.label("Dual Tic-Tac-Toe Demo").classes("text-2xl font-bold mb-4")

# Flex container to place boards side-by-side
with ui.row().classes("gap-8 items-start flex-wrap"):
    game1 = TicTacToeGame(title="Board 1")
    game2 = TicTacToeGame(title="Board 2")

ui.run(host="0.0.0.0", port=8080, title="Tic-Tac-Toe Demo", reload=False)