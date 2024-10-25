from random import randint

board_size = 8

board = [[0 for col in range(board_size)] for row in range(board_size)]

def set_queen(queens_num, row):
    print(row)
    if row == board_size:
        print(board)
        return True
    for j in range(0, board_size):
        if queens_num == 0:
            board[0][randint(0, board_size - 1)] = 1
            row = 0
            queens_num += 1
            set_queen(queens_num, row + 1)
        else:
            if is_safe(row, j):
                board[row][j] = 1
                if set_queen(queens_num, row + 1):
                    return True
                board[row][j] = 0
    return False

def is_safe(r, c):
    if 1 in board[r]:
        return False
    for i in range(0, board_size):
        if board[i][c] == 1:
            return False
    for d in range(0, r):
        queen_idx = board[d].index(1)
        if queen_idx < c:
            cur_pos = c - queen_idx
            if r - d == cur_pos:
                return False
        else:
            offender_pos = queen_idx - c
            if r - d == offender_pos:
                return False
    return True


if not set_queen(0, 0):
    print("Could not solve")
