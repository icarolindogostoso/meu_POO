import streamlit as st
from view import View
import time

class ManterCategoriaUI:
    def main():
        st.title("Manter Categorias")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterCategoriaUI.listar()

        with tab2:
            ManterCategoriaUI.inserir()

        with tab3:
            ManterCategoriaUI.atualizar()

        with tab4:
            ManterCategoriaUI.excluir()

    def listar():
        categorias = View.categoriaListar()
        if len(categorias) == 0:
            st.write("Nenhuma categoria cadastrada")
        else:
            for caterogia in categorias:
                with st.container(border=True):
                    st.header(f"{caterogia.getId()}. {caterogia.getNome()}")
                    st.write(f"Descrição: {caterogia.getDescricao()}")


    def inserir():
        nome = st.text_input("Informe o nome: ")
        descricao = st.text_input("Informe a descricao: ")
        if st.button("Inserir"):
            View.categoriaInserir(nome, descricao)
            st.success("Categoria criada com sucesso!")
            time.sleep(2)
            st.rerun()

    def atualizar():
        categorias = View.categoriaListar()
        if len(categorias) == 0:
            st.write("Nenhuma categoria cadastrada")
        else:
            op = st.selectbox("Selecione a categoria", categorias)
            nome = st.text_input("Informe o nome: ", op.getNome())
            descricao = st.text_input("Informe a descricao: ", op.getDescricao())
            if st.button("Atualizar"):
                View.categoriaAtualizar(op.getId(), nome, descricao)
                st.success("Categoria atualizada com sucesso!")
                time.sleep(2)
                st.rerun()

    def excluir():
        categorias = View.categoriaListar()
        if len(categorias) == 0:
            st.write("Nenhuma categoria cadastrada")
        else:
            op = st.selectbox("Exclusão de categoria", categorias)
            if st.button("Excluir"):
                View.categoriaExcluir(op.getId())
                st.success("Categoria excluida com sucesso!")
                time.sleep(2)
                st.rerun()