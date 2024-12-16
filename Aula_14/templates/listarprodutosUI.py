import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from view import View

class ListarProdutosUI:
    def main():
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