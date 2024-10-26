class Viagem:
    def __init__ (self):
        self.__distancia = 0
        self.__tempo = 0

    def set_distancia (self, v):
        if v > 0:
            self.__distancia = v
        else:
            raise ValueError ("a distancia nao pode ser negativa")
        
    def set_tempo (self, v):
        if v > 0:
            self.__tempo = v
        else:
            raise ValueError ("o tempo nao pode ser negativo")
        
    def get_distancia (self):
        return self.__distancia
    
    def get_tempo (self):
        return self.__tempo
    
    def velocidade_media (self):
        return self.__distancia / self.__tempo
    

class UI:
    @staticmethod
    def main():
        x = Viagem()

        x.set_distancia(float(input("Informe o valor da distancia da viagem: ")))
        x.set_tempo(float(input("Informe o valor do tempo da viagem: ")))

        print(f"Distancia = {x.get_distancia()} Tempo = {x.get_tempo()}")
        print(f"Velocidade media = {x.velocidade_media()}")

UI.main()