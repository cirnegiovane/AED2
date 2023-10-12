#include <iostream>
using namespace std;

int chessboard[8][8] = {{0}};

bool check(int x, int y) {
    for (int i = 0; i < 8; i++) {
        if (chessboard[x][i] == 1 || chessboard[i][y] == 1) {
            return false;
        }
    }

    for (int i = x, j = y; i >= 0 && j >= 0; i--, j--) {
        if (chessboard[i][j] == 1) {
            return false;
        }
    }

    for (int i = x, j = y; i >= 0 && j < 8; i--, j++) {
        if (chessboard[i][j] == 1) {
            return false;
        }
    }

    for (int i = x, j = y; i < 8 && j >= 0; i++, j--) {
        if (chessboard[i][j] == 1) {
            return false;
        }
    }

    for (int i = x, j = y; i < 8 && j < 8; i++, j++) {
        if (chessboard[i][j] == 1) {
            return false;
        }
    }

    return true;
}

bool solve_chessboard(int col) {
    if (col == 8) {
        return true;
    }

    for (int i = 0; i < 8; i++) {
        if (check(i, col)) {
            chessboard[i][col] = 1;
            if (solve_chessboard(col + 1)) {
                return true;
            }
            chessboard[i][col] = 0;
        }
    }

    return false;
}

int main() {
    if (solve_chessboard(0)) {
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                cout << chessboard[i][j] << " ";
            }
            cout << endl;
        }
    } else {
        cout << "Não há solução possível." << endl;
    }

    return 0;
}