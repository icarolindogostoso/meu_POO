import json

class Categoria:
    def __init__ (self, id, d):
        self.setId(id)
        self.setDescricao(d)

    def setId (self, id):
        if id > 0:
            self.__id = id
        else:
            raise ValueError ("Id invalido")
        
    def setDescricao(self, d):
        if len(d) > 0:
            self.__descricao = d
        else:
            raise ValueError ("Descicao invalida")
        
    def getId (self):
        return self.__id
    
    def getDescricao(self):
        return self.__descricao
        
    def __str__ (self):
        return f"{self.__id} - {self.__descricao}"
    
class Categorias:
    objetos = []

    @classmethod
    def inserir (cls, obj):
        cls.abrir()

        id = 0
        for categoria in cls.objetos:
            if categoria.getId() > id:
                id = categoria.getId()
        obj.setId(id + 1)

        cls.objetos.append(obj)

        cls.salvar()

    @classmethod
    def listar (cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def listarId (cls, id):
        cls.abrir()

        for categoria in cls.objetos:
            if categoria.getId() == id:
                return categoria
        return None
            
    @classmethod
    def atualizar (cls, obj):
        categoria = cls.listarId(obj.getId())
        if categoria != None:
            categoria.setDescricao(obj.getDescricao())
            cls.salvar()

    @classmethod
    def excluir (cls, obj):
        categoria = cls.listarId(obj.getId())
        if categoria != None:
            cls.objetos.remove(categoria)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Aula_09/Projeto_2/categorias.json", mode="r") as arquivo:
                clientes_json = json.load(arquivo)
                for obj in clientes_json:
                    c = Categoria(obj["id"], obj["d"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("Aula_09/Projeto_2/categorias.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)