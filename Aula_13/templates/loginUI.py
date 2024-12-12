import streamlit as st
from view import View

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o email: ")
        senha = st.text_input("Informe a senha: ", type="password")
        if st.button("Entrar"):
            c = View.clienteAutenticar(email, senha)
            if c == None:
                st.write("Email ou senha invalidos")
            else:
                st.session_state["clienteId"] = c["id"]
                st.session_state["clienteNome"] = c["nome"]
                st.rerun()