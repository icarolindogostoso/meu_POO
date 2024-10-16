def maior (a,b,c):
    maior = a + ((a - b) * (-1 * (a < b)))
    return maior + ((maior - c) * (-1 * (maior < c)))

a = int(input())
b = int(input())
c = int(input())
print(maior(a,b,c))