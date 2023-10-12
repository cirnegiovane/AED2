def arranjoComRepeticao(v, p, cont): 
    if cont >= 100:     #condição de parada da função.
        return cont

    if len(p) == 4:     #4 pois é 4 a 4.
        print(p, file=arq)
        cont += 1
        return cont

    for i in range(len(v)):
            p.append(v[i])

            cont = arranjoComRepeticao(v, p, cont)

            p.pop()
    return cont

arq = open("100ArranjoComRep.txt", "w")
v = list(range(1,101))
p = []
cont = 0

arranjoComRepeticao(v, p, cont)
arq.close()