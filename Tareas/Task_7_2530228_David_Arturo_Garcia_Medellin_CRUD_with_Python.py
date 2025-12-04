# --------------------------------------------------
# Portada
# Nombre: David Arturo Garcia Medellin
# Matrícula: 2530228
# Fecha: 26 de junio de 2024
# Grupo: IM 1-3
# --------------------------------------------------

"""
Resumen Ejecutivo:
Este archivo implementa un CRUD (Crear, Leer, Actualizar, Eliminar) para gestionar productos en memoria utilizando diccionarios y/o listas de diccionarios. Cada operación CRUD está separada en funciones individuales para una mejor organización del código. El programa incluye un menú interactivo que permite al usuario realizar las operaciones de creación, lectura, actualización, eliminación y listado de productos. Además, se implementan validaciones para garantizar la entrada correcta de datos y se gestionan mensajes de error en caso de entradas incorrectas.

Se optó por usar una lista de diccionarios para representar los productos, donde cada diccionario contiene los campos: "id", "name", "price" y "quantity". Esta estructura es flexible y permite un acceso fácil a los elementos, lo que es adecuado para la implementación de un CRUD en memoria.
"""

# --------------------------------------------------
# Problem: In-memory CRUD manager with functions
# Description:
# The program implements a CRUD system for managing items (e.g., products) in memory using functions for each CRUD operation. The main data structure is a list of dictionaries, where each dictionary represents an item with fields like id, name, price, and quantity. The program provides a simple text-based menu for interacting with the user.

# Inputs:
# - option (integer; user's choice in the menu, e.g., 0 for Exit, 1 for Create, etc.).
# - item_id (string or int; unique identifier for the item).
# - name (string; the name of the item).
# - price (float; price of the item).
# - quantity (integer; quantity of the item).

# Outputs:
# - "Item created", "Item updated", "Item deleted", "Item not found", "Items list:", etc.

# Validations:
# - option must be valid (e.g., 0..5).
# - item_id must not be empty or duplicated (for Create).
# - price and quantity must be non-negative numbers.
# - If an operation is attempted with an invalid item_id (e.g., non-existing id), show "Item not found".

# Test cases:
# 1) Normal: create an item, read it, update it, delete it → expected messages and final state.
# 2) Border: attempt to create an item with minimal valid data (e.g., quantity = 0) or an id that's too short/long.
# 3) Error: use invalid menu option, invalid id (empty), or non-numeric price → expected error messages.

# --------------------------------------------------
# Solution Implementation
# Define the main data structure: a list of dictionaries.
# Each dictionary represents an item with "id", "name", "price", and "quantity".

# Global items list
items = []

# Function to create a new item
def create_item(data_structure, item_id, name, price, quantity):
    """Creates an item and adds it to the list if the item_id does not already exist."""
    if any(item['id'] == item_id for item in data_structure):
        print("Error: Item ID already exists.")
        return False
    else:
        new_item = {"id": item_id, "name": name, "price": price, "quantity": quantity}
        data_structure.append(new_item)
        print("Item created")
        return True

# Function to read an item by id
def read_item(data_structure, item_id):
    """Reads an item based on the item_id."""
    for item in data_structure:
        if item['id'] == item_id:
            print(item)
            return item
    print("Error: Item not found")
    return None

# Function to update an item by id
def update_item(data_structure, item_id, new_name, new_price, new_quantity):
    """Updates an existing item by item_id."""
    item = read_item(data_structure, item_id)
    if item:
        item['name'] = new_name
        item['price'] = new_price
        item['quantity'] = new_quantity
        print("Item updated")
        return True
    return False

# Function to delete an item by id
def delete_item(data_structure, item_id):
    """Deletes an item based on item_id."""
    item = read_item(data_structure, item_id)
    if item:
        data_structure.remove(item)
        print("Item deleted")
        return True
    return False

# Function to list all items
def list_items(data_structure):
    """Lists all items in the inventory."""
    if data_structure:
        print("Items list:")
        for item in data_structure:
            print(item)
    else:
        print("No items available.")

# Main menu loop
def main():
    while True:
        print("\n--- Menu ---")
        print("1) Create item")
        print("2) Read item by id")
        print("3) Update item by id")
        print("4) Delete item by id")
        print("5) List all items")
        print("0) Exit")

        try:
            option = int(input("Choose an option: "))
        except ValueError:
            print("Error: invalid input")
            continue
        
        if option == 1:
            item_id = input("Enter item ID: ").strip()
            name = input("Enter item name: ").strip()
            try:
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                if price < 0 or quantity < 0:
                    print("Error: price and quantity must be non-negative.")
                    continue
            except ValueError:
                print("Error: price and quantity must be valid numbers.")
                continue
            create_item(items, item_id, name, price, quantity)

        elif option == 2:
            item_id = input("Enter item ID to read: ").strip()
            read_item(items, item_id)

        elif option == 3:
            item_id = input("Enter item ID to update: ").strip()
            new_name = input("Enter new item name: ").strip()
            try:
                new_price = float(input("Enter new item price: "))
                new_quantity = int(input("Enter new item quantity: "))
                if new_price < 0 or new_quantity < 0:
                    print("Error: price and quantity must be non-negative.")
                    continue
            except ValueError:
                print("Error: price and quantity must be valid numbers.")
                continue
            update_item(items, item_id, new_name, new_price, new_quantity)

        elif option == 4:
            item_id = input("Enter item ID to delete: ").strip()
            delete_item(items, item_id)

        elif option == 5:
            list_items(items)

        elif option == 0:
            print("Exiting the program...")
            break

        else:
            print("Error: invalid input")

# Run the main program
if __name__ == "__main__":
    main()

# --------------------------------------------------
# Conclusiones:
# El uso de funciones para implementar el CRUD permitió organizar el código y separar las responsabilidades de cada operación. 
# Las funciones específicas para crear, leer, actualizar y eliminar elementos mantienen el flujo del programa limpio y modular.
# Utilizar una lista de diccionarios para almacenar los productos resultó ser adecuado debido a la facilidad de acceso y 
# modificación de los datos. La validación de entradas también fue importante para garantizar que solo se procesaran datos válidos.
# El programa puede ser extendido para incluir funcionalidades adicionales, como guardar los datos en un archivo o una base de datos.

# --------------------------------------------------
# References:
# 1) Python documentation – Data structures (dict, list).
# 2) Python documentation – Defining functions.
# 3) Tutorials on CRUD operations with Python.

# --------------------------------------------------
# GitHub Repository: [Metodologias_De_La_Programacion]
