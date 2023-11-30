from os import system, name
from time import sleep
import random

def clear():
    if name == 'nt':
        a = system('cls')
    else:
        a = system('clear')
