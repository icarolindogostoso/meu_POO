from models.clientes import Cliente, Clientes

class View:
    @staticmethod
    def inserir_cliente(nome, email, fone):
        cliente = Cliente(0, nome, email, fone)
        Clientes.inserir(cliente)

    @staticmethod
    def clientes_listar():
        return Clientes.listar()

    @staticmethod
    def atualizar_clientes(id, nome, email, fone):
        cliente = Cliente(id, nome, email, fone)
        Clientes.atualizar(cliente)

    @staticmethod
    def excluir_clientes(id):
        Clientes.excluir(Clientes.listar_id(id))