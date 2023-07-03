import pandas as pd
from repository import repository

freq_file = 'data/freq.xls'

# Carregar o arquivo Excel em um DataFrame
df_freq = pd.read_excel(freq_file)

# Remover as primeiras 4 linhas (cabeçalho)
df_freq = df_freq.drop(df_freq.head(4).index)

# Promover a primeira linha como cabeçalho
new_header = df_freq.iloc[0]
df_freq = df_freq[1:]
df_freq.columns = new_header

# Remover as colunas com valores nulos
df_selected = df_freq.dropna(axis=1, how='all')

# Exibir as primeiras linhas do DataFrame resultante
print(df_selected.head())

# Exibir informações sobre o DataFrame
print(df_selected.info())
