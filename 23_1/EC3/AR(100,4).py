def Arranjo(np):
    global P, n, q, cont

    if np == q + 1:
        cont += 1
        if cont > k:
            return
        print(P[1:])
    else:
        for i in range(1, n + 1):
            P[np] = i
            Arranjo(np + 1)

n, q = map(int, input("Digite o valor de n e q: ").split())
P = [0] * (q + 1)
cont = 0
k = 100
Arranjo(1)