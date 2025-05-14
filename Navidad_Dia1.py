# Las listas deben ser extraídas de los datos proporcionados.
# Para manejar esto, convertiré las filas a dos listas separadas: izquierda y derecha.

# Entrada de datos proporcionados (como un ejemplo representativo)
# Nuevos datos para calcular la distancia
# Listas proporcionadas
# Definir las listas proporcionadas
# Listas iniciales
lista_izquierda = [3, 4, 2, 1, 3, 3]
lista_derecha = [4, 3, 5, 3, 9, 3]

# Ordenar ambas listas en orden ascendente
lista_izquierda.sort()
lista_derecha.sort()

# Calcular la distancia total entre los pares
distancias = [abs(a - b) for a, b in zip(lista_izquierda, lista_derecha)]
distancia_total = sum(distancias)

# Mostrar la distancia total
print("La distancia total es:", distancia_total)

