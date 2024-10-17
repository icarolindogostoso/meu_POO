class Triangulo:                        # tipo de variavel
    def __init__(self):                 # todos esses metodos que tem __algumacoisa__ tem alguma funcionalidade especifica no python
        self.b = 0                      
        self.h = 0                      # campos ou atributos

    def calc_area(self):                # metodo
        return self.b * self.h / 2

x = Triangulo()
y = int()
z = 5
s = str()

print(x, type(x))
print(y, type(y))
print(z, type(z))
print(s, type(s))