import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o arquivo atualizado
df = pd.read_csv("ubs_atualizado.csv", sep=";")

# Contar a frequência de UBS por estado
df_freq = df['Nome_UF'].value_counts().reset_index()
df_freq.columns = ['Estado', 'Frequência']

# Criando o gráfico de pizza
grafico_pizza = px.pie(df_freq, values='Frequência', names='Estado', 
                        title='Distribuição Percentual de UBS por Estado')

# Exibindo o gráfico
st.plotly_chart(grafico_pizza)