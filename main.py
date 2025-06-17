import pandas as pd
import streamlit as st
import plotly.express as px

# Configurações da página
st.set_page_config(
    page_title='Gapminder',
    page_icon='🌍',
    layout='wide'
)

@st.cache_data
def load_dataset():
    # Carregando os dados
    df = pd.read_csv('dataset/gapminder_data_graphs.csv')

    # Removendo as linhas com valores NaN
    df = df.dropna()

    # Retorna os dados
    return df
df = load_dataset()

# Cabeçalho
st.sidebar.header('Gapminder Dashboard 🌍')
st.sidebar.markdown('A Gapminder é uma organização educacional independente sem fins lucrativos que combate conceitos globais errôneos.')
st.sidebar.divider()

# Seleção do Ano
unique_years = df['year'].unique()
year_select  = st.selectbox(label='Ano', options=sorted(unique_years))

# Filtrados o dataset 
df_filtred = df[df['year'] == year_select]

# Continents
unique_continentes = ['Todos'] + df_filtred['continent'].unique().tolist()
continente_select  = st.sidebar.selectbox(label='Continente', options=unique_continentes)
title = 'Expectativa de vida em relação ao PIB per capita por continente'
# Filtrando novamente por continente
if continente_select != 'Todos':
    df_filtred = df_filtred[df_filtred['continent'] == continente_select]

    # Filtrando por país
    countrys = ['Todos'] + df_filtred['country'].unique().tolist()
    country  = st.sidebar.selectbox(label='País', options=countrys)
    if country != 'Todos':
        df_filtred = df_filtred[df_filtred['country'] == country]
        title = f'Expectativa de vida em relação ao PIB per capita no {country}'
        labelc1 = 'Expectativa de Vida'
        labelc2 = 'PIB per capita'
    else:
        labelc1 = 'Expectativa de Vida Média'
        labelc2 = 'PIB per capita Média'
else:
    labelc1 = 'Expectativa de Vida Média'
    labelc2 = 'PIB per capita Média'

# Indicadores globais
c1, c2 = st.columns(2)
c1.metric(label=labelc1, value=f"{df_filtred['life_exp'].mean():.2f}")
# c2.metric(label='Índice de Desenvolvimento Humano (IDH) Médio', value=f"{df_filtred['hdi_index'].mean():.2f}")
c2.metric(label=labelc2, value=f"{round(df_filtred['gdp'].mean(), 2):,}")

fig1 = px.scatter(data_frame=df_filtred, x='gdp', y='life_exp', color='continent', 
                  title=title)
# Atualizando o tamanho dos pontos
fig1.update_traces(marker=dict(size=8))
# Atualizando as labels dos eixos X e Y
st.write(fig1.update_layout(
    xaxis_title="PIB per capita",  
    yaxis_title="Expectativa de Vida"
))

# Gráfico 

# Rodapé
st.sidebar.divider()
st.sidebar.markdown('#### ©️ Desenvolvido por [Murilo Rocha](https://www.linkedin.com/in/murilo-silva-ia/)')
