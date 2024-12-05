import streamlit as st
from retangulo import Retangulo

class RetanguloUI:
    def main():
        st.header("Calculos com retangulos")
        b = st.text_input("Informe a base")
        h = st.text_input("Informe a altura")
        
        if st.button("Calcular"):
            r = Retangulo(float(b), float(h))
            st.write(r)
            st.write(f"Area = {r.calcArea()}")
            st.write(f"Diagonal = {r.calcDiagonal()}")