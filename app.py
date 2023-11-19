import pandas as pd
import plotly.express as px
import streamlit as st

# Carga de datos (asegúrate de que la ruta al archivo CSV sea la correcta)
car_data = pd.read_csv('./notebooks/vehicles_us.csv')

# Creación del título y descripción en la app web
st.header("Web App - Data Visualization")
st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
st.write('Seleccione alguna de las opciones que siguen:')

# Creación de checkboxes para selección de histogramas
check1 = st.checkbox("Crear histograma según 'paint_color'")
check2 = st.checkbox("Crear histograma según 'condition'")
check3 = st.checkbox("Crear histograma según 'type'")
check4 = st.checkbox("Crear histograma según 'fuel")

# Lista para almacenar los gráficos seleccionados
selected_charts = []

# Creación de histogramas basados en las selecciones de los checkboxes
if check1:
    fig1 = px.histogram(car_data, x="paint_color", color="paint_color",
                        title="Distribución de vehículos por color.")
    selected_charts.append(fig1)
if check2:
    fig2 = px.histogram(car_data, x="condition", color="condition",
                        title="Distribución de vehículos por estado.")
    selected_charts.append(fig2)
if check3:
    fig3 = px.histogram(car_data, x="type", color="type",
                        title="Distribución de vehículos por tipo.")
    selected_charts.append(fig3)
if check4:
    fig4 = px.histogram(car_data, x="fuel", color="fuel",
                        title="Distribución de vehículos por combustible utilizado.")
    selected_charts.append(fig4)

# Mostrar los histogramas seleccionados
for fig in selected_charts:
    st.plotly_chart(fig, use_container_width=True)

# Mensaje y gráficos adicionales
st.header("Web App - Análisis adicional")

# Menú desplegable para seleccionar el gráfico
option = st.selectbox(
    'Selecciona el gráfico que deseas visualizar:',
    ('Distribución del Kilometraje', 'Kilometraje vs Precio', 'Distribución de días de publicación',
     'Tiempo Medio de Publicación por tipo de vehículo y Condición')
)

# Visualización del gráfico seleccionado
if option == 'Distribución del Kilometraje':
    fig = px.histogram(car_data, x='odometer',
                       color='odometer',
                       title='Distribución del Kilometraje')
    st.plotly_chart(fig, use_container_width=True)

elif option == 'Kilometraje vs Precio':
    fig = px.scatter(car_data, x='odometer', y='price',
                     color='price',
                     title='Kilometraje vs Precio')
    st.plotly_chart(fig, use_container_width=True)

elif option == 'Tipo de vehículo v/s Precio':
    fig = px.scatter(car_data, x='type', y='price',
                     color='price',
                     title='Tipo vs Precio')
    st.plotly_chart(fig, use_container_width=True)

elif option == 'Tiempo Medio de Publicación por Modelo y Condición':
    grouped_data = car_data.groupby(['model', 'condition'])[
        'days_listed'].mean().reset_index()
    fig = px.bar(grouped_data, x='model', y='days_listed', color='condition',
                 barmode='group', title='Tiempo Medio de Publicación por Modelo y Condición')
    st.plotly_chart(fig, use_container_width=True)
