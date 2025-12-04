# --------------------------------------------------
# Portada
# Nombre: David Arturo Garcia Medellin
# Matrícula: 2530228
# Materia: Metodologías de la Programación
# Tarea 3: Manejo de Listas, Tuplas y Diccionarios en Python
# --------------------------------------------------

"""
Resumen Ejecutivo:
Este archivo contiene la solución de seis problemas prácticos usando las estructuras de datos básicas de Python: 
listas (list), tuplas (tuple) y diccionarios (dict). Cada problema se enfoca en manipular colecciones de datos 
de diferentes formas, utilizando operaciones como agregación, búsqueda, eliminación y cálculo. Las listas se usan 
cuando se necesita un conjunto de datos mutable, las tuplas son ideales para datos inmutables, y los diccionarios 
facilitan el almacenamiento y acceso de datos mediante claves. Además, se incluyen validaciones para asegurar la 
correcta entrada de datos y la correcta ejecución del programa.
"""

# --------------------------------------------------
# Problem 1: Shopping list basics (list operations)
# Description:
# Este programa trabaja con una lista de productos y sus cantidades. Permite agregar un nuevo producto, 
# mostrar la cantidad total de productos en la lista y verificar si un producto específico está presente.

# Inputs:
# - shopping_list_input (string; la lista inicial de productos, separada por comas; por ejemplo: "apple,banana,orange").
# - product_to_add (string; el producto que deseas agregar a la lista).
# - product_to_search (string; el producto que deseas buscar en la lista).

# Outputs:
# - "Shopping list:" <shopping_list> (muestra la lista de productos).
# - "Total items:" <len(shopping_list)> (muestra el total de productos en la lista).
# - "Found item:" true|false (informa si el producto está en la lista o no).

# Validations:
# - Verificar que shopping_list_input no esté vacío.
# - Separar los productos correctamente por comas y eliminar cualquier espacio extra.
# - Verificar que product_to_add y product_to_search no estén vacíos.

# Test cases:
# 1) Normal: shopping_list_input="apple,banana,orange", product_to_add="grape", product_to_search="banana"
# 2) Border: shopping_list_input="", product_to_add="apple", product_to_search="apple"
# 3) Error: shopping_list_input="apple,banana", product_to_add="", product_to_search="pear"

# Código:
shopping_list_input = input("Enter your shopping list (comma separated fruits/vegetables): ").strip()
shopping_list = [item.strip() for item in shopping_list_input.split(",")]

def add_product_to_list(product):
    """Función que agrega un producto a la lista de compras si no está vacío"""
    if product.strip() != "":
        shopping_list.append(product)
    return shopping_list

def search_product_in_list(product):
    """Función que verifica si un producto está en la lista de compras"""
    return product in shopping_list

# Solicita al usuario el nombre de un producto para agregar a la lista
product_to_add = input("Enter a product to add to your shopping list (e.g., 'apple'): ")
add_product_to_list(product_to_add)

# Solicita al usuario el nombre de un producto para buscar en la lista
product_to_search = input("Enter a product to search in your shopping list (e.g., 'banana'): ")
search_result = search_product_in_list(product_to_search)

# Muestra los resultados
print("Shopping list:", shopping_list)
print("Total items:", len(shopping_list))
print("Found item:", search_result)

# --------------------------------------------------
# Problem 2: Points and distances with tuples
# Description:
# Este programa usa tuplas para representar dos puntos en un plano 2D y calcula la distancia euclidiana entre ambos 
# puntos, además de calcular el punto medio entre ellos.

# Inputs:
# - x1, y1 (float; coordenadas del primer punto en el plano 2D).
# - x2, y2 (float; coordenadas del segundo punto en el plano 2D).

# Outputs:
# - "Point A:" (x1, y1) (muestra las coordenadas del primer punto).
# - "Point B:" (x2, y2) (muestra las coordenadas del segundo punto).
# - "Distance:" <distance> (muestra la distancia euclidiana entre los dos puntos).
# - "Midpoint:" (mx, my) (muestra el punto medio entre los dos puntos).

# Validations:
# - Verificar que las coordenadas (x1, y1, x2, y2) sean números flotantes.

# Test cases:
# 1) Normal: x1=1.0, y1=2.0, x2=4.0, y2=6.0
# 2) Border: x1=0.0, y1=0.0, x2=5.0, y2=5.0
# 3) Error: x1="a", y1="b", x2="c", y2="d"

