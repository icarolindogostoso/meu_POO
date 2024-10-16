def maior (a,b):
    if a > b:
        return a
    else:
        return b
print(maior(2,4))
print(maior(4,2))
print(type(maior)) # é uma classe, entao pode gerar um objeto

x = maior 
print(x(10,20))