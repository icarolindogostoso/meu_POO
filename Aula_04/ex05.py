class Triangulo:
    def __init__ (self):
        self.b = 0
        self.h = 0
    def calc_area(self):
        return self.b * self.h / 2

x = Triangulo() # Triangulo() cria um objeto da classe
                # x é uma referencia para esse objetoa
x.b = float(input("Informe o valor da base do triangulo: "))
x.h = float(input("Informe o valor da altura: "))
print(f"Área = {x.calc_area()}")