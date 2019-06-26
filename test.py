QuantidadeDeProblemas = int(input())
Lista = ()
for i in range(QuantidadeDeProblemas):
    Problema, Solução, Dificuldade = input().split()
    Dificuldade = int(Dificuldade)
    tupla = (Dificuldade, Problema, Solução,)
    Lista = (tupla,) + Lista
print(Lista)
Lista = sorted(Lista, reverse = True, key = lambda a: a[0])
for d, p, s in Lista:
    print(s, end="")
