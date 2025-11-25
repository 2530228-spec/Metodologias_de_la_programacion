#Empty dictionary
homer_0 = {
    "color": "yellow", 
    "bag": "maggie-bag", 
    "mom": False}
print(homer_0)
print(type(homer_0))

marge = {
    "color": "yellow", 
    "bag": "homer-donut", 
    "mom" : True}

gun_0 = {
    "scar": "yellow-orange", 
    "headshot": 1.5}

print(homer_0)
homer_0["x-position"] = 15
homer_0["y-position"] = 25
homer_0["z-position"] = 10
print(homer_0)

marge["x-position"] = 15
marge["y-position"] = 25
marge["z-position"] = 10


print("\n")
covenant_grunt = {
    "color": "orange",
    "weapon": "plasma-gun",
    "armament": "plasma-grenade",
    "health": 2,
}

covenant_elite = {
    "color": "blue",
    "weapon": "energy-sword",
    "armament": "plasma-grenade",
    "health": 7,
}

covenant_jackal ={
    "color": "grey",
    "weapon": "plasma-rifle",
    "armament": "plasma-grenade",
    "health": 5,
}

#lista de diccionarios
covenants = [
    covenant_grunt, 
    covenant_elite, 
    covenant_jackal
]

for covenant in covenants:
    print("\n", covenant)
    for key, valuea in covenant.items():
        print("\t" + key + ": " + str(valuea))

print("\n")
## Listas de diccionarios
students = {
    "santiago":["reprobado","prepa1","rebelde"],
    "Jorge":["aprobado", "cbits 271"],
}

print("\n")
sensors = {
    "temperature": {
        "value": 22.5,
        "unit": "Celsius"
    },
    "humidity": {
        "value": 60,
        "unit": "%"
    },
}

print("Temperature:", sensors["temperature"]["value"], sensors["temperature"]["unit"])
print("Humidity:", sensors["humidity"]["value"], sensors["humidity"]["unit"])