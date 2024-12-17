import streamlit as st
import pandas as pd
from view import View

class VisualizarMeusPedidosUI:
    def main():
        st.session_state.page = "pagina1"
        st.title("Visualizar Meus Pedidos")

        venda = None
        for obj in View.vendaListar():
                if obj.getIdCliente() == st.session_state["clienteId"] and obj.getCarrinho() == True:
                    venda = obj

        valido = False
        for vendaitem in View.vendaItemListar():
            if vendaitem.getIdVenda() == venda.getId():
                valido = True
                break

        if valido == False:
            st.write("Nenhum pedido realizado")
        else:
            for vendaitem in View.vendaItemListar():
                produto = None
                for obj in View.produtoListar():
                    if obj.getId() == vendaitem.getIdProduto():
                        produto = obj
                        break

                if vendaitem.getIdVenda() == venda.getId():
                    with st.container(border=True):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.image(produto.getFoto(), width=500)
                        with col2:
                            st.header(f"Produto: {vendaitem.getNome()}")
                            st.write(f"Preço: R$ {vendaitem.getPreco():.2f}")
                            st.write(f"Quantidade: {vendaitem.getQtd()}")