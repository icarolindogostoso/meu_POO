import streamlit as st
import pandas as pd
from view import View

class ManterClienteUI:
    @staticmethod
    def main():
        st.header("Cadastro de Clientes")
        
        tabs = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tabs[0]:
            lista = View.clienteListar()
            data = {'id': [], 'nome': [], 'email': [], 'fone': []}
            for c in lista:
                data['id'].append(c.getId())
                data['nome'].append(c.getNome())
                data['email'].append(c.getEmail())
                data['fone'].append(c.getFone())
            df = pd.DataFrame(data)
            st.write(df)

        with tabs[1]:
            nome = st.text_input("Infome o nome: ")
            email = st.text_input("Informe o email: ")
            fone = st.text_input("Informe o fone: ")
            if st.button("Inserir"):
                View.clienteInserir(nome, email, fone)

        with tabs[2]:
            lista = View.clienteListar()
            selecionado = st.selectbox("Escolha a opcao", lista)
            id = selecionado.getId()
            nome = st.text_input("Infome o nome: ", selecionado.getNome())
            email = st.text_input("Informe o email: ", selecionado.getEmail())
            fone = st.text_input("Informe o fone: ", selecionado.getFone())
            if st.button("Atualizar"):
                View.clienteAtualizar(id, nome, email, fone)

        with tabs[3]:
            lista = View.clienteListar()
            selecionado = st.selectbox("Escolha a opcao", lista)
            id = selecionado.getId()
            if st.button("Excluir"):
                View.clienteExcluir(id)