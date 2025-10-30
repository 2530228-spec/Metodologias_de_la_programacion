"""
  Trings vaiables 
  
  Un string es de manera sencilla una serie 
  de caracteres. En Python, todo lo que se encuentre
  dentro de comillas simples (' ') o dobles (" ")
  sera considerado un string. 

  Ejemplos:
      "Esto es un string"
      'Esto tambien es un string'
 'Le dije a un amigo "Python es mi lenguaje favorito"'
 "El lenguaje 'Python' lleva el nombre por Monty Python, no por la serpiente."


"""

name = "clase de programacion"
print(name)

#title
print(name.title())

print(name)

"""
un metodo es una accion que 
Python puede ralizar en un fragmento
de datos o sobre una variable.

     El punto (.) despues de una variable 
     seguido del metodo title() dice que
     se tiene que ejecutar el metodo title ()
     de la variable.

     Todos los metodos van seguidos de parentesis
     porque en ocaciones necesitan informacion adicional
     para funcionar, la cual iría dentro de los parentecis.
     En esta ocacion, el metodo .title() no requiere informacion
     adicional para funcionar.
"""
print("Metodo upper: ", name.upper())
print("Metodo lower: ", name.lower())

#Concatenacion de STRINGS
first_name = "david"
last_name = "medellin"
full_name = first_name + " " + last_name
print("Nombre completo: ", full_name.title())

# White spaces
"""
 Un white space se refiere a cualquier caracter que no se imprime 
 es decir, un espacio, tabuladores y  finales de línea. Los white spaces
 se utilizan para organizar las salidas de tal manera que sea mas amigable 
 de leer o ver para el usuario.

    Ejemplo:
     -Tabulador: \t
     -Salto de linea: \n

"""
print("Whitespaces Tabulador")
print("Python")
print("\tPython")
print("\t\tPython")

print("Whitespaces Tabulador")
print("Lenguajes de programacion:\n\tPython\nC\n\tJavaScript")

#Eliminacion de espacioas en blanco 
programming_language = " Python "
print(programming_language)
print(programming_language.lstrip())
print(programming_language.rstrip())
print(programming_language.strip())

# Syntax Error con string
message = "Una fortaleza de python es su comunidad"
print(message)
message = 'Una fortaleza de "python" es su comunidad'