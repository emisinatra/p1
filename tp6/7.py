# Ejercicio 7
# Crear un diccionario vacío para almacenar la cantidad total de ocurrencias de cada carácter
char_count = {}

# Crear una variable para contar la cantidad de strings ingresados por el usuario
string_count = 0

# Pedir al usuario que ingrese strings hasta que se hayan procesado 50 strings
while string_count < 50:
    # Solicitar un string al usuario
    string = input("Ingrese un string (se han procesado " + str(string_count) + " strings): ")
    # Iterar por cada carácter del string
    for char in string:
        # Si el carácter está en el diccionario, incrementar su valor en uno
        if char in char_count:
            char_count[char] += 1
        # Si no, agregar el carácter al diccionario con el valor uno
        else:
            char_count[char] = 1
    # Incrementar la variable que cuenta la cantidad de strings en uno
    string_count += 1

# Imprimir la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados, iterando por el diccionario
print("La cantidad total de ocurrencias de cada carácter, en todos los strings ingresados, es:")
for char, count in char_count.items():
    print("'" + char + "':" + str(count))