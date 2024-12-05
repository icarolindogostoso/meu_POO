import streamlit as st
from equacaoUI import EquacaoUI
from retanguloUI import RetanguloUI

op = st.sidebar.selectbox("Menu", ["Retangulo", "Equação"])
if op == "Retangulo":
    RetanguloUI.main()
if op == "Equação":
    EquacaoUI.main()