from src.board import Board

def main():
    board = Board()
    current_player = "X"

    print("=================================")
    print("   WELCOME TO TIC-TAC-TOE DEMO   ")
    print("=================================\n")

    while True:
        print(board)
        print()
        user_input = input(f"Player {current_player}, choose a position (0-8) or 'q' to quit: ")

        if user_input.lower() == "q":
            print("Demo exited.")
            break

        if not user_input.isdigit():
            print("\n[!] Invalid input. Please enter a number from 0 to 8.\n")
            continue

        pos = int(user_input)
        if board.make_move(pos, current_player):
            print(f"\n[+] Player {current_player} played at position {pos}.\n")
        else:
            print("\n[!] Invalid move! Square is taken or out of bounds.\n")

if __name__ == "__main__":
    main()