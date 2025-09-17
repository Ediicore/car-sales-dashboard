import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la aplicación
st.title('Dashboard de Ventas de Coches Usados')
st.header('Análisis Exploratorio de Datos')

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Botón para histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

# Casillas de verificación (opcional extra - desafío adicional)
st.header('Opciones Avanzadas')
build_histogram = st.checkbox('Construir un histograma de odómetro')
build_scatter = st.checkbox('Construir gráfico de dispersión odómetro vs precio')

if build_histogram:
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write('Construir gráfico de dispersión: Odómetro vs Precio')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
