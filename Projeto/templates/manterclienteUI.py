import streamlit as st
import pandas as pd
from view import View
import time

class ManterClienteUI:
    def main():
        st.title("Manter Clientes")
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
            for cliente in clientes:
                with st.container(border=True):
                    st.header(f"{cliente.getId()}. {cliente.getNome()}")
                    st.subheader(f"Email: {cliente.getEmail()}")
                    st.write(f"Fone: {cliente.getFone()} - Senha: {cliente.getSenha()}")


    def inserir():
        nome = st.text_input("Informe o nome: ")
        email = st.text_input("Informe o email: ")
        fone = st.text_input("Informe o fone: ")
        senha = st.text_input("Informe a senha: ", type="password")
        if st.button("Inserir"):
            if nome == "" or email == "" or fone == "" or senha == "":
                st.error("Parametro inválido")
            else:
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