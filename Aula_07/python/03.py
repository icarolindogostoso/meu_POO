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
        self.__setNome(nome)
        self.__setCpf(cpf)
        self.__setLimite(limite)
        self.__socio = None
    
    def __setNome (self, nome):
        if len(nome) > 0:
            self.__nome = nome
        else:
            raise ValueError ("Sem nome")
        
    def __setCpf (self, cpf):
        if len(cpf) > 0:
            self.__cpf = cpf
        else:
            raise ValueError ("Sem cpf")
        
    def __setLimite (self, limite):
        if limite > 0:
            self.__limite = limite
        else:
            raise ValueError ("Sem limite")
        
    def setSocio (self, cliente):
        self.__socio = cliente

    def getLimite (self):
        return self.__limite
    
    def __str__ (self):
        socio = f"e socio = {self.__socio}" if (socio != None) else ""
        return f"Cliente {self.__nome}, com cpf {self.__cpf} {socio}"
    

class UI:
    @staticmethod
    def menu():
        print("1 - Nova empresa, 2 - Cadastrar cliente, 3 - Listar clientes, 4 -")