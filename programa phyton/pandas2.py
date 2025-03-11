import pandas as pd

# Crear el DataFrame con datos de ventas
data = {
    'Fecha': ['2023-03-01', '2023-03-02', '2023-03-03', '2023-03-04', '2023-03-05'],
    'Producto': ['Camiseta', 'Pantalón', 'Camiseta', 'Zapatos', 'Pantalón'],
    'Cantidad Vendida': [10, 5, 12, 3, 7],
    'Precio Unitario': [15, 30, 15, 50, 30],
    'Ciudad': ['Madrid', 'Madrid', 'Barcelona', 'Barcelona', 'Madrid']
}

# Crear el DataFrame
df = pd.DataFrame(data)

# Convertir la columna 'Fecha' a tipo datetime
df['Fecha'] = pd.to_datetime(df['Fecha'])

# Filtrar ventas por ciudad
ciudad_especifica = 'Madrid'
ventas_ciudad = df[df['Ciudad'] == ciudad_especifica]

# Calcular la venta total por cada producto (Cantidad Vendida * Precio Unitario)
df['Venta Total'] = df['Cantidad Vendida'] * df['Precio Unitario']

# Mostrar las ventas totales por ciudad
ventas_por_ciudad = df.groupby('Ciudad')['Venta Total'].sum()
print("Ventas Totales por Ciudad:")
print(ventas_por_ciudad)

# Mostrar las 3 fechas con mayores ventas
top_3_fechas = df.groupby('Fecha')['Venta Total'].sum().sort_values(ascending=False).head(3)
print("\nLas 3 fechas con mayores ventas:")
print(top_3_fechas)