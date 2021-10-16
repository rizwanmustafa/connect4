#!/usr/bin/env python3

from colorama import init as coloroma_init, Fore, Style
from typing import List

coloroma_init()

def create_empty_board() -> List[List[bool]]:
    board = []

    for i in range(6):
        board.append([None] * 7)

    return board

def print_board(board : List[List[bool]]):
	for row in board:
		for col in row:
			char = "_" if col == None else "X" if col == True else "O"
			color = Fore.RED if char == "X" else Fore.GREEN if char == "O" else ""
			print(color + char, end=" " + Style.RESET_ALL)

		print()

# Debug statements
board = create_empty_board()
board[0][0] = True # Player 1
board[0][1] = False # Player 2
print_board(board)
