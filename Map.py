import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

def load_data():
    df = pd.read_csv("ubs_atualizado.csv", sep=";", encoding="utf-8")
    df["LATITUDE"] = df["LATITUDE"].astype(str).str.replace(",", ".").astype(float)
    df["LONGITUDE"] = df["LONGITUDE"].astype(str).str.replace(",", ".").astype(float)
    return df.dropna(subset=["LATITUDE", "LONGITUDE"])

df = load_data()

if df is not None:
    st.title("Mapa Interativo das UBS por Estado")

    estados = st.multiselect("Selecione os estados", df['Nome_UF'].unique())

    if estados:
        df_filtrado = df[df['Nome_UF'].isin(estados)]
    else:
        df_filtrado = df

    mapa = folium.Map(location=[-15.793889, -47.882778], zoom_start=4)

    for index, row in df_filtrado.iterrows():
        folium.Marker(
            location=[row['LATITUDE'], row['LONGITUDE']],
            popup=f"<b>{row['NOME']}</b><br>Município: {row['Nome_Município']}<br>Estado: {row['Nome_UF']}",
            tooltip=row['NOME']
        ).add_to(mapa)

    folium_static(mapa)
else:
    st.write("Erro ao carregar os dados. Verifique o arquivo 'ubs_atualizado.csv'.")