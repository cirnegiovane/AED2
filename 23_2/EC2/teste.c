#include <stdio.h>
#include <string.h>

#define MAX_LEN 100

// Matriz de memoização para armazenar resultados intermediários
int memo[MAX_LEN][MAX_LEN];

// Função para encontrar o mínimo entre três números
int min(int a, int b, int c) {
    if (a <= b && a <= c) return a;
    if (b <= a && b <= c) return b;
    return c;
}

// Função recursiva para calcular a distância de edição
int editDistance(char *str1, char *str2, int i, int j) {
    // Casos base: se uma das strings estiver vazia, a distância é o comprimento da outra string
    if (i == 0) return j;
    if (j == 0) return i;

    // Verificar se o resultado já foi calculado antes (memoização)
    if (memo[i][j] != -1) return memo[i][j];

    // Se os últimos caracteres são iguais, não é necessário fazer nenhuma operação
    if (str1[i - 1] == str2[j - 1]) {
        memo[i][j] = editDistance(str1, str2, i - 1, j - 1);
    } else {
        // Caso contrário, calcular a distância mínima considerando diferentes operações
        int insert = 1 + editDistance(str1, str2, i, j - 1);
        int remove = 1 + editDistance(str1, str2, i - 1, j);
        int replace = 1 + editDistance(str1, str2, i - 1, j - 1);
        memo[i][j] = min(insert, remove, replace);
    }

    return memo[i][j];
}

int main() {
    char str1[] = "tabua";
    char str2[] = "pedra";
    int len1 = strlen(str1);
    int len2 = strlen(str2);

    // Inicializar a matriz de memoização com -1
    memset(memo, -1, sizeof(memo));

    // Chamar a função para calcular a distância de edição
    int distance = editDistance(str1, str2, len1, len2);

    // Imprimir o resultado
    printf("A distância de edição entre '%s' e '%s' é %d.\n", str1, str2, distance);

    return 0;
}