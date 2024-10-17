class Triangulo:
    def __init__ (self):
        self.b = 0
        self.h = 0
    def calc_area(self):
        return self.b * self.h / 2

x = Triangulo() # Triangulo.__init__(x)
x.b = 5
x.h = 8
print(x.b,x.h)

y = Triangulo()
y.b = 10
y.h = 20
print(y.b,y.h)

z = y
z.b = 15
z.h = 30
print(y.b,y.h) # z e y estao apontados pro mesmo objeto, entao se mudar o z vai mudar o y

print(x.b * x.h / 2) # Area de X (jeito errado)
print(y.b * y.h / 2) # Area de Y (jeito errado)

print(x.calc_area()) # Area de X        Triangulo.calc_area(x)
print(y.calc_area()) # Area de Y        Triangulo.calc_area(y)
