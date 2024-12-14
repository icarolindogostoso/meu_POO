import streamlit as st
from view import View
import time

class AdicionarRemoverProdutoNoCarrinhoUI:
    def main():
        tab1, tab2, tab3 = st.tabs(["Adicionar Produto", "Remover Produto Escolhido", "Atualizar Produto Escolhido"])
        with tab1:
            AdicionarRemoverProdutoNoCarrinhoUI.adicionarProdutoNoCarrinho()
        with tab2:
            AdicionarRemoverProdutoNoCarrinhoUI.removerProdutoNoCarrinho()
        with tab3:
            AdicionarRemoverProdutoNoCarrinhoUI.atualizarProdutoNoCarrinho()

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
        venda = None
        for obj in vendas:
            if obj.getIdCliente() == st.session_state["clienteId"] and obj.getCarrinho() == True:
                venda = obj

        vendaItens = []
        for vendaitem in View.vendaItemListar():
            if vendaitem.getIdVenda() == venda.getId():
                vendaItens.append(vendaitem)
            
        if len(vendaItens) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Selecione o produto", vendaItens, key="produto_2")
            if st.button("Remover"):
                produto = None
                for obj in View.produtoListar():
                    if obj.getId() == op.getIdProduto():
                        produto = obj

                View.vendaItemExcluir(op.getId())
                View.produtoAtualizar(produto.getId(), produto.getDescricao(), produto.getPreco(), produto.getEstoque() + op.getQtd(), produto.getIdCategoria())
                View.vendaAtualizar(venda.getId(), venda.getData(), venda.getCarrinho(), venda.getTotal() - (produto.getPreco() * op.getQtd()), venda.getIdCliente())
                st.success("Produto removido do carrinho com sucesso!")
                time.sleep(2)
                st.rerun()

    def atualizarProdutoNoCarrinho():
        st.header("Atualizar Produto no Carrinho")

        vendas = View.vendaListar()
        venda = None
        for obj in vendas:
            if obj.getIdCliente() == st.session_state["clienteId"] and obj.getCarrinho() == True:
                venda = obj

        vendaItens = []
        for vendaitem in View.vendaItemListar():
            if vendaitem.getIdVenda() == venda.getId():
                vendaItens.append(vendaitem)
            
        if len(vendaItens) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Selecione o produto", vendaItens, key="produto_3")
            quantidade = st.number_input("Informe a quantidade: ", value=0, step=1, key="quantidade_2")
            if st.button("Atualizar"):
                produto = None
                for obj in View.produtoListar():
                    if obj.getId() == op.getIdProduto():
                        produto = obj
                
                View.produtoAtualizar(produto.getId(), produto.getDescricao(), produto.getPreco(), produto.getEstoque() + op.getQtd(), produto.getIdCategoria())
                View.vendaAtualizar(venda.getId(), venda.getData(), venda.getCarrinho(), venda.getTotal() - (produto.getPreco() * op.getQtd()), venda.getIdCliente())

                for obj in View.produtoListar():
                    if obj.getId() == op.getIdProduto():
                        produto = obj

                if quantidade > produto.getEstoque():
                    st.error("Estoque insuficiente")
                else:
                    View.vendaItemAtualizar(op.getId(), op.getDescricao(), quantidade, op.getPreco(), op.getIdVenda(), op.getIdProduto())
                    View.produtoAtualizar(produto.getId(), produto.getDescricao(), produto.getPreco(), produto.getEstoque() - quantidade, produto.getIdCategoria())
                    View.vendaAtualizar(venda.getId(), venda.getData(), venda.getCarrinho(), venda.getTotal() + (op.getPreco() * quantidade), venda.getIdCliente())
                    st.success("Produto atualizado no carrinho com sucesso!")
                    time.sleep(2)
                    st.rerun()