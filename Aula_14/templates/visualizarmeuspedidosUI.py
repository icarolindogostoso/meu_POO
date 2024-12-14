import streamlit as st
import pandas as pd
from view import View

class VisualizarMeusPedidosUI:
    def main():
        st.header("Visualizar Meus Pedidos")

        vendas = View.vendaListar()
        id_venda = 0
        for venda in vendas:
                if venda.getIdCliente() == st.session_state["clienteId"] and venda.getCarrinho() == True:
                    id_venda = venda.getId()

        vendaItens = View.vendaItemListar()
        valido = False
        for vendaitem in vendaItens:
            if vendaitem.getIdVenda() == id_venda:
                valido = True
                break

        if valido == False:
            st.write("Nenhum pedido realizado")
        else:
            dic = []
            for obj in vendaItens:
                if obj.getIdVenda() == id_venda:
                    dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)