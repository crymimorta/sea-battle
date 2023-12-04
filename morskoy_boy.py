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
