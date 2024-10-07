#aqui importamos las cosas que vamos a utilizar
import pandas as pd
import matplotlib.pyplot as plt

#aqui en es donde se carga el datase, en el cual ponemos el nombre de nuestro archivo csv
df = pd.read_csv("vgsales.csv")

#aqui seleccionamos las columnas y los 10 juegos con mas ventas
top_juegos = df[['Name', 'Global_Sales']].nlargest(10, 'Global_Sales')

#aqui en esta parte extraemos los nombres y tambien las ventas
juegos = top_juegos['Name']
ventas_globales = top_juegos['Global_Sales']

#aqui vemos que es un grafico de barra el que tenemos, y su respectivo titulo
plt.figure(figsize=(10, 6))
plt.bar(juegos, ventas_globales, color='skyblue')
plt.title("Ventas Globales de Videojuegos", fontsize=16)
plt.xlabel("Juegos", fontsize=12)
plt.ylabel("Ventas Globales (millones)", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()  
plt.show() #aqui mostramos el grafico
