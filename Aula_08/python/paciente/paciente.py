from datetime import datetime

class Paciente:
    def __init__ (self, nome, cpf, telefone, nascimento):
        self.__setNome(nome)
        self.__setCpf(cpf)
        self.__setTelefone(telefone)
        self.__nascimento = nascimento
    
    def __setNome(self, nome):
        if len(nome) > 0:
            self.__nome = nome
        else:
            raise ValueError ("Nome vazio")

    def __setCpf(self, cpf):
        if len(cpf) > 0:
            self.__cpf = cpf
        else:
            raise ValueError ("Cpf invalido")
        
    def __setTelefone(self, telefone):
        if len(telefone) > 0:
            self.__telefone = telefone
        else:
            raise ValueError ("Telefone invalido")

    def idade(self):
        hoje = datetime.today()
        idade_ano = hoje.year - self.__nascimento.year
        idade_mes = hoje.month - self.__nascimento.month
        return f"{idade_ano} anos e {idade_mes} meses"
    
    def __str__ (self):
        return f"{self.__nome} - {self.__cpf} - {self.__telefone} - {self.__nascimento.date()}"