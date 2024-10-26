class EntradaDeCinema:
    def __init__ (self):
        self.__dia = ""
        self.__horario = []

    def set_dia (self, v):
        if v in ["Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]:
            self.__dia = v
        else:
            raise ValueError ("Dia inexistente")
        
    def set_horario (self, v):
        if (v > 0 and v < 24) :
            self.__horario = v
        else:
            raise ValueError ("Horario inexistente")
        
    def get_dia (self):
        return self.__dia
    
    def get_horario (self):
        return self.__horario
    
    def entrada (self):
        v = 16.00
        if self.__dia in ["Segunda", "Terca", "Quinta"]:
            v = v
            return v
        elif self.__dia == "Quarta":
            v = v / 2
            return v
        elif self.__dia in ["Sexta", "Sabado", "Domingo"]:
            v = v + 4
            return v
        elif self.__horario >= 17 and self.__horario < 24:
            v = v * 1.5
            return v
    
    def meia_entrada (self):
        v = 8.00
        if self.__dia in ["Segunda", "Terca", "Quinta"]:
            v = v
        elif self.__dia == "Quarta":
            v = v
            return v
        elif self.__dia in ["Sexta", "Sabado", "Domingo"]:
            v = v + 2
            return v
        elif self.__horario >= 17 and self.__horario < 24:
            v = v * 1.5
            return v


class UI:
    @staticmethod
    def main():
        x = EntradaDeCinema()

        x.set_dia(str(input("Informe o dia da sessão do seu filme: ").capitalize()))
        x.set_horario(int(input("Informe o horario da sessão do seu filme: ")))
        
        print(f"Entrada = {x.entrada()}")
        print(f"Meia entrada = {x.meia_entrada()}")

UI.main()