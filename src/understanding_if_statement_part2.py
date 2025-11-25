#
age = 0
try:
    age = int(input("Escribe tu edad "))
except:
   age = -1
   print("Error, ingresaste una letra")

if age >= 100:
      print ("Tienes mas de un siglo")
elif age >= 18 and age < 100:
        print("Eres mayor de edad")
elif age >= 0 and age < 18:
        print("Eres menor de edad")
else:
      print("Tuviste un error")

#Utilizando varias listas 
guisos_disponibles = ["salsa verde", "deshebrada", "mole"]
guisos_a_ordenar = ["deshebrada", "caldo de iguana"]

print("¿que guisos desea ordenar?")
for guiso in guisos_a_ordenar:
      print(f"deseo {guiso}")
      if guiso in guisos_disponibles:
            print(f"Si tenemos {guiso}")
      else:
            print("No tenomos guiso de ese")
print("Realizando pedido....")