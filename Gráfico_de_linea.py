#aqui importamos las cosas que vamos a utilizar
import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv("coin_Bitcoin.csv")
except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")
    exit()

#aqui en esta parte nos aseguramos que las columnas si existan 
if 'Date' not in df.columns or 'Close' not in df.columns:
    print("Las columnas 'Date' o 'Close' no están en el DataFrame.")
    exit()

#aqui convertimos la columna date a tipo datetime para ordenar el dataFrame
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')

#aqui lo que hicimos es seleccionar las primeras 100 filas despues de ordenar
df = df.head(100)

#aqui extraemos las fechas y los precios
fechas = df['Date']
precio_bitcoin = df['Close']

#y por ultimo aqui usamos el grafico de lineas 
plt.plot(fechas, precio_bitcoin, marker='o', color='green')
plt.title("Evolución del Precio de Bitcoin") #este es el titulo del grafico por decirlo asi
plt.xlabel("Fecha")
plt.ylabel("Precio de Cierre (USD)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()  # Ajustar la gráfica para que no se corten las etiquetas
plt.show()
