import streamlit as st
from dataset import df
from utils import convert_csv, mensagem_sucesso

st.title('Dataset de Vendas')

with st.expander('Colunas'):
    colunas = st.multiselect(
        'Selecione as Colunas',
        list(df.columns),
        list(df.columns)
        )

st.sidebar.title('Filtros')
with st.sidebar.expander('Categoria do Produto'):
    categorias = st.multiselect(
        'Selecione as Categorias',
        df['Categoria do Produto'].unique(),
        df['Categoria do Produto'].unique()
        )
with st.sidebar.expander('Preço do Produto'):
    preco = st.slider(
        'Selecione o Preço',
        0, 5000,
        (0, 5000))

with st.sidebar.expander('Data da compra'):
    data_compra = st.date_input(
        'Selecione a Data',
        # Comando abaixo inicia com ( e termina com ) porque está dentro de uma tupla
      (  df['Data da Compra'].min(),
        df['Data da Compra'].max())
    )

# Criando uma query, obs: Para campos do tipo texto, usamos `` do contrário não é necessário
query = """
    `Categoria do Produto` in @categorias and \
    @preco[0] <= Preço <= Preço[1] and \
    @data_compra[0] <= `Data da Compra` <= @data_compra[1]
"""
# filtrando os registros
filtros_dados = df.query(query)
# Filtrando as colunas
filtros_dados = filtros_dados[colunas]

st.dataframe(filtros_dados)

st.markdown(f'A tabela possui :blue[{filtros_dados.shape[0]}] linhas e :blue[{filtros_dados.shape[1]}] colunas')

st.markdown('Escreva um nome do arquivo')

coluna1, coluna2 = st.columns(2)
with coluna1:
    nome_arquivo = st.text_input(
        '',
        label_visibility='collapsed'
    )
    nome_arquivo += '.csv'

with coluna2:
    st.download_button(
        'Baixar Arquivo',
        data=convert_csv(filtros_dados),
        file_name='nome_arquivo',
        mime='text/csv',
        on_click=mensagem_sucesso
    )