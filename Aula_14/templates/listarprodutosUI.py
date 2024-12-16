import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import pandas as pd
from view import View

class ListarProdutosUI:
    def main():
        st.title("Listar Produtos")
        produto = View.produtoListar()
        if len(produto) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            produto = None
            for i,obj in enumerate(View.produtoListar()):
                produto = obj
            
                categoria = None
                for obj in View.categoriaListar():
                    if obj.getId() == produto.getIdCategoria():
                        categoria = obj
                
                with stylable_container(
                    key = "container",
                    css_styles = '''
                    div[data-testid="stVerticalBlockBorderWrapper"]{
                        padding: 0em 1em 1em 1em;
                        border: 2px solid rgba(80, 80, 80, 1);
                        border-radius: 0.5rem;
                    }
                    '''
                ):
                    with st.container():
                        st.header(produto.getDescricao())
                        st.subheader(categoria.getDescricao())
                        st.write(f"Estoque: {produto.getEstoque()} - Preco: {produto.getPreco()}")
                        if st.button("Comprar", key=f"comprar_{i}"):
                            st.success("Produto comprado com sucesso!")