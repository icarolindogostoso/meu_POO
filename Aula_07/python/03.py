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
        self.__limite = self.__limite + cliente.__limite

    def getLimite (self):
        return self.__limite
    
    def __str__ (self):
        socio = f"e socio = {self.__socio}" if (self.__socio != None) else ""
        return f"Cliente {self.__nome}, com cpf {self.__cpf} {socio}"
    

class UI:
    @staticmethod
    def menu():
        print("1 - Nova empresa, 2 - Cadastrar cliente, 3 - Listar clientes, 9 - Fim")
        return int(input("Informe uma opcao: "))

    @staticmethod
    def main():
        op = 0
        empresa = None
        while op != 9:
            op = UI.menu()
            if op == 1:
                empresa = UI.nova_empresa()
            if op == 2:
                if empresa == None:
                    print("Nenhuma empresa criada!")
                else:
                    UI.inserir_cliente(empresa)
            if op == 3:
                if empresa == None:
                    print("Nenhuma empresa criada!")
                else:
                    UI.listar_clientes(empresa)

    @staticmethod
    def nova_empresa():
        nome = input("Informe o nome da empresa: ")
        empresa = Empresa(nome)
        return empresa

    @staticmethod
    def inserir_cliente (empresa):
        nome = input("Informe o nome do cliente: ")
        cpf = input("Informe o cpf do cliente: ")
        limite = float(input("Informe o limite do cliente: "))
        cliente = Cliente(nome,cpf,limite)
        empresa.inserir(cliente)

    @staticmethod
    def listar_clientes(empresa):
        print(empresa)
        for cliente in empresa.listar():
            print(cliente)

UI.main()