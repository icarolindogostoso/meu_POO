import streamlit as st
import pandas as pd
from view import View

class VisualizarMeusPedidosUI:
    def main():
        st.header("Visualizar Meus Pedidos")
        vendaItem = View.vendaItemListar()
        if len(vendaItem) == 0:
            st.write("Nenhum pedido realizado")
        else:
            dic = []
            vendas = View.vendaListar()
            for venda in vendas:
                if venda.getIdCliente() == st.session_state["clienteId"] and venda.getCarrinho() == True:
                    id_venda = venda.getId()
            for obj in vendaItem:
                if obj.getIdVenda() == id_venda:
                    dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)