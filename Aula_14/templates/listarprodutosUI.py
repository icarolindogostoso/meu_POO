import streamlit as st
import pandas as pd
from view import View

class ListarProdutosUI:
    def main():
        st.header("Listar Produtos")
        produto = View.produtoListar()
        if len(produto) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            dic = []
            for obj in produto:
                if obj.getEstoque() > 0:
                    dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)