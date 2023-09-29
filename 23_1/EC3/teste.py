def GeraSub(ns, t, S, V, odd_count, even_count):
    n = len(V)
    for i in range(t, n+1):
        S[ns] = V[i-1]
        
        if V[i-1] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        
        if odd_count == 2 * even_count:
            print(S[:ns+1])
        
        if i < n:
            GeraSub(ns+1, i+1, S, V, odd_count, even_count)
        
        if V[i-1] % 2 == 0:
            even_count -= 1
        else:
            odd_count -= 1

n = int(input("Digite o valor de n: "))
V = []
for i in range(1, n+1):
    V.append(int(input(f"Digite V[{i}]: ")))

S = [0] * (n+1)  # Cria um array para armazenar os subconjuntos

GeraSub(1, 1, S, V, 0, 0)