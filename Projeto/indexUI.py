from templates.abrircontaUI import AbrirContaUI
from templates.adicionarremoverprodutonocarrinhoUI import AdicionarRemoverProdutoNoCarrinhoUI
from templates.fecharpedidoUI import FecharPedidoUI
from templates.listarprodutosUI import ListarProdutosUI
from templates.loginUI import LoginUI
from templates.mantercategoriaUI import ManterCategoriaUI
from templates.manterclienteUI import ManterClienteUI
from templates.manterprodutoUI import ManterProdutoUI
from templates.reajustarprodutoUI import ReajustarProdutoUI
from templates.visualizarmeuspedidosUI import VisualizarMeusPedidosUI
from templates.visualizarpedidosUI import VisualizarPedidosUI

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
        if op == "Cadastro de Categorias":
            ManterCategoriaUI.main()
        if op == "Cadastro de Produtos":
            ManterProdutoUI.main()
        if op == "Reajustar Preços":
            ReajustarProdutoUI.main()
        if op == "Visualizar Pedidos":
            VisualizarPedidosUI.main()

    def menuCliente():
        View.vendaInserir(True, 0, st.session_state["clienteId"])
        op = st.sidebar.selectbox("Menu", ["Listar Produtos", "Adicionar / Remover Produto no Carrinho", "Fechar Pedido", "Ver Meus Pedidos"])
        if op == "Listar Produtos":
            ListarProdutosUI.main()
        if op == "Adicionar / Remover Produto no Carrinho":
            AdicionarRemoverProdutoNoCarrinhoUI.main()
        if op == "Fechar Pedido":
            FecharPedidoUI.main()
        if op == "Ver Meus Pedidos":
            VisualizarMeusPedidosUI.main()

    def sairDoSistema():
        if st.sidebar.button("Sair"):
            View.vendaFechar(st.session_state["clienteId"])
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