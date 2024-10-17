class Viagem:
    def __init__ (self):
        self.distancia = 0
        self.tempo_horas = 0
        self.tempo_minutos = self.tempo_horas * 60
    def calc_velocidade (self):
        return self.distancia / self.tempo_horas

v = Viagem()
v.distancia = float(input("Digite a distancia da viagem: "))
v.tempo_horas = float(input("Digite o tempo da viagem em horas: "))
print(f"Velocidade media da viagem = {v.calc_velocidade()}")
print(f"Tempo da viagem em minutos = {v.tempo_minutos}")