"""
  El while es un ciclo controlado/comando 
  por condiciones.

  La estructura basica de while es:
    while condicion:
        actions
"""

# while infinito
while True:
    try:
      number = int(input("Ingresa un número : "))

      if number >= 25 and number <= 50:
          print("El número está en el rango")
          break
      else:
          print("El número está fuera del rango")        
    except ValueError:
         print("Por favor ingresa un número válido")