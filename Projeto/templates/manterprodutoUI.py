import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from view import View
import time

class ManterProdutoUI:
    def main():
        st.header("Manter Produtos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterProdutoUI.listar()

        with tab2:
            ManterProdutoUI.inserir()

        with tab3:    
            ManterProdutoUI.atualizar()

        with tab4:
            ManterProdutoUI.excluir()

    def listar():
        produtos = View.produtoListar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            for produto in produtos:
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
                            st.image(produto.getFoto(), width=500)
                        with col2:
                            st.header(f"{produto.getId()}. {produto.getNome()}")
                            st.write(f"Descrição: {produto.getDescricao()}")
                            st.write(f"Preco: {produto.getPreco()} - Estoque: {produto.getEstoque()}")
                    
    def inserir():
        foto = st.text_input("Informe o link da foto: ")
        nome = st.text_input("Informe o nome: ")
        descricao = st.text_input("Informe a descricao: ")
        preco = st.number_input("Informe o preco: ", value=0.0, step=0.01, format="%.2f") #st.text("Informe o preco: ")
        estoque = st.number_input("Informe o estoque: ", value=0, step=1)
        categorias = View.categoriaListar()
        op = st.selectbox("Selecione a categoria", categorias, key="categoria_1")
        if st.button("Inserir"):
            if foto == "" or nome == "" or descricao == "" or preco <= 0 or estoque <= 0 or categoria == None:
                st.error("Parametro inválido")
            else:
                View.produtoInserir(foto, nome,descricao, preco, estoque, op.getId())
                st.success("Produto criado com sucesso!")
                time.sleep(2)
                st.rerun()

    def atualizar():
        produtos = View.produtoListar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Selecione o produto", produtos)
            foto = st.text_input("Informe o link da foto: ", op.getFoto())
            nome = st.text_input("Informe o nome: ", op.getNome())
            descricao = st.text_input("Informe a descricao: ", op.getDescricao())
            preco = st.number_input("Informe o preco: ", value=op.getPreco(), step=0.01, format="%.2f")
            estoque = st.number_input("Informe o estoque: ", value=op.getEstoque(), step=1)
            categorias = View.categoriaListar()
            op2 = st.selectbox("Selecione a categoria", categorias, key="categoria_2")
            if st.button("Atualizar"):
                View.produtoAtualizar(op.getId(), foto, nome, descricao, preco, estoque, op2.getId())
                st.success("Produto atualizado com sucesso!")
                time.sleep(2)
                st.rerun()
    
    def excluir():
        produtos = View.produtoListar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Exclusão de produto", produtos)
            if st.button("Excluir"):
                View.produtoExcluir(op.getId())
                st.success("Produto excluido com sucesso!")
                time.sleep(2)
                st.rerun()