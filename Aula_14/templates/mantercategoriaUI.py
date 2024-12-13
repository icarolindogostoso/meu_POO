import streamlit as st
import pandas as pd
from view import View
import time

class ManterCategoriaUI:
    def main():
        st.header("Manter Categorias")
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
            dic = []
            for obj in categorias:
                dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        descricao = st.text_input("Informe a descricao: ")
        if st.button("Inserir"):
            View.categoriaInserir(descricao)
            st.success("Categoria criada com sucesso!")
            time.sleep(2)
            st.rerun()

    def atualizar():
        categorias = View.categoriaListar()
        if len(categorias) == 0:
            st.write("Nenhuma categoria cadastrada")
        else:
            op = st.selectbox("Selecione a categoria", categorias)
            descricao = st.text_input("Informe a descricao: ", op.getDescricao())
            if st.button("Atualizar"):
                View.categoriaAtualizar(op.getId(), descricao)
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