import time
from dataset import df
import pandas as pd
import streamlit as st


# Função para formatar valores monetários
def format_number(value, prefix = ''):
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f}{unit}'
        
        value /= 1000
    
    return f'{prefix} {value:.2f} milhões'

# -------------------------------------------------------------------------------------------------------------------
# Construindo a dataFrme de receita por estado e somando o valor total de cada estado
df_rec_estado = df.groupby('Local da compra')[['Preço']].sum()

# Removendo duplicados e criando 
df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra','lat', 'lon']].\
                merge(df_rec_estado, left_on='Local da compra', right_index=True).sort_values('Preço', ascending=False)

# print(df_rec_estado)
# -------------------------------------------------------------------------------------------------------------------




# -------------------------------------------------------------------------------------------------------------------
# Construindo a dataFrme de Receita mensal
df_rec_mensal = df.set_index('Data da Compra').groupby(pd.Grouper(freq='ME'))['Preço'].sum().reset_index()

# Extraindo o mês e o ano da coluna Dada da compra (OBS: Para fazer essa operação a coluna deve ser passada para datetime)
df_rec_mensal['Ano'] = df_rec_mensal['Data da Compra'].dt.year
df_rec_mensal['Mes'] = df_rec_mensal['Data da Compra'].dt.month_name()
# print(df_rec_mensal.head())
# -------------------------------------------------------------------------------------------------------------------

# Criando um grafico mostrando todas as categorias e suas receitas totais

df_rec_categoria = df.groupby('Categoria do Produto')[['Preço']].sum().sort_values('Preço', ascending=False)

# print(df_rec_categoria.head())


# Criando o df de vendedores. trazendos o nome, o valor total que foi vendido por cada um e quantas vendas cada um fez
df_vendedores = pd.DataFrame(df.groupby('Vendedor')['Preço'].agg(['sum', 'count']))

# print(df_vendedores)

# Função para converte arquivos CSV

@st.cache_data
def convert_csv(dados):
    return dados.to_csv(index=False, encoding='utf-8')
    

def mensagem_sucesso():
    success = st.success(
        'Arquivo baixado com sucesso'
        #  icon='check'
        )   
    time.sleep(3)
    success.empty()