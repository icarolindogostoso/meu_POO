class Empresa:
    def __init__ (self, nome):
        self.__setNome(nome)
        self.__clientes = []

    def __setNome (self, nome):
        if len(nome) > 0:
            self.__nome = nome
        else:
            raise ValueError ("Sem nome")
    
    def inserir (self, cliente):
        self.__clientes.append(cliente)

    def listar (self):
        return self.__clientes
    
    def __str__ (self):
        return f"Empresa: {self.__nome}"
    

class Cliente:
    def __init__ (self, nome, cpf, limite):