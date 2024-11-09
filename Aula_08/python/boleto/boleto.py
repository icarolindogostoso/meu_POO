from pagamento import Pagamento

class Boleto:
    def __init__ (self, cod, emissao, venc, valor):
        self.__codBarras = cod
        self.__dateEmissao = emissao
        self.__dateVencimento = venc
        self.__valorBoleto = valor
        self.__valorPago = 0
        self.__situacaoPagamento = Pagamento.emAberto

    def pagar (self, valorPago):
        if valorPago > 0:
            self.__valorPago = valorPago
        else:
            raise ValueError ("Valor invalido")
    
    def situacao (self):
        if self.__valorPago >= self.__valorBoleto:
            return Pagamento.pago
        elif self.__valorPago > 0:
            return Pagamento.pagoParcial
        else:
            return Pagamento.emAberto
        
    def __str__ (self):
        situacao = self.situacao()
        situacao_str = {Pagamento.emAberto: "Em aberto", Pagamento.pagoParcial: "Pago parcial", Pagamento.pago: "Pago"}.get(situacao)
        return f"{self.__codBarras} - {self.__dateEmissao.date()} - {self.__dateVencimento.date()} - {self.__valorBoleto} - {self.__valorPago} - {situacao_str}"