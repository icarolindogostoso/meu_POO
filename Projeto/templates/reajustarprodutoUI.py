import streamlit as st
from view import View
import time

class ReajustarProdutoUI:
    def main():
        st.header("Reajustar Produtos")
        tab1, tab2 = st.tabs(["Reajustar Produto Especifico", "Reajustar Todos os Produtos"])
        with tab1:
            ReajustarProdutoUI.reajustarProdutoEspecifico()
        with tab2:
            ReajustarProdutoUI.reajustarTodosProdutos()

    def reajustarProdutoEspecifico():
        produtos = View.produtoListar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            produto = st.selectbox("Selecione o produto", produtos)
            percentual = st.number_input("Informe o percentual: ", value=0.0, step=0.01, format="%.2f", key="percentual_1")
            if st.button("Reajustar", key="reajustar_1"):
                View.produtoReajustarEspecifico(produto.getId(), percentual)
                st.success("Produto reajustado com sucesso!")
                time.sleep(2)
                st.rerun()

    def reajustarTodosProdutos():
        percentual = st.number_input("Informe o percentual: ", value=0.0, step=0.01, format="%.2f", key="percentual_2")
        if st.button("Reajustar", key="reajustar_2"):
            View.produtoReajustarTodos(percentual)
            st.success("Produtos reajustados com sucesso!")
            time.sleep(2)
            st.rerun()