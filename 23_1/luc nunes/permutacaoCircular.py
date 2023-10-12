def permCirc(v, p, used, cont):
    if cont >= 100:     #condição de parada da função.
        return cont
    
    if len(p) == (len(v)-1):
        p.append(aux)
        print(p,file=arq)
        p.pop()
        cont += 1
        return cont

    for i in range(len(v)-1):
        if used[i] == False:
            used[i] = True
            p.append(v[i])

            cont = permCirc(v, p, used, cont)

            used[i] = False
            p.pop()
    return cont

arq = open("100PermCircular.txt", "w")
v = list(range(1,101))
aux = v[len(v)-1]
p = []
used = [False] * len(v)
cont = 0

permCirc(v, p, used, cont)
arq.close()
#Enunciado: PC(100) = permutações circulares de 100 elementos.