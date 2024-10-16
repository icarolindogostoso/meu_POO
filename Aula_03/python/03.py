def iniciais(nome):
    for i in range(len(nome)):
        nome[i] = nome[i][0]

nome = input().split()
iniciais(nome)
print(*nome)