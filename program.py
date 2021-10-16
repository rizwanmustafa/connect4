#!/usr/bin/env python3
from typing import List


def create_empty_board() -> List[List[bool]]:
    board = []

    for i in range(6):
        board.append([None] * 7)

    return board


# Debug statements
board = create_empty_board()
