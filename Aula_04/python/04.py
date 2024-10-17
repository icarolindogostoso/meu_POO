class Entrada_Cinema:
    def __init__ (self):
        self.dia = ''
        self.hora = 0
        self.minuto = 0

    def entrada (self):
        valor = 16.00
        if self.hora >= 17 and self.hora < 24:
            valor = valor * 1.5
        if self.dia == 'Quarta':
            return 8.00
        if self.dia in ['Sexta', 'Sabado', 'Domingo']:
            return valor + 4
        return valor
        
    def meia_entrada (self):
        valor = 8.00
        if self.hora >= 17 and self.hora < 24:
            valor = valor * 1.5
        if self.dia == 'Quarta':
            return 8.00
        if self.dia in ['Sexta', 'Sabado', 'Domingo']:
            return valor + 2
        return valor
        
ec = Entrada_Cinema()
ec.dia = input("Digite o dia da sua sessão: ").title()
ec.hora, ec.minuto = map(int,input("Digite o horario da sua sessão: ").split(":"))
print(f"Valor entrada: {ec.entrada()}")
print(f"Valor meia-entrada: {ec.meia_entrada()}")