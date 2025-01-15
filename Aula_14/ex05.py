from datetime import datetime

class Servico:
    def __init__ (self, id, descricao, valor, duracao):
        if valor < 0:
            raise ValueError ("Valor inválido")
        if duracao < 0:
            raise ValueError ("Duração inválida")
        
        self.__id = id
        self.__desciracao = descricao
        self.__valor = valor
        self.__duracao = duracao

class View:
    def abrir_agenda(data, hora_inicio, hora_fim, intervalo):
        dt = datetime.srtptime(data, "%d/%m/%Y")
        if dt.date() < datetime.now().date():
            raise ValueError ("Data inválida")