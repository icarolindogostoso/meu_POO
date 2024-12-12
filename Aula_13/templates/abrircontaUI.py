import streamlit as st
from view import View
import time

class AbrirContaUI:
    def main():
        st.header("Abrir Conta no Sistema")
        AbrirContaUI.inserir()

    def inserir():
        nome = st.text_input("Infome o nome: ")
        email = st.text_input("Informe o email: ")
        fone = st.text_input("Informe o fone: ")
        senha = st.text_input("Informe a senha: ", type="password")
        if st.button("Inserir"):
            View.clienteInserir(nome, email, fone, senha)
            st.success("Conta criada com sucesso!")
            time.sleep(2)
            st.rerun()