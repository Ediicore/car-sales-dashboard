import pandas as pd
import plotly.express as px
import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Dashboard de Autos", layout="wide")

# Título
st.title("🚗 Dashboard de Análisis de Autos Usados")
st.markdown("---")

# Cargar datos
@st.cache_data
def load_data():
    return pd.read_csv('vehicles_us.csv')

df = load_data()

# Sidebar con filtros
st.sidebar.header("🔧 Filtros")
manufacturers = df['model'].dropna().unique()
selected_manufacturers = st.sidebar.multiselect(
    'Seleccionar Marcas',
    options=sorted(manufacturers),
    default=manufacturers[:2] if len(manufacturers) > 2 else manufacturers
)

# Aplicar filtros
filtered_df = df[df['model'].isin(selected_manufacturers)] if selected_manufacturers else df

# Métricas principales
st.header("📊 Métricas Principales")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total de Vehículos", len(filtered_df))
with col2:
    st.metric("Precio Promedio", f"${filtered_df['price'].mean():,.0f}")
with col3:
    st.metric("Año Promedio", f"{filtered_df['model_year'].mean():.0f}")
with col4:
    st.metric("Condición Principal", filtered_df['condition'].mode()[0] if not filtered_df.empty else "N/A")

# Gráficas principales
st.header("📈 Visualizaciones")

# 1. Histograma de precios
st.subheader("Distribución de Precios")
fig1 = px.histogram(filtered_df, x='price', nbins=20, 
                   title='Distribución de Precios de Vehículos')
st.plotly_chart(fig1, use_container_width=True)

# 2. Gráfico de dispersión año vs precio
st.subheader("Relación: Año vs Precio")
fig2 = px.scatter(filtered_df, x='model_year', y='price', color='model',
                 title='Año del Modelo vs Precio',
                 labels={'model_year': 'Año del Modelo', 'price': 'Precio ($)'})
st.plotly_chart(fig2, use_container_width=True)

# 3. Comparación entre marcas (como en tus imágenes)
st.subheader("Comparación de Precios entre Marcas")
if len(selected_manufacturers) >= 2:
    col1, col2 = st.columns(2)
    with col1:
        manuf1 = st.selectbox("Seleccionar Marca 1", options=selected_manufacturers)
    with col2:
        manuf2 = st.selectbox("Seleccionar Marca 2", 
                             options=[m for m in selected_manufacturers if m != manuf1])
    
    # Histograma comparativo
    compare_df = filtered_df[filtered_df['model'].isin([manuf1, manuf2])]
    fig3 = px.histogram(compare_df, x='price', color='model', barmode='overlay',
                       title=f'Comparación de Precios: {manuf1} vs {manuf2}')
    st.plotly_chart(fig3, use_container_width=True)

# 4. Condición vs Año del modelo
st.subheader("Condición vs Año del Modelo")
fig4 = px.histogram(filtered_df, x='model_year', color='condition',
                   title='Distribución de Condición por Año',
                   labels={'model_year': 'Año del Modelo'})
st.plotly_chart(fig4, use_container_width=True)

# 5. Tabla de datos
st.header("📋 Datos Filtrados")
st.dataframe(filtered_df[['price', 'model_year', 'model', 'condition', 'cylinders', 'fuel']].head(20))

# Botones originales (para cumplir con el proyecto)
st.header("🎯 Funcionalidades Requeridas")
hist_button = st.button('Construir histograma de odómetro')
scatter_button = st.button('Construir gráfico de dispersión odómetro vs precio')

if hist_button:
    fig = px.histogram(filtered_df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:
    fig = px.scatter(filtered_df, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("**Dashboard desarrollado para el Sprint 7**")
