# Função para verificar se o padrão ocorre i vezes na string
def verifica_padrao(i, string, padrao):
    count = 0
    j = 0

    for char in string:
        if char == padrao[j]:
            j += 1
            if j == len(padrao):
                count += 1
                j = 0
        if count >= i:
            return 'Y'
    
    return 'N'

# Leitura do número de casos de teste
num_casos_teste = int(input())

# Processamento de cada caso de teste
for _ in range(num_casos_teste):
    i = int(input())
    string = input()
    padrao = input()
    
    resultado = verifica_padrao(i, string, padrao)
    print(resultado)