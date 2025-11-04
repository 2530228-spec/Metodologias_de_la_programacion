# Numbers 

"""
    Enteros

        Los enteres los podemos sumar , restar,
        multiplicar y dividir.
        Les podemos aplicar potencias(**2,**3,**4, etc)
        modulo(%)
"""
number_1 = 35
number_2 = 15
suma = number_1 + number_2
resta = number_1 - number_2
multiplicacion = number_1 * number_2
division = number_1 / number_2
potencia = number_1 ** 2
modulo = number_1 % number_2

print("Suma: ", suma, type(suma))
print("Resta: ", resta, type(resta))
print("Multiplicacion: ", multiplicacion, type(multiplicacion))
print("Division: ", division, type(division))
print("Potencia: ", potencia, type(potencia))
print("Modulo: ", modulo, type(modulo))

"""
    Jerarquia de operaciones

    2+3*4 -> 14
    (2+3)*4 -> 20
"""

"""
    Floats
        python llama floats a los numeros con decimales.
        Los floats los podemos sumar , restar,
        multiplicar y dividir.
        Les podemos aplicar potencias(**2,**3,**4, etc)
"""
print(0.1 + 0.2)
print(0.2 - 0.2)
print(0.1 * 2)
print(2 * 0.2)

#Imprimir la edad de alguien 
age = 18
message = "Medellin tienes " + str(age) + " años."
print(message)

"""
   TypeError: Esto significa que Python no puede
   reconocer el tipo de informacion que le estamos dando.
"""
"""
   Zen de Python (investigar)
"""
