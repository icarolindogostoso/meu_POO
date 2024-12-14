import streamlit as st
import pandas as pd
from view import View
import time

class FecharPedidoUI:
    def main():
        tab1, tab2= st.tabs(["Fechar Pedido", "Pedidos Realizados"])
        with tab1:
            FecharPedidoUI.fecharPedido()
        with tab2:
            FecharPedidoUI.pedidosRealizados()

    def fecharPedido():
        st.header("Fechar Pedido")
        vendas = View.vendaListar()
        for venda in vendas:
            if venda.getIdCliente() == st.session_state["clienteId"] and venda.getCarrinho() == True:
                pass
            else:
                vendas.remove(venda)

        if len(vendas) == 0:
            st.write("Nenhum pedido realizado")
        else:
            dic = []
            for obj in vendas:
                dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

        if st.button("Fechar Pedido"):
            if vendas[len(vendas) - 1].getTotal() == 0:
                st.write("Nenhum pedido realizado")
            else:
                for venda in vendas:
                    venda.setCarrinho(False)
                    View.vendaAtualizar(venda.getId(), venda.getData(), venda.getCarrinho(), venda.getTotal(), venda.getIdCliente())
                View.vendaInserir(True, 0, st.session_state["clienteId"])
                st.success("Pedido fechado com sucesso!")
                time.sleep(2)
                st.rerun()

    def pedidosRealizados():
        st.header("Pedidos Realizados")
        vendas = View.vendaListar()
        for venda in vendas:
            if venda.getIdCliente() == st.session_state["clienteId"]:
                pass
            else:
                vendas.remove(venda)

        if len(vendas) == 0:
            st.write("Nenhum pedido realizado")
        else:
            dic = []
            for obj in vendas:
                dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)