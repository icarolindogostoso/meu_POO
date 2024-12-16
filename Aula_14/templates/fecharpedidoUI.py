import streamlit as st
from view import View
import time
from datetime import datetime

class FecharPedidoUI:
    def main():
        tab1, tab2= st.tabs(["Fechar Pedido", "Pedidos Realizados"])
        with tab1:
            FecharPedidoUI.fecharPedido()
        with tab2:
            FecharPedidoUI.pedidosRealizados()

    def fecharPedido():
        st.title("Fechar Pedido")
        vendas = View.vendaListar()
        if len(vendas) == 0:
            st.write("Nenhum pedido realizado")
        else:
            with st.container(border=True):
                cliente = None
                for obj in View.clienteListar():
                    if obj.getId() == st.session_state["clienteId"]:
                        cliente = obj

                venda = None
                for obj in vendas:
                    if obj.getIdCliente() == st.session_state["clienteId"] and obj.getCarrinho() == True:
                        venda = obj

                if venda == None:
                    st.write("Nenhum pedido ativo")
                else:
                    st.header(f"Fechar pedido {venda.getId()} de {cliente.getNome()}")
                    st.subheader(f"Total: R$ {venda.getTotal():.2f}")
                    data = venda.getData()
                    data_obj = datetime.fromisoformat(data)
                    data_formatada = data_obj.strftime("dia: %d / %m / %Y às %H horas e %M minutos")
                    if venda.getCarrinho() == True:
                        st.write(f"Carrinho Ativo - " + data_formatada)
                    else:
                        st.write("Carrinho Fechado - " + data_formatada)
                    if st.button("Fechar Pedido"):
                        if vendas[len(vendas) - 1].getTotal() == 0:
                            st.write("Nenhum pedido realizado")
                        else:
                            for venda in vendas:
                                venda.setCarrinho(False)
                                View.vendaAtualizar(venda.getId(), venda.getData(), venda.getCarrinho(), venda.getTotal(), venda.getIdCliente())
                            View.vendaInserir(True, 0, st.session_state["clienteId"])
                            st.success("Pedido fechado com sucesso!")
                            time.sleep(2)
                            st.rerun()

    def pedidosRealizados():
        st.header("Pedidos Realizados")
        vendas = View.vendaListar()
        for venda in vendas:
            if venda.getIdCliente() == st.session_state["clienteId"]:
                pass
            else:
                vendas.remove(venda)

        cliente = None
        for obj in View.clienteListar():
            if obj.getId() == st.session_state["clienteId"]:
                cliente = obj

        if len(vendas) == 0:
            st.write("Nenhum pedido realizado")
        else:
            for i, venda in enumerate(vendas):
                with st.container(border=True):
                    st.header(f"Pedido {venda.getId()} de {cliente.getNome()}")
                    st.subheader(f"Total: R$ {venda.getTotal():.2f}")
                    data = venda.getData()
                    data_obj = datetime.fromisoformat(data)
                    data_formatada = data_obj.strftime("dia: %d / %m / %Y às %H horas e %M minutos")
                    if venda.getCarrinho() == True:
                        st.write(f"Carrinho Ativo - " + data_formatada)
                    else:
                        st.write("Carrinho Fechado - " + data_formatada)
                    