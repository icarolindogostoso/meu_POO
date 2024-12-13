import streamlit as st
from view import View
import time

class AdicionarProdutoNoCarrinhoUI:
    def main():
        st.header("Adicionar Produto no Carrinho")
        produto = View.produtoListar()
        if len(produto) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Selecione o produto", produto)
            quantidade = st.number_input("Informe a quantidade: ", value=0, step=1, key="quantidade_1")
            if st.button("Adicionar"):
                if quantidade > op.getEstoque():
                    st.error("Estoque insuficiente")
                else:
                    for venda in View.vendaListar():
                        if venda.getIdCliente() == st.session_state["clienteId"] and venda.getCarrinho() == True:
                            View.vendaItemInserir(op.getDescricao(), quantidade, op.getPreco(), venda.getId(), op.getId())
                            View.produtoAtualizar(op.getId(), op.getDescricao(), op.getPreco(), op.getEstoque() - quantidade, op.getIdCategoria())
                            View.vendaAtualizar(venda.getId(), venda.getData(), venda.getCarrinho(), venda.getTotal() + (op.getPreco() * quantidade), venda.getIdCliente())
                            st.success("Produto adicionado ao carrinho com sucesso!")
                            time.sleep(2)
                            st.rerun()