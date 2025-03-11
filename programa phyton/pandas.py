import pandas as pd

# Crear un DataFrame
data = {
    'Nombre': ['Juan', 'Ana', 'Pedro', 'Luis', 'Marta'],
    'Edad': [20, 22, 21, 23, 20],
    'Calificación': [8, 6, 9, 7, 5]
}

df = pd.DataFrame(data)

# Mostrar el DataFrame
print("DataFrame Completo:")
print(df)

# Filtrar estudiantes con calificación >= 7
print("\nEstudiantes con calificación >= 7:")
print(df[df['Calificación'] >= 7])

# Calcular el promedio de las calificaciones
promedio = df['Calificación'].mean()
print("\nPromedio de calificaciones:", promedio)