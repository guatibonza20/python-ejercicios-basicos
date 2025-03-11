from mapify import Map

# Crear un mapa centrado en Madrid, España (latitud, longitud)
madrid_map = Map(center=(40.4168, -3.7038), zoom=12)

# Agregar algunos puntos de interés
madrid_map.add_marker(40.4154, -3.7074, "Plaza Mayor")
madrid_map.add_marker(40.4138, -3.6921, "Museo del Prado")
madrid_map.add_marker(40.4153, -3.6840, "Parque del Retiro")

# Guardar el mapa como archivo HTML
madrid_map.save("madrid_map.html")

print("El mapa ha sido creado y guardado como 'madrid_map.html'.")