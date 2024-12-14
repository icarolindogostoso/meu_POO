import streamlit as st
from view import View
import time

class AdicionarRemoverProdutoNoCarrinhoUI:
    def main():
        tab1, tab2 = st.tabs(["Adicionar Produto", "Remover Produto"])
        with tab1:
            AdicionarRemoverProdutoNoCarrinhoUI.adicionarProdutoNoCarrinho()
        with tab2:
            AdicionarRemoverProdutoNoCarrinhoUI.removerProdutoNoCarrinho()

    def adicionarProdutoNoCarrinho():
        st.header("Adicionar Produto no Carrinho")
        produtos = View.produtoListar()
        for produto in produtos:
            if produto.getEstoque() == 0:
                produtos.remove(produto)
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Selecione o produto", produtos, key="produto_1")
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
        
    def removerProdutoNoCarrinho():
        st.header("Remover Produto no Carrinho")

        vendas = View.vendaListar()
        id_venda = 0
        for venda in vendas:
                if venda.getIdCliente() == st.session_state["clienteId"] and venda.getCarrinho() == True:
                    id_venda = venda.getId()

        vendaItens = View.vendaItemListar()
        for vendaitem in vendaItens:
            if vendaitem.getIdVenda() != id_venda:
                vendaItens.remove(vendaitem)
            
        if len(vendaItens) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Selecione o produto", vendaItens, key="produto_2")
            if st.button("Remover"):
                View.vendaItemExcluir(op.getId())
                View.produtoAtualizar(op.getIdProduto(), op.getDescricao(), op.getPreco(), op.getEstoque() + op.getQuantidade(), op.getIdCategoria())
                View.vendaAtualizar(id_venda, venda.getData(), venda.getCarrinho(), venda.getTotal() - (op.getPreco() * op.getQuantidade()), venda.getIdCliente())
                st.success("Produto removido do carrinho com sucesso!")
                time.sleep(2)
                st.rerun()