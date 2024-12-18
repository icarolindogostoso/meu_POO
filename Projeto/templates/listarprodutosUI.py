import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from view import View
import time

class ListarProdutosUI:
    def main():
        if 'page' not in st.session_state:
            st.session_state.page = "pagina1"

        if st.session_state.page == "pagina1":
            st.title("Listar Produtos")
            produto = View.produtoListar()
            if len(produto) == 0:
                st.write("Nenhum produto cadastrado")
            else:
                categoria = None
                for obj in View.categoriaListar():
                    categoria = obj

                    st.header(categoria.getNome())

                    for i,obj in enumerate(View.produtoListar()):
                        if obj.getIdCategoria() == categoria.getId():
                            
                            with stylable_container(
                                key = "container",
                                css_styles = '''
                                img{
                                    width: 350px;   /* Largura específica */
                                    height: 250px;
                                }
                                '''
                            ):
                                with st.container(border=True):
                                    col1, col2 = st.columns(2)
                                    with col1:
                                        st.image(obj.getFoto(), width=500)
                                    with col2:
                                        st.subheader(f"{obj.getId()}. {obj.getNome()}")
                                        st.write(obj.getDescricao())
                                        st.write(f"Estoque: {obj.getEstoque()} - Preco: {obj.getPreco()}")
                                        if st.button("Comprar", key=f"comprar_{i}"):
                                            st.session_state.page = "pagina2"
                                            st.session_state.produtoId = obj.getId()
                                            st.rerun()


        if st.session_state.page == "pagina2":
            st.title("Comprar Produto")
            produto = None
            for obj in View.produtoListar():
                if obj.getId() == st.session_state.produtoId:
                    produto = obj
                    
            with stylable_container(
                key = "container",
                css_styles = '''
                img{
                    width: 50px;   /* Largura específica */
                    height: 295px;
                }
                '''
            ):
                col1, col2 = st.columns(2)
                with col1:
                    st.image(produto.getFoto(), width=500)
                with col2:
                    categoria = None
                    for objeto in View.categoriaListar():
                        if produto.getIdCategoria() == objeto.getId():
                            categoria = objeto
                            break
                    
                    with st.container(border=True): 
                        st.header(f"{produto.getId()}. {produto.getNome()}")
                        st.write(produto.getDescricao())
                        st.subheader(f"{categoria.getNome()}")
                        st.write(categoria.getDescricao())
                        st.write(f"Estoque: {produto.getEstoque()} - Preco: {produto.getPreco()}")
                        quantidade = st.number_input("Informe a quantidade: ", value=0, step=1, key="quantidade")
                        if st.button("Comprar", key="comprar"):
                            if quantidade <= 0:
                                st.error("Quantidade invalida")
                            else:
                                for venda in View.vendaListar():
                                    if venda.getIdCliente() == st.session_state["clienteId"] and venda.getCarrinho() == True:
                                        View.vendaItemInserir(produto.getNome(), quantidade, produto.getPreco(), venda.getId(), produto.getId())
                                        View.produtoAtualizar(produto.getId(), produto.getFoto(), produto.getNome(), produto.getDescricao(), produto.getPreco(), produto.getEstoque() - quantidade, produto.getIdCategoria())
                                        View.vendaAtualizar(venda.getId(), venda.getData(), venda.getCarrinho(), venda.getTotal() + (produto.getPreco() * quantidade), venda.getIdCliente())
                                        st.success("Produto adicionado ao carrinho com sucesso!")
                                        time.sleep(2)
                                        st.rerun()
                                        st.session_state.page = "pagina1"