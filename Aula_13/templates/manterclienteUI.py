import streamlit as st
import pandas as pd
from view import View
import time

class ManterClienteUI:
    def main():
        st.header("Manter Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterClienteUI.listar()

        with tab2:
            ManterClienteUI.inserir()

        with tab3:
            ManterClienteUI.atualizar()

        with tab4:
            ManterClienteUI.excluir()

    def listar():
        clientes = View.clienteListar()

        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            dic = []
            for obj in clientes:
                dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome: ")
        email = st.text_input("Informe o email: ")
        fone = st.text_input("Informe o fone: ")
        senha = st.text_input("Informe a senha: ", type="password")
        if st.button("Inserir"):
            View.clienteInserir(nome, email, fone, senha)
            st.success("Cliente criado com sucesso!")
            time.sleep(2)
            st.rerun()

    def atualizar():
        clientes = View.clienteListar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Selecione o cliente", clientes)
            nome = st.text_input("Informe o nome: ", op.getNome())
            email = st.text_input("Informe o email: ", op.getEmail())
            fone = st.text_input("Informe o fone: ", op.getFone())
            senha = st.text_input("Informe a senha: ", op.getSenha(), type="password")
            if st.button("Atualizar"):
                View.clienteAtualizar(op.getId(), nome, email, fone, senha)
                st.success("Cliente atualizado com sucesso!")
                time.sleep(2)
                st.rerun()

    def excluir():
        clientes = View.clienteListar()
        if len(clientes) == 0: 
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Exclusão de cliente", clientes)
            if st.button("Excluir"):
                View.clienteExcluir(op.getId())
                st.success("Cliente excluido com sucesso!")
                time.sleep(2)
                st.rerun()