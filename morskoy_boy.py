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
