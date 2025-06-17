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
    # Retorna os dados
    return df
df = load_dataset()

# Cabeçalho
st.sidebar.header('Gapminder Dashboard 🌍')
st.sidebar.markdown('A Gapminder é uma organização educacional independente sem fins lucrativos que combate conceitos globais errôneos.')
st.sidebar.divider()

# Seleção do Ano
unique_years = df['year'].unique()
year_select  = st.selectbox(label='Ano', options=unique_years)

# Filtrados o dataset 
df_filtred = df[df['year'] == year_select]

# Continents
unique_continentes = ['Todos'] + df_filtred['continent'].unique().tolist()
continente_select  = st.sidebar.selectbox(label='Continente', options=unique_continentes)


# Filtrando novamente por continente
if continente_select != 'Todos':
    df_filtred = df_filtred[df_filtred['continent'] == continente_select]
else:
    pass

# Indicadores globais
c1, c2, c3 = st.columns(3)
c1.metric(label='Expectativa de Vida Média', value=f"{df_filtred['life_exp'].mean():.2f}")
c2.metric(label='Índice de Desenvolvimento Humano (IDH)', value=f"{df_filtred['hdi_index'].mean():.2f}")
c3.metric(label='PIB per capita', value=f"{df_filtred['hdi_index'].mean():.2f}")

fig1 = px.scatter(data_frame=df_filtred, x='gdp', y='life_exp', color='continent')
# Atualizando as labels dos eixos X e Y
st.write(fig1.update_layout(
    xaxis_title="PIB per capita",  
    yaxis_title="Expectativa de Vida" 
))

# Rodapé
st.sidebar.divider()
st.sidebar.markdown('#### ©️ Desenvolvido por [Murilo Rocha](https://www.linkedin.com/in/murilo-silva-ia/)')
