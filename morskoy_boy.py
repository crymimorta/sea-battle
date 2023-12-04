from os import system, name
from time import sleep
import random

def clear():
    if name == 'nt':
        a = system('cls')
    else:
        a = system('clear')

def print_board(board):
    print("   A B C D E F G")
    for i in range(7):
        print(f"{i + 1:2d} ", end="")
        for j in range(7):
            print(board[i][j], end=" ")
        print()

def place_ships():
    ships = [(3, 's'), (2, 'm'), (2, 'm'), (1, 's'), (1, 's'), (1, 's'), (1, 's')]

    board = [['O' for _ in range(7)] for _ in range(7)]

    def is_valid_placement(x, y, size, orientation, board):
        def is_clear(x, y):
            if 0 <= x < 7 and 0 <= y < 7 and board[y][x] == 'O':
                return True
            return False

        def is_clear_around(x, y):
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= x + i < 7 and 0 <= y + j < 7:
                        if board[y + j][x + i] != 'O':
                            return False
            return True

        if orientation == 'horizontal':
            for i in range(size):
                if not is_clear(x + i, y) or not is_clear_around(x + i, y):
                    return False
        else:
            for i in range(size):
                if not is_clear(x, y + i) or not is_clear_around(x, y + i):
                    return False

        return True

    for size, symbol in ships:
        while True:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                x = random.randint(0, 6 - size)
                y = random.randint(0, 6)
            else:
                x = random.randint(0, 6)
                y = random.randint(0, 6 - size)

            if is_valid_placement(x, y, size, orientation, board):
                for i in range(size):
                    if orientation == 'horizontal':
                        board[y][x + i] = symbol
                    else:
                        board[y + i][x] = symbol
                break

    return board

def get_shot():
    while True:
        try:
            # Convert input to uppercase for case-insensitive comparison
            shot = input("Enter coordinates for your shot (e.g., A5): ").upper()
            if len(shot) == 2 and 'A' <= shot[0] <= 'G' and '1' <= shot[1] <= '7':
                return int(shot[1]) - 1, ord(shot[0]) - ord('A')
            else:
                print("Invalid input. Please enter a valid coordinate.")
        except ValueError:
            print("Invalid input. Please enter a valid coordinate.")

def play_game():
    clear()
    print("Dear player, in my version of the game, if you hit, then 'H' from the word 'Hit' will be displayed on the board at this point, if you miss 'M' from the word 'Miss'.")
    print("Thank you for your attention!")
    sleep(10)
    clear()

    player_name = input("Enter your name: ")
    shots = 0

    while True:
        clear()
        print(f"Player: {player_name}\n")
        board = place_ships()
        hidden_board = [['O' for _ in range(7)] for _ in range(7)]

        while True:
            clear()
            print_board(hidden_board)
            row, col = get_shot()

            if hidden_board[row][col] != 'O':
                print("You've already shot at this location. Try again.")
                continue

            shots += 1

            if board[row][col] != 'O':
                print("Hit!")
                sleep (2)
                hidden_board[row][col] = 'H'
            else:
                print("Miss!")
                sleep(2)
                hidden_board[row][col] = 'M'

            # Check if all ships are sunk
            if all(cell != 'O' for row in board for cell in row):
                print("Congratulations! You sank all the ships!")
                print(f"You made {shots} shots.")
                break

            # Check if all ships are hit but not every cell is shot
            if all(cell != 'O' for row in board for cell in row) and any(cell == 'O' for row in hidden_board for cell in row):
                print("All ships are hit, but not every cell is shot. Game over.")
                break

            # Check if all cells are shot
            if all(cell != 'O' for row in hidden_board for cell in row):
                print("All cells are shot. Game over.")
                break

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Game Over. Here is the sorted list of players:")
            sleep(5)
            # You can add your code to display a sorted list of players here.
            break

if __name__ == "__main__":
    play_game()
