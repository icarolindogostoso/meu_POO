import streamlit as st
import pandas as pd
from view import View
import time

class VisualizarPedidosUI:
    def main():
        st.header("Todos os Pedidos")
        vendas = View.vendaListar()
        if len(vendas) == 0:
            st.write("Nenhum pedido realizado")
        else:
            dic = []
            for obj in vendas:
                dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)