#Enunciado: C(100, 5) = combinações de 100 elementos, 5 a 5.

def comb(np, cont):
    for i in range(1, n+1):
        if cont == 100:
            return cont
        if i > p[np-1]:
            p[np] = i
            if np == q:
                print(p[1:], file = arq)
                cont += 1
                if cont == 100:
                    return cont
            else:
                cont = comb(np+1, cont)
                if cont == 100:
                    return cont
    return cont


arq = open("100Combinacoes.txt", "w")
q = 5           #pois combinação 5 a 5. Número de elementos a serem combinados por vez.
n = 100         #valor do teto das combinações, o valor máximo a ser combinado.
p = [-1] * 6    #vetor onde as soluções são armazenadas.
p[0] = 0        #0 sentinela
cont = 0
comb(1, cont)

arq.close()