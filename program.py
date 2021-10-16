#!/usr/bin/env python3

import os

from colorama import init as coloroma_init, Fore, Style
from typing import List

coloroma_init()


def create_empty_board() -> List[List[bool]]:
    board = []

    for i in range(6):
        board.append([None] * 7)

    return board


def print_board(board: List[List[bool]]):
    print("1 2 3 4 5 6 7")
    for row in board:
        for col in row:
            char = "_" if col == None else "X" if col == True else "O"
            color = Fore.RED if char == "X" else Fore.GREEN if char == "O" else ""
            print(color + char, end=" " + Style.RESET_ALL)

        print()


def drop_disc(board: List[List[bool]], playerOne: bool, col: int) -> bool:
    if 0 > col or col > 6:
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


def is_board_full(board: List[List[bool]]) -> bool:
    for row in board:
        for col in row:
            if col == None:
                return False

    return True


def is_valid_row_col(row: int = 0, col: int = 0) -> bool:
    if row < 0 or row > 5:
        return False

    if col < 0 or col > 6:
        return False

    return True


def get_player_text(player_one: bool, player_name: str):
    if player_one:
        return Fore.RED + f"Player 1 ({player_name}) " + Style.RESET_ALL
    else:
        return Fore.GREEN + f"Player 2 ({player_name}) " + Style.RESET_ALL


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


# Variables for playing
clear_console()

player_one_name = input("Player 1 Name: ")
player_two_name = input("Player 2 Name: ")
clear_console()

board = create_empty_board()
player_one_turn: bool = True


while True:
    print("Connect4 Implemented by Rizwan Mustafa (A1 2021)")
    print()
    print_board(board)
    print()

    # Keep taking input from the user until correct column is entered
    while True:

        col = input(get_player_text(player_one_turn, player_one_name if player_one_turn else player_two_name) + "Enter column number for placing disc: ")
        if not col.isnumeric():
            continue
        col = int(col)
        if col < 1 or col > 7:
            continue

        col -= 1
        row = drop_disc(board, player_one_turn, col)

        if row != -1:
            # The disc was placed, check for victory
            max_count = max(
                get_vertical_count(row, col, board),
                get_horizontal_count(row, col, board),
                get_increasing_diagonal_count(row, col, board),
                get_decreasing_diagonal_count(row, col, board)
            )

            # If the player won, let them know
            if max_count >= 4:
                clear_console()
                print("Connect4 Implemented by Rizwan Mustafa (A1 2021)")
                print_board(board)
                print()
                print(get_player_text(player_one_turn, player_one_name if player_one_turn else player_two_name) + "wins!")

                user_choice = input("Play another game [Y/N]: ").lower()
                if user_choice == "y":
                    clear_console()
                    board = create_empty_board()
                    player_one_turn = not player_one_turn
                    break
                else:
                    exit()

            # If there is a draw, let them know
            if is_board_full(board):
                clear_console()
                print("Connect4 Implemented by Rizwan Mustafa (A1 2021)")
                print()
                print_board(board)
                print()
                print("Draw between " + get_player_text(True, player_one_name) + "and" + get_player_text(False, player_two_name) + "!")

                user_choice = input("Play another game [Y/N]: ").lower()
                if user_choice == "y":
                    clear_console()
                    board = create_empty_board()
                    player_one_turn = not player_one_turn
                    break
                else:
                    exit()
        else:
            continue

        clear_console()
        break

    player_one_turn = not player_one_turn

# TODO: Test, test and test this application
