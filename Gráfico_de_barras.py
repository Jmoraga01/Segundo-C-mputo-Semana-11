import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv("vgsales.csv")

# Seleccionar las columnas y los 10 juegos con más ventas
top_juegos = df[['Name', 'Global_Sales']].nlargest(10, 'Global_Sales')

# Extraer los nombres y las ventas
juegos = top_juegos['Name']
ventas_globales = top_juegos['Global_Sales']

# Gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(juegos, ventas_globales, color='skyblue')
plt.title("Ventas Globales de Videojuegos", fontsize=16)
plt.xlabel("Juegos", fontsize=12)
plt.ylabel("Ventas Globales (millones)", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()  # Ajustar para que no se corten las etiquetas
plt.show()
