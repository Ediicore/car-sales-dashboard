import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración
plt.style.use('ggplot')
pd.set_option('display.max_columns', None)
print("=== INICIANDO ANÁLISIS EDA ===\n")

# 1. Cargar datos
print("1. CARGANDO DATOS...")
df = pd.read_csv('data/vehicles_us.csv')
print(f"Dataset shape: {df.shape}")
print("\nPrimeras 5 filas:")
print(df.head())
print("\n" + "="*50 + "\n")

# 2. Información del dataset
print("2. INFORMACIÓN DEL DATASET:")
print(df.info())
print("\nValores nulos por columna:")
print(df.isnull().sum())
print("\nEstadísticas descriptivas:")
print(df.describe())
print("\n" + "="*50 + "\n")

# 3. Análisis de precios
print("3. ANÁLISIS DE PRECIOS...")
plt.figure(figsize=(10, 6))
plt.hist(df['price'], bins=20, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('Distribución de Precios de Vehículos')
plt.xlabel('Precio ($)')
plt.ylabel('Frecuencia')
plt.grid(True, alpha=0.3)
plt.savefig('price_distribution.png')
plt.close()  # Cerrar la figura para no mostrar en terminal
print("Gráfica de distribución de precios guardada como 'price_distribution.png'")

# 4. Precio por modelo
print("4. PRECIO POR MODELO...")
plt.figure(figsize=(12, 6))
df.groupby('model')['price'].mean().sort_values(ascending=False).plot(kind='bar', color='orange')
plt.title('Precio Promedio por Modelo')
plt.xlabel('Modelo')
plt.ylabel('Precio Promedio ($)')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('price_by_model.png')
plt.close()
print("Gráfica de precio por modelo guardada como 'price_by_model.png'")

# 5. Correlaciones
print("5. ANÁLISIS DE CORRELACIONES...")
numeric_cols = df.select_dtypes(include=[np.number]).columns
print(f"Columnas numéricas: {numeric_cols.tolist()}")

if len(numeric_cols) > 1:
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', center=0)
    plt.title('Matriz de Correlación')
    plt.tight_layout()
    plt.savefig('correlation_matrix.png')
    plt.close()
    print("Matriz de correlación guardada como 'correlation_matrix.png'")
else:
    print("No hay suficientes columnas numéricas para la matriz de correlación")

# 6. Análisis de transmisión
print("6. ANÁLISIS DE TRANSMISIÓN...")
if 'transmission' in df.columns:
    transmission_counts = df['transmission'].value_counts()
    print("\nDistribución por transmisión:")
    print(transmission_counts)
    
    plt.figure(figsize=(8, 6))
    transmission_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title('Distribución por Tipo de Transmisión')
    plt.ylabel('')
    plt.savefig('transmission_distribution.png')
    plt.close()
    print("Gráfica de distribución de transmisión guardada")

# 7. Conclusiones
print("\n7. CONCLUSIONES:")
print("\n=== RESUMEN DEL ANÁLISIS ===")
print(f"• Total de vehículos: {len(df)}")
print(f"• Precio promedio: ${df['price'].mean():,.2f}")
print(f"• Precio mínimo: ${df['price'].min():,}")
print(f"• Precio máximo: ${df['price'].max():,}")
print(f"• Modelos únicos: {df['model'].nunique()}")

print("\n=== RECOMENDACIONES PARA EL DASHBOARD ===")
print("1. Incluir filtros por: modelo, año, precio, transmisión")
print("2. Mostrar métricas clave: precios promedios, conteos por modelo")
print("3. Visualizar distribuciones: histogramas, gráficas de barras")
print("4. Destacar relaciones entre variables clave")

print("\n=== GRÁFICAS GENERADAS ===")
print("✓ price_distribution.png - Distribución de precios")
print("✓ price_by_model.png - Precio promedio por modelo")
if len(numeric_cols) > 1:
    print("✓ correlation_matrix.png - Matriz de correlación")
if 'transmission' in df.columns:
    print("✓ transmission_distribution.png - Distribución de transmisión")

print("\n=== ANÁLISIS COMPLETADO ===\n")
