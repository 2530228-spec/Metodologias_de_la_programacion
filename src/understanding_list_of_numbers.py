"""
   Las listas tambien pueden almacenar
   numeros y de echo, son muy utilizadas
   para almacenar listas de numeros.

"""

# Metodo built-in para generar listas de numeros
"""
    el metodo range(inicio, fin, paso)
    genera una lista de numeros desde 'inicio' hasta 'fin-1'
    con un 'paso' definido.
"""

for value in range(10): # Genera numeros del 0 al 9
    print(value)

for value in range(1, 10): # Genera numeros del 1 al 9
    print(value)

print("Números Impares del 0 al 9:")
for value in range(1, 10, 2): # Genera numeros impares del 1 al 9
    print(value)
even_numbers = list(range(2, 11, 2)) # Genera una lista de numeros pares del 2 al 10
print(even_numbers)

print("Tabla del 9:")
for value in range(0,91,9):
    print(value)
tabla_del_9 = list(range(0, 91, 9))
print(tabla_del_9)

# Cuadrados de los primeros 10 numeros enteros
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)