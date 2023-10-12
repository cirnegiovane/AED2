def arranjoSimp(v, p, used, cont): 
    if cont >= 100:     #condição de parada da função.
        return cont

    if len(p) == 4:     #4 pois é 4 a 4.
        print(p)
        cont += 1
        return cont

    for i in range(len(v)):
        if used[i] == False:
            used[i] = True
            p.append(v[i])

            cont = arranjoSimp(v, p, used, cont)

            used[i] = False
            p.pop()
    return cont


v = list(range(1,101))          #lista com os valores a serem organizados.
p = []                          #vetor onde os subconjuntos ficarão armazenados.
used = [False] * len(v)         #vetor com valores booleanos usados para fazer as escolhas
cont = 0

arranjoSimp(v, p, used, cont)


"""
 Implementar (entregar o programa e a saída impressa) um programa de Backtracking para gerar as 100 primeiras configurações:

 Arranjo Simples com 4 elementos.
"""