def iniciais(nome):
    nome2 = []
    for i in nome:
        nome2.append(i[0].upper() + i[1:].lower())
    return nome2

nome = input().split()
print(*iniciais(nome))