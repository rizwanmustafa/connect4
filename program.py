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
        return -1

    for row in reversed(range(6)):
        # Go through each row from bottom to top and if its empty, place a disc
        if board[row][col] == None:
            board[row][col] = playerOne == True
            return row

    print(f"Cannot place disc in column {col + 1} because it is filled!")
    return -1


def get_vertical_count(row: int, col: int, board: List[List[bool]]) -> int:
    count: int = 1
    base = board[row][col]

    # Get bottom count
    for temp_row in range(row + 1, row + 4):
        if temp_row > 5:
            break

        if board[temp_row][col] == base:
            count += 1
        else:
            break

    # Get top count
    for temp_row in reversed(range(row - 3, row)):
        if temp_row < 0:
            break

        if board[temp_row][col] == base:
            count += 1
        else:
            break

    return count


def get_horizontal_count(row: int, col: int, board: List[List[bool]]) -> int:
    count: int = 1
    base = board[row][col]

    # Get bottom count
    for temp_col in range(col + 1, col + 4):
        if temp_col > 6:
            break

        if board[row][temp_col] == base:
            count += 1
        else:
            break

    # Get top count
    for temp_col in reversed(range(col - 3, col)):
        if temp_col < 0:
            break

        if board[row][temp_col] == base:
            count += 1
        else:
            break

    return count


def get_increasing_diagonal_count(row: int, col: int, board: List[List[bool]]) -> int:
    count: int = 1
    temp_row: int = row
    temp_col: int = col

    base = board[row][col]

    for i in range(3):
        temp_row -= 1
        temp_col += 1
        if not is_valid_row_col(temp_row, temp_col):
            break

        if board[temp_row][temp_col] == base:
            count += 1
        else:
            break

    temp_row: int = row
    temp_col: int = col

    for i in range(3):
        temp_row += 1
        temp_col -= 1

        if not is_valid_row_col(temp_row, temp_col):
            break

        if board[temp_row][temp_col] == base:
            count += 1
        else:
            break

    return count


def get_decreasing_diagonal_count(row: int, col: int, board: List[List[bool]]) -> int:
    count: int = 1
    temp_row: int = row
    temp_col: int = col

    base = board[row][col]

    for i in range(3):
        temp_row += 1
        temp_col += 1
        if not is_valid_row_col(temp_row, temp_col):
            break

        if board[temp_row][temp_col] == base:
            count += 1
        else:
            break

    temp_row: int = row
    temp_col: int = col

    for i in range(3):
        temp_row -= 1
        temp_col -= 1

        if not is_valid_row_col(temp_row, temp_col):
            break

        if board[temp_row][temp_col] == base:
            count += 1
        else:
            break

    return count


def is_valid_row_col(row: int = 0, col: int = 0) -> bool:
    if row < 0 or row > 5:
        return False

    if col < 0 or col > 6:
        return False

    return True


# Debug statements
board = create_empty_board()

board[3][0] = True
board[2][1] = True
board[1][2] = True
board[0][3] = True

print_board(board)
print()
