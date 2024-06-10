import streamlit as st
import plotly.exceptions as px
from utils import format_number
from graficos import grafico_mapa_estado
from graficos import grafico_rec_mensal
from graficos import grafico_rec_estado
from graficos import grafico_rec_categoria, grafico_rec_vendedores, grafico_rec_vendas




# Trazendo os dados do arquivo dataset.py
from dataset import df

st.set_page_config(layout='wide')
st.title("Dash de vendas :shopping_trolley:")

# Sessão dos filtros
st.sidebar.title('Filtro de Vendedores')

filtro_vendedor = st.sidebar.multiselect(
    "Vendedores",
    df['Vendedor'].unique(),

)

if filtro_vendedor:
    df = df[df['Vendedor'].isin(filtro_vendedor)]

# Fim Sessão dos filtros


# Criando as abas
aba1, aba2, aba3 = st.tabs(['Dataset', 'Receitas', 'Vendedores'])

# Adicionando a tabela df na aba1
with aba1:
    st.dataframe(df)
with aba2:
    # Dividino a aba2 em 2 colunas
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Receita Total', format_number(df['Preço'].sum(), "R$"))
        st.plotly_chart(grafico_mapa_estado, use_container_width=True)
        st.plotly_chart(grafico_rec_estado, use_container_width=True)
    with coluna2:
        # A função shape conta quantos registros existem
        st.metric('Quantidade de Vendas', format_number(df.shape[0]))
        st.plotly_chart(grafico_rec_mensal, use_container_width=True)
        st.plotly_chart(grafico_rec_categoria, use_container_width=True)
with aba3:
    coluna1, coluna2 = st.columns(2)

    with coluna1:
        st.plotly_chart(grafico_rec_vendedores)
    
    with coluna2:
        st.plotly_chart(grafico_rec_vendas)