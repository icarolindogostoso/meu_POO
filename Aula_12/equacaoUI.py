import streamlit as st
import pandas as pd
from equacao import Equacao

class EquacaoUI:
    def main():

        col1, col2 = st.columns(2)
        with col1:
            st.header("Equacao do II Grau: y = ax**2 + bx + c")
            a = st.text_input("Coeficiente a")
            b = st.text_input("Coeficiente b")
            c = st.text_input("Coeficiente c")
            n = st.text_input("Informe o numero de pontos do grafico", "5")

            if st.button("Calcular"):
                e = Equacao(float(a),float(b),float(c))
                st.write(f"Delta = {e.Delta()}")
                st.write(f"X1 = {e.X1()}")
                st.write(f"X2 = {e.X2()}")

                with col2:
                    px = []
                    py = []
                    x1 = e.X1()
                    x2 = e.X2()

                    if e.Delta() > 0:
                        d = x2 - x1
                        xmin = x1 - d/2
                        xmax = x2 + d/2

                    if e.Delta() == 0:
                        xmin = 0.5 * x1 - 1
                        xmax = 1.5 * x1 + 1
                        
                    if e.Delta() < 0:
                        xmin = 0.5 * e.XVertice()
                        xmax = 1.5 * e.XVertice()

                    if xmin == 0 and xmax == 0:
                        xmin = -5
                        xmax = 5

                    d = (xmax - xmin) / int(n)
                    x = xmin
                    while x <= xmax:
                        px.append(x)
                        py.append(e.Y(x))
                        x = x + d
                    dic = {"x" : px, "y": py}
                    chart_data = pd.DataFrame(dic)
                    st.line_chart(chart_data, x = "x", y = "y")