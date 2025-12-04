"""
Problema 1.-
    Implementa un sistema sensillo de intento 
    de contraseña correcta (por ejemplo "admin123"),
    el usuario tendra un maximo de MAX_ATEMPS intentos 
    para introducirla. Si acierta dentro del limite 
    mostrara un mensaje de exito. Si agota los intentos 
    mostrara un mensaje de bloqueo.
"""
#Contraseña correcta
CORRECT_PIN = "admin123"
MAX_ATTEMPTS = 3
attempts = 0

while attempt < MAX_ATTEMPTS:

    user_imput = input("Ingresa tu PIN")

    if user_imput == CORRECT_PIN:
        print("Acceso cocedido")
        break
    else:
        attempt += 1
        reamining_attemps = MAX_ATTEMPTS - attempt
        if reamining_attemps > 0:
            print("Ingresa un pin valido")
            print(f"Te quedan {reamining_attemps} intentos")
        else:
            print("Maximo de intentos alcansado, cuenta bloqueada")

"""
Problema 2.-
    Define una funcion factoreal (n) que regrese n! (n factorial)
    Puedes implementarla de forma interativa (con for) o recursiva,
    pero debes documentar tu elección en comentarios.
    El codigo principal debe:
     -Leer/definir n 
     -Validar n
     -Llamar a factorial(n)
     -Mostrar el resultado

"""





"""
Pregunta de rescate No. 1 
        Implementa un programa en Python que calcule y
        muestre la serie de Fibonacci.
"""
# Serie de Fibonacci
n = int(input("Cuántos términos quieres: "))

a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c

"""
Pregunta de rescate No. 2
        Implementa CRUD (Created,Read,Upsate,Delete) sobre 
        una estructura de datos de memoria (diccionario o 
        lista de diccionarios.) utilizando funciones en python.
        Ademas, que practique la separación de responsabilidades
        (Cada operacion en una funcion), el diseño de menus basicos,
        lavalidacion de entradas y la documentación de su solucion 
        con descripcion, casos de prueva y conclución.
"""





"""
Pregunta de rescate No.3
        El sen de pyton: 
        Se refiere a las normas no escritas por la 
        comunidad de python para programar en este 
        lengaje, entre ellas se refiere a :
        . No mas de 90 caracteres por linea de codigo
        . Usar el ingles ya que es un idioma mas aseptado
        mundialmente
        . Utilizar nombres legibles y entendibles 
        en los valores definidos 
        . No escribir una variables con mayusculas 
        . No escribir una constante con minusculas 
"""