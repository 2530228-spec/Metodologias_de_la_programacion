# Trabajando con listas 


"""
    Recorrer una lista sin importsr 
    ls csntidad de elementos que tenga
"""

magicians = ["ron", "harry", "hermione"]

print(magicians[0], magicians[1], magicians[2])

for magician in magicians:
    print(magician)
    print(magician.upper())
    print(f"{magician.title()} Ese fue un gran hechizo.")
    print(f"{magician.lower()} No podemos esperar el proximo hechizo.")

print("\nGracias a todos por participar en el show de hoy.\n")

"""
     Identacion
        La identacion es muy importante en python
        ya que nos ayuda a definir bloques de codigo.
        Un bloque de codigo es un conjunto de lineas
        que pertenecen a una misma estructura de control.

        Basicamente se utilizan 4 espacios para identar
        un bloque de codigo.
"""

# No olvidemos identar
magicians = ["ron", "harry", "hermione"]
for magician in magicians:
    print(magician)


#Herror de logica 
magicians = ["ron", "harry", "hermione"]
for magician in magicians:
    print(magician)
print(f"I can't wait to see your next trick!, {magician.title()}")

# Identacion inecesaria 
message = "Hello World!"
print(message)
