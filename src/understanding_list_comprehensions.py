"""
squares = []
for value in range(0, 11):
    squares.append(value ** 2)
    squares.append(square)
print(squares)

"""
"""
   Una list comprehension conbina el ciclo for
   y la creacion de elementos en una sola linea.
   y automaticamente genera cada nuevo elemento
   a la lista, es decir, sin utilizar el metodo append.

"""
squares = [value ** 2 for value in range(0, 11)]
print(squares)

# Para generar los números pares del 1 al 100 
squares_if = [value for value in range(0, 101) if value % 2 == 0]
print(squares_if)
