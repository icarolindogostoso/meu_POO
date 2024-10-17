class Triangulo:
    pass

x = Triangulo()
y = Triangulo()
z = x # <- x e z vao referenciar o mesmo triangulo (tem 2 objetos)

print(x)
print(y)
print(z)