# Código:
x1 = float(input("Enter x1 coordinate: "))  # Solicita la coordenada x del primer punto
y1 = float(input("Enter y1 coordinate: "))  # Solicita la coordenada y del primer punto
x2 = float(input("Enter x2 coordinate: "))  # Solicita la coordenada x del segundo punto
y2 = float(input("Enter y2 coordinate: "))  # Solicita la coordenada y del segundo punto

distance_between_points = ((x2 - x1)**2 + (y2 - y1)**2)**0.5  # Calcula la distancia euclidiana
midpoint_of_points = ((x1 + x2)/2, (y1 + y2)/2)  # Calcula el punto medio entre los dos puntos

print("Point A:", (x1, y1))
print("Point B:", (x2, y2))
print("Distance:", distance_between_points)
print("Midpoint:", midpoint_of_points)

# --------------------------------------------------
# Problem 3: Product catalog with dictionary
# Description:
# Administra un catálogo de productos usando un diccionario. Verifica si un producto existe en el catálogo 
# y calcula el total a pagar si el producto está disponible.

# Inputs:
# - product_to_buy (string; nombre del producto que el usuario quiere comprar).
# - quantity_to_buy (int; cantidad del producto que el usuario desea comprar).

# Outputs:
# - "Unit price:" <unit_price> (muestra el precio unitario del producto).
# - "Quantity:" <quantity> (muestra la cantidad que se desea comprar).
# - "Total:" <total_price> (muestra el total a pagar por la cantidad solicitada).
# - "Error: product not found" (muestra un mensaje si el producto no se encuentra).

# Validations:
# - quantity > 0.
# - Verificar que el producto exista en el diccionario.

# Test cases:
# 1) Normal: product_to_buy="apple", quantity_to_buy=2
# 2) Border: product_to_buy="orange", quantity_to_buy=0
# 3) Error: product_to_buy="grape", quantity_to_buy=3

# Código:
product_catalog = {
    "apple": 10.0, 
    "banana": 5.0, 
    "orange": 3.0
}

product_to_buy = input("Enter the product name you want to buy (e.g., 'apple'): ").strip()
quantity_to_buy = int(input(f"Enter the quantity of {product_to_buy}: "))  # Solicita la cantidad

def calculate_product_total(product, quantity):
    if product in product_catalog and quantity > 0:
        unit_price = product_catalog[product]
        total_price = unit_price * quantity
        return unit_price, quantity, total_price
    else:
        return "Error: product not found"

product_total = calculate_product_total(product_to_buy, quantity_to_buy)

if isinstance(product_total, tuple):
    print("Unit price:", product_total[0])
    print("Quantity:", product_total[1])
    print("Total:", product_total[2])
else:
    print(product_total)

# --------------------------------------------------
# Problem 4: Student grades with dict and list
# Description:
# Administra las calificaciones de estudiantes usando un diccionario donde cada clave es el nombre del estudiante 
# y cada valor es una lista de calificaciones. El programa calcula el promedio y determina si el estudiante ha 
# aprobado (promedio >= 70.0).

# Inputs:
# - student_name_to_check (string; el nombre del estudiante cuyas calificaciones se desean verificar).

# Outputs:
# - "Grades:" <grades_list> (muestra la lista de calificaciones del estudiante).
# - "Average:" <average_grade> (muestra el promedio de las calificaciones).
# - "Passed:" true|false (indica si el estudiante aprobó o no).
# - "Error: student not found" (muestra un mensaje si el estudiante no está en el diccionario).

# Validations:
# - Verificar que el nombre del estudiante esté en el diccionario.
# - Verificar que las calificaciones no estén vacías.

# Test cases:
# 1) Normal: student_name_to_check="Alice"
# 2) Border: student_name_to_check="Bob"
# 3) Error: student_name_to_check="Eve"

# Código:
student_grades = {
    "Alice": [90, 85, 88],
    "Bob": [60, 70, 80],
    "Charlie": [75, 80, 82]
}

student_name_to_check = input("Enter the student's name to check grades: ").strip()

def calculate_student_average(student_name):
    if student_name in student_grades:
        grades_list = student_grades[student_name]
        average_grade = sum(grades_list) / len(grades_list)
        passed_status = average_grade >= 70
        return grades_list, average_grade, passed_status
    else:
        return "Error: student not found"

student_info = calculate_student_average(student_name_to_check)

