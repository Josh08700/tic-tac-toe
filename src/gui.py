from nicegui import ui
from src.board import Board

board = Board()
current_player = ['X']  # Used a list so closure state updates smoothly
buttons = {}

def make_move(pos: int):
    # Ignore clicks if game is already won or cell is taken
    if board.check_winner() is not None:
        return

    player = current_player[0]
    if board.make_move(pos, player):
        # Update button text on screen
        buttons[pos].text = player
        
        # Check for winner
        winner = board.check_winner()
        if winner:
            status_label.text = f'🎉 Player {winner} Wins!'
            status_label.classes('text-green-600 font-bold')
        else:
            # Switch player turn
            current_player[0] = 'O' if player == 'X' else 'X'
            status_label.text = f"Player {current_player[0]}'s Turn"

def reset_game():
    global board
    board = Board()
    current_player[0] = 'X'
    status_label.text = "Player X's Turn"
    status_label.classes('text-gray-800', remove='text-green-600 font-bold')
    for pos, btn in buttons.items():
        btn.text = ''

# GUI Layout
ui.label('Tic-Tac-Toe Demo').classes('text-2xl font-bold mb-4')
status_label = ui.label("Player X's Turn").classes('text-lg mb-2')

# 3x3 Grid of Clickable Buttons
with ui.grid(columns=3).classes('gap-2 w-48 h-48'):
    for i in range(9):
        buttons[i] = ui.button('', on_click=lambda i=i: make_move(i)).classes('w-14 h-14 text-xl')

ui.button('Reset Game', on_click=reset_game).classes('mt-4')

#ui.run(title='Tic-Tac-Toe Demo', reload=False)
ui.run(host='0.0.0.0', port=8080, title='Tic-Tac-Toe Demo', reload=False)