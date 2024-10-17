class Viagem:
    def __init__ (self):
        self.distancia = 0
        self.tempo_hora = 0
        self.tempo_minuto = 0
    def calc_velocidade (self):
        tempo_total = self.tempo_hora + (self.tempo_minuto / 60)
        return self.distancia / tempo_total
    
v = Viagem()
v.distancia = float(input("Digite a distancia de uma viagem em km: "))
v.tempo_hora = float(input("Digite o numero de horas demora a viagem: "))
v.tempo_minuto = float(input("Digite o numero de minutos demora a viagem: "))
print(f"Velocidade media da viagem> {v.calc_velocidade()}")