if isinstance(student_info, tuple):
    print("Grades:", student_info[0])
    print("Average:", student_info[1])
    print("Passed:", student_info[2])
else:
    print(student_info)

# --------------------------------------------------
# Problem 5: Word frequency counter (list + dict)
# Description:
# Cuenta la frecuencia de cada palabra en una oración, usando una lista para almacenar las palabras y un diccionario 
# para llevar el conteo de las ocurrencias.

# Inputs:
# - sentence_input (string; la oración cuya frecuencia de palabras se desea contar).

# Outputs:
# - "Words list:" <words_list> (muestra las palabras de la oración).
# - "Frequencies:" <word_frequency_dict> (muestra el conteo de cada palabra).
# - "Most common word:" <most_common_word> (muestra la palabra más frecuente).

# Validations:
# - La oración no debe estar vacía.
# - Convertir todas las palabras a minúsculas para un conteo uniforme.

# Test cases:
# 1) Normal: sentence_input="apple banana apple"
# 2) Border: sentence_input=""
# 3) Error: sentence_input="apple banana banana"

# Código:
sentence_input = input("Enter a sentence to count word frequencies: ").lower().strip()

words_list_from_sentence = sentence_input.split()
word_frequency_dict = {}

for word in words_list_from_sentence:
    word_frequency_dict[word] = word_frequency_dict.get(word, 0) + 1

most_common_word = max(word_frequency_dict, key=word_frequency_dict.get)

print("Words list:", words_list_from_sentence)
print("Frequencies:", word_frequency_dict)
print("Most common word:", most_common_word)

# --------------------------------------------------
# Problem 6: Simple contact book (dictionary CRUD)
# Description:
# Implementa un mini "contact book" usando un diccionario donde la clave es el nombre del contacto y el valor es 
# el número de teléfono. Permite agregar, buscar y eliminar contactos.

# Inputs:
# - action (string; la acción a realizar: "ADD", "SEARCH" o "DELETE").
# - contact_name (string; el nombre del contacto).
# - phone_number (string; solo para "ADD", el número de teléfono del contacto).

# Outputs:
# - "Contact saved:" name, phone (muestra el contacto guardado).
# - "Phone:" <phone> (muestra el número de teléfono del contacto).
# - "Error: contact not found" (muestra un mensaje si el contacto no existe).
# - "Contact deleted:" name (muestra el contacto eliminado).

# Validations:
# - action debe ser "ADD", "SEARCH" o "DELETE".
# - contact_name no debe estar vacío.
# - phone_number no debe estar vacío para la acción "ADD".

# Test cases:
# 1) Normal: action="ADD", contact_name="Alice", phone_number="123456789"
# 2) Border: action="SEARCH", contact_name="Bob"
# 3) Error: action="DELETE", contact_name="Charlie"

# Código:
contact_book = {"Alice": "123456789", "Bob": "987654321"}

action = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper()
contact_name = input("Enter the contact name: ").strip()

if action == "ADD":
    phone_number = input("Enter the phone number: ").strip()
    contact_book[contact_name] = phone_number
    print(f"Contact saved: {contact_name}, {phone_number}")
elif action == "SEARCH":
    print(f"Phone: {contact_book.get(contact_name, 'Error: contact not found')}")
elif action == "DELETE":
    if contact_name in contact_book:
        del contact_book[contact_name]
        print(f"Contact deleted: {contact_name}")
    else:
        print("Error: contact not found")
else:
    print("Invalid action")

# --------------------------------------------------
# Conclusiones:
# A lo largo de estos ejercicios, he aprendido a utilizar las colecciones en Python de manera efectiva. Las listas 
# son útiles cuando se necesita modificar dinámicamente el contenido de la colección. Las tuplas son ideales para datos 
# constantes que no deben cambiar, y los diccionarios proporcionan un mecanismo eficiente para asociar claves y valores 
# en situaciones donde se requiere acceso rápido a los elementos. Cada una de estas estructuras tiene su utilidad y es 
# fundamental elegir la más adecuada dependiendo del problema a resolver.

# --------------------------------------------------
# References:
# 1) Python documentation - Built-in Types: list, tuple, dict
# 2) Python tutorial – Data structures
# 3) Python documentation – Functions and methods for lists, tuples, and dictionaries
# 4) Tutoriales sobre operaciones básicas en Python
# 5) Apuntes de clase sobre estructuras de datos en Python

# --------------------------------------------------
# GitHub Repository: [Metodologias_De_La_Programacion]
