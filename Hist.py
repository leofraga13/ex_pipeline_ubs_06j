import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o arquivo atualizado
df = pd.read_csv("ubs_atualizado.csv", sep=";")

# Contar a frequência de UBS por município
df_municipio = df['Nome_Município'].value_counts().reset_index()
df_municipio.columns = ['Município', 'Quantidade de UBS']

min_ubs = st.slider("Número mínimo de UBS por município", 0, int(df_municipio['Quantidade de UBS'].max()), 0)

df_filtrado = df_municipio[df_municipio['Quantidade de UBS'] >= min_ubs]

# Criando o histograma
histograma = px.histogram(df_filtrado, x='Quantidade de UBS', 
                           title='Quantidade de UBS por Município',
                           labels={'Quantidade de UBS': 'Número de UBS', 'count': 'Número de Municípios'})

# Exibindo o histograma
st.plotly_chart(histograma)