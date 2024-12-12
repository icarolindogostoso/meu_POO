from templates.manterclienteUI import ManterClienteUI
from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI
from view import View

import streamlit as st

class IndexUI:
    def menuVisitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema":
            LoginUI.main()
        if op == "Abrir Conta":
            AbrirContaUI.main()

    def menuAdmin():
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Categorias", "Cadastro de Produtos", "Reajustar Preços", "Visualizar Pedidos"])
        if op == "Cadastro de Clientes":
            ManterClienteUI.main()

    def menuCliente():
        op = st.sidebar.selectbox("Menu", ["Listar Produtos", "Adicionar Produto no Carrinho", "Fechar Pedido", "Ver Meus Pedidos"])
        if op == "Listar Produtos":
            View.clienteListarProduto()
        if op == "Inserir Produto no Carrinho":
            View.clienteAdicionarProduto()
        if op == "Comprar Carrinho":
            View.clenteFecharPedido()
        if op == "Ver Meus Pedidos":
            View.clienteMeusPedidos()

    def sairDoSistema():
        if st.sidebar.button("Sair"):
            del st.session_state["clienteId"]
            del st.session_state["clienteNome"]
            st.rerun()

    def sidebar():
        if "clienteId" not in st.session_state:
            IndexUI.menuVisitante()
        else:
            admin = st.session_state["clienteNome"] == "admin"
            st.sidebar.write(f"Bem-vindo(a), " + st.session_state['clienteNome'])
            if admin:
                IndexUI.menuAdmin()
            else:
                IndexUI.menuCliente()
            IndexUI.sairDoSistema()

    def main():
        View.clienteAdmin()
        IndexUI.sidebar()

IndexUI.main()