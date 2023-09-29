def is_valid(board, row, col):
    for i in range(len(board)):
        if board[i][col] == 1 or board[row][i] == 1:
            return False
        for j in range(len(board)):
            if abs(row - i) == abs(col - j) and board[i][j] == 1:
                return False
    return True

def solve(board, row, count):
    if count == 8:
        print_board(board)
        return

    for col in range(len(board)):
        if is_valid(board, row, col):
            board[row][col] = 1
            if row == len(board) - 1:
                solve(board, 0, count + 1)
            else:
                solve(board, row + 1, count + 1)
            board[row][col] = 0

    if row < len(board) - 1:
        solve(board, row + 1, count)

def print_board(board):
    for row in board:
        print(row)
    print()

board = [[0] * 8 for _ in range(8)]

fixed_towers = [[2, 6], [4, 4]]
for tower in fixed_towers:
    row, col = tower
    board[row][col] = 1

solve(board, 0, 2)