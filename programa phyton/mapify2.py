import pandas as pd
from mapify import Map

# Cargar los datos desde el archivo CSV
data = pd.read_csv('puntos_turisticos.csv')

# Crear un mapa centrado en Madrid
mapa = Map(center=(40.4168, -3.7038), zoom=12)

# Añadir los puntos turísticos al mapa
for _, row in data.iterrows():
    nombre = row['Nombre']
    latitud = row['Latitud']
    longitud = row['Longitud']
    descripcion = row['Descripción']
    
    # Agregar marcador con descripción
    mapa.add_marker(latitud, longitud, nombre, popup=descripcion)

# Guardar el mapa como archivo HTML
mapa.save("mapa_turistico_madrid.html")

print("El mapa con los puntos turísticos ha sido creado y guardado como 'mapa_turistico_madrid.html'.")

#/////tener en cuenta
#///Archivo CSV de ejemplo (puntos_turisticos.csv):
#////csv
#///Copiar
#////Nombre,Latitud,Longitud,Descripción
#////Plaza Mayor,40.4154,-3.7074,"Plaza histórica en el centro de Madrid"
#Museo del Prado,40.4138,-3.6921,"Museo de arte famoso en Madrid"
#/////Parque del Retiro,40.4153,-3.6840,"Parque público en Madrid con áreas verdes"
#Templo de Debod,40.5895,-3.7143,"Templo egipcio antiguo en Madrid"////