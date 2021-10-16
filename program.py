#!/usr/bin/env python3

from colorama import init as coloroma_init, Fore, Style
from typing import List

coloroma_init()


def create_empty_board() -> List[List[bool]]:
    board = []

    for i in range(6):
        board.append([None] * 7)

    return board


def print_board(board: List[List[bool]]):
    for row in board:
        for col in row:
            char = "_" if col == None else "X" if col == True else "O"
            color = Fore.RED if char == "X" else Fore.GREEN if char == "O" else ""
            print(color + char, end=" " + Style.RESET_ALL)

        print()


def drop_disc(board: List[List[bool]], playerOne: bool, col: int) -> bool:
    if 1 > col or col > 7:
        print("Column value out of bounds! It must be between 1 and 7 inclusive!")
        return False

    col -= 1

    placed_disc: bool = False

    for row in reversed(range(6)):
        # Go through each row from bottom to top and if its empty, place a disc
        if board[row][col] == None:
            board[row][col] = playerOne == True
            placed_disc = True
            break

    if not placed_disc:
        print(f"Cannot place disc in column {col + 1} because it is filled!")
        return False

    return True


# Debug statements
board = create_empty_board()
board[0][0] = True  # Player 1
board[0][1] = False  # Player 2
print_board(board)
print()
for i in range(8):
    print(drop_disc(board, i % 2 == 0, 7))
    print_board(board)
