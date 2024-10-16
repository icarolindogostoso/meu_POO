def maior (a,b):
    return a + ((a - b) * (-1 * (a < b)))

a = int(input())
b = int(input())
print(maior(a,b))