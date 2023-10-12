def solve_torres_pacificas():
    tabuleiro = [[0] * 8 for _ in range(8)]

    tabuleiro[2][3] = 1
    tabuleiro[7][5] = 1

    def is_safe(x, y):
        for i in range(8):
            if tabuleiro[x][i] == 1 or tabuleiro[i][y] == 1:
                return False
        for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
            if tabuleiro[i][j] == 1:
                return False
        for i, j in zip(range(x, -1, -1), range(y, 8)):
            if tabuleiro[i][j] == 1:
                return False
        for i, j in zip(range(x, 8), range(y, -1, -1)):
            if tabuleiro[i][j] == 1:
                return False
        for i, j in zip(range(x, 8), range(y, 8)):
            if tabuleiro[i][j] == 1:
                return False
        return True

    def solve_util(col):
        if col == 8:
            return True
        for i in range(8):
            if is_safe(i, col):
                tabuleiro[i][col] = 1
                if solve_util(col + 1):
                    return True
                tabuleiro[i][col] = 0
        return False

    if solve_util(0):
        
        for row in tabuleiro:
            print(row)
    else:
        print("-1")

solve_torres_pacificas()