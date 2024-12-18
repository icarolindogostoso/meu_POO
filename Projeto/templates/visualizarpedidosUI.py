import streamlit as st
import pandas as pd
from view import View
import time
from datetime import datetime

class VisualizarPedidosUI:
    def main():
        st.title("Todos os Pedidos")
        vendas = View.vendaListar()
        if len(vendas) == 0:
            st.write("Nenhum pedido realizado")
        else:
            for venda in View.vendaListar():
                for cliente in View.clienteListar():
                    with st.container(border=True):
                        if venda.getIdCliente() == cliente.getId():
                            st.header(f"Pedido: {venda.getId()} de {cliente.getNome()}")
                            st.subheader(f"Total: R$ {venda.getTotal():.2f}")
                            data = venda.getData()
                            data_obj = datetime.fromisoformat(data)
                            data_formatada = data_obj.strftime("dia: %d / %m / %Y às %H horas e %M minutos")
                            if venda.getCarrinho() == True:
                                st.write(f"Carrinho Ativo - " + data_formatada)
                            else:
                                st.write("Carrinho Fechado - " + data_formatada)
            # dic = []
            # for obj in vendas:
            #     dic.append(obj.__dict__)
            # df = pd.DataFrame(dic)
            # st.dataframe(df)