# Lists

"""
   Las listas son elementos mutables,
   es decir, que pueden cambiar su contenido

   Las listas nos permiten almasenar información
   en un luga, la cantidad de informacion
   que tengas: ya sean pocos elementos o millones
   de elementos.

   Se recomienda nombrar una variable de tipo lista
   en plural. 

   En python los corchetes ( [ ] ) definen una lista,
   sus elementos van separados por comas.
   Ejemplo:
"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized', 'giant']
print(bicycles)

print(bicycles[0].title())

# Los indices comienzan en 0 y terminan en n-1, donde n es la cantidad de elementos.

print(bicycles[4].title())

# Acceder al ultimo elemento de una lista.
print(bicycles[-1].title()) # Acceder al ultimo elemento.
print(bicycles[-2].title()) # Acceder al penultimo elemento.
print(bicycles[-5].title()) # Acceder al primer elemento.

# Utilizando valores de la lista
message = "Mi bicicleta favorita es la " + bicycles[4].upper() + "."
print(message)

message_f = f"Mi bicicleta favorita es la {bicycles[4].title()}."
print(message_f)

# Agregar elementos a una lista
print("\n")
print("Agregar elementos a una lista:")
print(bicycles)

print("Agregar un elemento al final de la lista:")
bicycles.append('ducatti')
print(bicycles)