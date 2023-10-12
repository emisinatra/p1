# Crear el diccionario
frutas = {'manzana': 2.0, 'banana': 3.0, 'naranja': 1.5}

# Preguntar al usuario
fruta = input("Introduce una fruta: ")
kilos = float(input("Introduce el número de kilos: "))

# Mostrar el precio o un mensaje de aviso
if fruta in frutas:
    print(f"El precio de {kilos} kilos de {fruta} es {frutas[fruta]*kilos}")
else:
    print("La fruta no está en el diccionario")

