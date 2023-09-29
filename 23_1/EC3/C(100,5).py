P = []
n = 0
q = 0
cont = 0
k = 100

def Comb(np):
    global cont
    for i in range(1, n + 1):
        if i > P[np - 1]:
            P[np] = i
            if np == q:
                cont += 1
                print(P[1:])
                if cont == k:
                    return
            else:
                Comb(np + 1)
        if cont == k:
            return

n, q = map(int, input("Digite os valores de n e q: ").split())
P = [0] * (q + 1)
Comb(1)