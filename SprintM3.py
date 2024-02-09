import numpy as np

import pandas as pd

# Crear el DataFrame
df = pd.DataFrame({
    'calorias': [420, 380, 390, 490, 300],
    'tiempo': [60, 40, 75, 55, 45]
}, index=['L', 'M', 'χ', 'J', 'ν'])

# Mostrar el DataFrame
print(df)


# Calcular la media, mediana y desviación típica de ambas columnas
media_calorias = df['calorias'].mean()
mediana_calorias = df['calorias'].median()
desviacion_calorias = df['calorias'].std()

media_tiempo = df['tiempo'].mean()
mediana_tiempo = df['tiempo'].median()
desviacion_tiempo = df['tiempo'].std()

# Mostrar los resultados
print("Calorias:")
print("Media:", media_calorias)
print("Mediana:", mediana_calorias)
print("Desviación típica:", desviacion_calorias)
print("\nTiempo:")
print("Media:", media_tiempo)
print("Mediana:", mediana_tiempo)
print("Desviación típica:", desviacion_tiempo)

# Añadir una nueva columna booleana al DataFrame para verificar el reto de quemar más de 400 calorías por hora
df['reto_cumplido'] = df['calorias'] *60/ df['tiempo'] > 400

# Mostrar el DataFrame resultante
print(df)


# Filtrar las filas pares del DataFrame
df_filtrado1 = df.iloc[1::2]

# Mostrar el DataFrame filtrado
print(df_filtrado1)

df_filtrado = df.iloc[1::2][df['reto_cumplido']]

print(df_filtrado)

# Contar el número de días en los que se ha conseguido y no se ha conseguido el reto
conteo_reto = df['reto_cumplido'].value_counts()

# Calcular los porcentajes de días en los que se ha conseguido y no se ha conseguido el reto
porcentaje_reto = conteo_reto / len(df) * 100

# Mostrar la serie con los porcentajes
print("Porcentaje de días en los que se ha conseguido el reto y no se ha conseguido:")
print(porcentaje_reto)


# Crear el gráfico de progresión de calorías y tiempo durante la semana
from matplotlib import pyplot as plt


plt.figure(figsize=(10, 6))
plt.plot(df.index, df['calorias'], marker='o', label='Calorías')
plt.plot(df.index  , df['tiempo'], marker='s', label='Tiempo')
plt.title('Progresión de Calorías y Tiempo durante la Semana')
plt.xlabel('Día de la Semana')
plt.ylabel('Cantidad')
plt.legend()
plt.grid(True)
plt.xticks(df.index)  # Asegurar que solo se muestren los días de la semana en el eje x
plt.tight_layout()

# Mostrar el gráfico
plt.show()      