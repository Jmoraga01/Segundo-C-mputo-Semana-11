#aqui importamos las cosas que vamos a utilizar
import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv("coin_Bitcoin.csv")
except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")
    exit()

# Asegúrate de que las columnas existen
if 'Date' not in df.columns or 'Close' not in df.columns:
    print("Las columnas 'Date' o 'Close' no están en el DataFrame.")
    exit()

# Convertir la columna 'Date' a tipo datetime y ordenar el DataFrame
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')

# Seleccionar las primeras 100 filas después de ordenar
df = df.head(100)

# Extraer fechas y precios
fechas = df['Date']
precio_bitcoin = df['Close']

# Gráfico de líneas
plt.plot(fechas, precio_bitcoin, marker='o', color='green')
plt.title("Evolución del Precio de Bitcoin")
plt.xlabel("Fecha")
plt.ylabel("Precio de Cierre (USD)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()  # Ajustar la gráfica para que no se corten las etiquetas
plt.show()
