from datetime import datetime, timedelta
from views import View

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1:
                UI.atleta_inserir()
            if op == 2:
                UI.atleta_listar()
            if op == 3:
                UI.treino_inserir()
            if op == 4:
                UI.treino_listar()
            if op == 5:
                UI.atleta_mais_rapido()
            if op == 6:
                UI.treino_mais_rapido()
            
    @staticmethod
    def menu():
        print("1-Inserir Atleta, 2-Listar Atleta, 3-Inserir Treino, 4-Listar Treino, 5-Atleta Mais Rapido, 6-Treino Mais Rapido, 9-Fim")
        return int(input("Escolha uma opção: "))

    @staticmethod
    def atleta_inserir():
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        nascimento = datetime.strptime(input("Informe o nascimento: "), "%d/%m/%Y")
        View.atleta_inserir(id, nome, nascimento)

    @staticmethod
    def atleta_listar():
        for atleta in View.atleta_listar():
            print(atleta)

    @staticmethod
    def treino_inserir():
        id = int(input("Informe o id:"))
        id_atleta = int(input("Informe o id do atleta: "))
        data = datetime.strptime(input("Informe a data: "), "%d/%m/%Y")
        dist = int(input("Informe a distancia em metros: "))
        tempo = input("Informe o tempo em hh:mm:ss: ")
        h, m, s = map(int, tempo.split(":"))
        View.treino_inserir(id, id_atleta, data, dist, timedelta(hours=h, minutes=m, seconds=s))

    @staticmethod
    def treino_listar():
        for treino in View.treino_listar():
            print(treino)

    @staticmethod
    def atleta_mais_rapido():
        print(View.atleta_mais_rapido())
    
    @staticmethod
    def treino_mais_rapido():
        id_atleta = int(input("Informe o id do atleta: "))
        print(View.treino_mais_rapido(id_atleta))

UI.main()