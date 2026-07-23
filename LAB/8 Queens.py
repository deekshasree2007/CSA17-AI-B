N = 8

board = [[0 for _ in range(N)] for _ in range(N)]

def is_safe(board, row, col):

    # Check left side of current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve(col):

    if col >= N:
        return True

    for row in range(N):

        if is_safe(board, row, col):

            board[row][col] = 1

            if solve(col + 1):
                return True

            board[row][col] = 0

    return False


if solve(0):
    for row in board:
        print(row)
else:
    print("Solution does not exist")
