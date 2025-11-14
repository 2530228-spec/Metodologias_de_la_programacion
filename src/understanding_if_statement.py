cars = ["audi", "bmw", "chevrolet", "corvette", "tesla"]

for car in cars:
    if car == "bmw" or car == "tesla" or car == "audi": 
        print(car.upper())
    else:
        print(car)

print("----Condicionales Básicos----", "\n")
# Condicionales: El condicional es el corazón de un if.
# Condicional True 

car = "bmw"
print(car == "bmw") # Salida: True

car_2 = "Audi"
print(car_2 == "audi") # Salida: False

car_2 = "Audi"
print(car_2.lower() == "audi") # Salida: True

#Codicional != para determinar desigualdad
requested_topping = "mushrooms"
if requested_topping != "anchovies": # Salida: True
    print("Hold the anchovies!")

# Condicionales numéricos
age = 18 # -> int
print(age == 18) # Salida: True

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
print(age < 21) # Salida: True
print(age <= 21) # Salida: True
print(age > 21) # Salida: False
print(age >= 21) # Salida: False

# Multiple condiciones
age_0 = 22
age_1 = 18

print(age_0 >= 21 and age_1 >= 21) # Salida: False
print(age_0 >= 21 and age_1 >= 18) # Salida: True
print(age_0 >= 21 or age_1 >= 21) # Salida: True
print(age_0 >= 23 or age_1 >= 21) # Salida: False

# Verificando si un valor está en una lista
requested_toppings = ["mushrooms", "onions", "pineapple"]
print("mushrooms" in requested_toppings) # Salida: True
print("pepperoni" in requested_toppings) # Salida: False

# Verificando si un valor no está en una lista
banned_users = ["gabriel", "max", "andrik", "quevedo", "chris"]
user = "pedro"
print(user not in banned_users) # Salida: True

# variables booleanas
game_active = True
can_edit = False

"""
    if statements

    if ccondition:
        do something

    if condition:
        do something (true)
    else:
        do something (false)
"""

# Preguntar la edad de una persona y determinar si es mayor de edad
print("----Ejemplo----", "\n")

age = int(input("¿Cual es tu edad?: "))
age = (f"tu esdad es: {age}")

if age >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

