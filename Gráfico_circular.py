import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset.
df = pd.read_csv("world_population.csv")

# Limpiar los nombres de las columnas
df.columns = df.columns.str.strip()

# Imprimir los nombres de las columnas y las primeras filas del DataFrame
print(df.columns.tolist())
print(df.head())

# Cambia estos nombres según los que encuentres en el DataFrame
try:
    continentes = df['Continent']  # Cambia este nombre si es necesario
    población = df['2022 Population']  # Cambia este nombre si es necesario

    # Verificar si hay datos nulos
    print(df.isnull().sum())

    # Agrupar por continente y sumar la población
    df_grouped = df.groupby('Continent')['2022 Population'].sum().reset_index()

    # Ordenar los datos por población
    df_grouped = df_grouped.sort_values(by='2022 Population', ascending=False)

    # Gráfico circular
    plt.figure(figsize=(10, 6))
    wedges, texts, autotexts = plt.pie(df_grouped['2022 Population'], 
                                        labels=df_grouped['Continent'],
                                        autopct='%1.1f%%', 
                                        startangle=140, 
                                        colors=plt.cm.tab20.colors,
                                        wedgeprops=dict(edgecolor='white'))

    # Formatear el gráfico
    plt.setp(autotexts, size=10, weight='bold', color='white')
    plt.setp(texts, size=12)

    plt.title("Distribución de la Población Mundial por Continentes", fontsize=16)
    plt.axis('equal')  # Para que el gráfico sea un círculo
    plt.show()

except KeyError as e:
    print(f"Error: {e}. Asegúrate de que los nombres de las columnas sean correctos.")
