#ALGORITMO DE BACKTRACKING PARA FAZER PERMUTAÇÕES DE TAMANHO n, COM SAÍDA n! SOLUÇÕES
# https://www.youtube.com/watch?v=Nabbpl7y4Lo

def perm(v, p, used):
    if len(p) == len(v):            #quando o tamanho do vetor de permutação for igual ao tamanho do vetor com os valores a serem permutados, é porque chegamos numa solução possível / caso base.
        print(p)
        return

    for i in range(len(v)):
        if used[i] == False:        #se minha escolha não foi utilizada, faça:
            used[i] = True          #seta True pra essa posição não ser utilizada na chamada recursiva
            p.append(v[i])          #adiciona o elemento v[i] na permutação(vetor p).
            
            perm(v, p, used)        #chamada recursiva pra formar a árvore de permutação.

            used[i] = False         #seta a posição já utilizada pra permutar como NÃO UTILIZADA depois da chamada recursiva.
            p.pop()                 #remove o v[i] da permutação pra poder criar outras soluções.



v = [1, 2, 3]
p = []
used = [False] * len(v)         #esse boolean array serve pra ver se o elemento na posição já foi usado pra permutar.

perm(v, p, used)