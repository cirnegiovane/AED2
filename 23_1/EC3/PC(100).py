def Permcircular(np):
    global n, P, S, cont

    for i in range(1, n):
        if not S[i]:
            P[np] = i
            S[i] = True
            if np == n - 1:
                if cont == 100:
                    return
                print(P)
                cont += 1
            else:
                Permcircular(np + 1)
            S[i] = False

n = int(input("Digite o valor de n: "))
S = [False] * n
P = [0] * n
P[n - 1] = n
cont = 0
Permcircular(1)