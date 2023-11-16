# Importamos librerias necesarias para proyecto
import pandas as pd
import plotly.express as px
import streamlit as st
"""
    Ejecutamos la lectura de los archivos que nos permitirán ejecutar el análisis del proyecto
"""
car_data = pd.read_csv('./notebooks/vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
