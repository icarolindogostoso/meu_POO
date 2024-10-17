class Circulo:
    def __init__ (self):
        self.r = 0
    def calc_area (self):
        return 3.14 * (self.r * self.r)

c = Circulo()
c.r = float(input("Digite o raio de um circulo: "))
print("Área =", c.calc_area())