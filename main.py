import pandas as pd
from repository import repository

rep = repository['data_map']

columns_map = rep['Frequencia']
old_columns = columns_map.keys()
new_columns = columns_map.values()

freq_file = 'data/freq.xls'

# Carregar o arquivo Excel em um DataFrame
freq = pd.read_excel(freq_file)

# Remover as primeiras 4 linhas (cabeçalho)
freq = freq.drop(freq.head(4).index)

# Promover a primeira linha como cabeçalho
new_header = freq.iloc[0]
freq = freq[1:] 
freq.columns = new_header
df_freq = freq[old_columns]
df_freq.columns = new_columns

# Remover as colunas com valores nulos
df_freq = df_freq.dropna(axis=1, how='all')
df_freq = df_freq.dropna()

print(df_freq)
print(df_freq.info())

_presencas = 'P'
_faltas = 'F'

new_df = {
    'Nome': [],
    'Presenças': [],
    'Faltas': [],
    'Aulas': [],
    'Frequencia': []
}

for nome in df_freq['nome']:
    print(nome)
    aluno = nome
    presencas = df_freq.loc[(df_freq['nome'] == nome) & (df_freq['presenca'] == _presencas)].shape[0]
    faltas = df_freq.loc[(df_freq['nome'] == nome) & (df_freq['presenca'] == _faltas)].shape[0]
    aulas = (presencas + faltas)

    if aulas > 0 and presencas > 0:
        frequencia = (presencas / aulas) * 100
    else:
        frequencia = 0

    temp_dict = {
        'Nome': aluno,
        'Presenças': presencas,
        'Faltas': faltas,
        'Aulas': aulas,
        'Frequencia': frequencia
    }

    new_df['Nome'].append(temp_dict['Nome'])
    new_df['Presenças'].append(temp_dict['Presenças'])
    new_df['Faltas'].append(temp_dict['Faltas'])
    new_df['Aulas'].append(temp_dict['Aulas'])
    new_df['Frequencia'].append(temp_dict['Frequencia'])

df_final = pd.DataFrame(new_df)

df_resumo = df_final.drop_duplicates(subset='Nome')

print(df_resumo)
print(df_resumo.info())

df_resumo.to_excel('frequencia.xlsx')
#TODO Mesclar df com df_cad para obter o código do aluno pelo nome.


    


