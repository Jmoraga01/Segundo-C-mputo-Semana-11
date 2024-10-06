#aqui importamos las cosas que vamos a utilizar
import pandas as pd
import matplotlib.pyplot as plt


#aqui en es donde se carga el datase
df = pd.read_csv("world_population.csv")

#esta linea de codigo es para limpiar los nombres de las columnas
df.columns = df.columns.str.strip()

#aqui es donde imprimimos ya sea los nombres de las columnas y las primeras filas del DataFrame
print(df.columns.tolist())
print(df.head())

#en esta línea de código es es donde nosotros podemos
#cambiar los nombres según lo que encontremos en este DataFrame
try:
    continentes = df['Continent']  
    población = df['2022 Population'] 

    #aqui verificamos si hay datos nulos
    print(df.isnull().sum())

    #aqui podemos ya sea agrupor por continente y tambien sumar la poblacion
    df_grouped = df.groupby('Continent')['2022 Population'].sum().reset_index()

    #aqui ordenamos los datos por poblacion
    df_grouped = df_grouped.sort_values(by='2022 Population', ascending=False)

    #en este podemos ver que es un grfico circular
    plt.figure(figsize=(10, 6))
    wedges, texts, autotexts = plt.pie(df_grouped['2022 Population'], 
                                        labels=df_grouped['Continent'],
                                        autopct='%1.1f%%', 
                                        startangle=140, 
                                        colors=plt.cm.tab20.colors,
                                        wedgeprops=dict(edgecolor='white'))

    plt.setp(autotexts, size=10, weight='bold', color='white')
    plt.setp(texts, size=12)

    plt.title("Distribución de la Población Mundial por Continentes", fontsize=16)
    plt.axis('equal')  #esta lo ponemos para que el gráfico sea un círculo
    plt.show()

except KeyError as e:
    print(f"Error: {e}. Asegúrate de que los nombres de las columnas sean correctos.")
