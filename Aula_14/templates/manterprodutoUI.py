import streamlit as st
import pandas as pd
from view import View
import time

class ManterProdutoUI:
    def main():
        st.header("Manter Produtos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterProdutoUI.listar()

        with tab2:
            ManterProdutoUI.inserir()

        with tab3:    
            ManterProdutoUI.atualizar()

        with tab4:
            ManterProdutoUI.excluir()

    def listar():
        produtos = View.produtoListar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            dic = []
            for obj in produtos:
                dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        descricao = st.text_input("Informe a descricao: ")
        preco = st.number_input("Informe o preco: ", value=0.0, step=0.01, format="%.2f") #st.text("Informe o preco: ")
        estoque = st.number_input("Informe o estoque: ", value=0, step=1)
        categorias = View.categoriaListar()
        op = st.selectbox("Selecione a categoria", categorias, key="categoria_1")
        if st.button("Inserir"):
            View.produtoInserir(descricao, preco, estoque, op.getId())
            st.success("Produto criado com sucesso!")
            time.sleep(2)
            st.rerun()

    def atualizar():
        produtos = View.produtoListar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Selecione o produto", produtos)
            descricao = st.text_input("Informe a descricao: ", op.getDescricao())
            preco = st.number_input("Informe o preco: ", value=op.getPreco(), step=0.01, format="%.2f")
            estoque = st.number_input("Informe o estoque: ", value=op.getEstoque(), step=1)
            categorias = View.categoriaListar()
            op2 = st.selectbox("Selecione a categoria", categorias, key="categoria_2")
            if st.button("Atualizar"):
                View.produtoAtualizar(op.getId(), descricao, preco, estoque, op2.getId())
                st.success("Produto atualizado com sucesso!")
                time.sleep(2)
                st.rerun()
    
    def excluir():
        produtos = View.produtoListar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Exclusão de produto", produtos)
            if st.button("Excluir"):
                View.produtoExcluir(op.getId())
                st.success("Produto excluido com sucesso!")
                time.sleep(2)
                st.rerun()