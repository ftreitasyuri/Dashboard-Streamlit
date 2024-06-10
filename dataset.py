import json
import pandas as pd

file = open('dados/vendas.json')

data = json.load(file)

# print(data)

df = pd.DataFrame.from_dict(data)
# print(df['Data da Compra'].head())
# print(df.info())
# Convertendo a coluna Data da Compra pra tipo date
df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y',errors='coerce')

# print(df['Data da Compra'].dt.month_name())
# print(df.info())

file.close()

