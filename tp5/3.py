#3.	Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club.
# Para eso ingresará nombre completo y número de DNI de cada socio,
# indicando que finalizará el procesamiento mediante el ingreso de un nombre vacio.
#Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, en cuyo caso será: nombre1, nombre2,
# apellido. Si un socio tuviera más de un apellido, el usuario solo ingresará uno.
#Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.
#Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre,
# la cantidad de letras del apellido y los 3 primeros dígitos de su DNI. Ejemplo:
#Nombre: María Ines Rosales
#DNI: 25469648
#ID -> Maria7254

# Crear una lista vacía para guardar los socios
socios = []
# Crear un bucle infinito para pedir los datos de cada socio
while True:
    # Pedir el nombre completo del socio
    nombre = input("Ingrese el nombre completo del socio (o vacío para terminar): ")
    # Si el nombre está vacío, salir del bucle
    if nombre == "":
        break
    # Pedir el número de DNI del socio y validar que sea correcto
    while True:
        dni = input("Ingrese el número de DNI del socio: ")
        if validar_dni(dni):
            break
        else:
            print("El número de DNI es inválido. Debe tener entre 7 y 8 dígitos.")
    # Agregar el socio a la lista como una tupla (nombre, dni)
    socios.append((nombre, dni))
# Recorrer la lista de socios y generar el identificador para cada uno
for nombre, dni in socios:
    # Separar el nombre por los espacios y obtener el primer nombre y el apellido
    partes = nombre.split()
    primer_nombre = partes[0]
    apellido = partes[-1]
    # Obtener la cantidad de letras del apellido y los 3 primeros dígitos del dni
    letras_apellido = len(apellido)
    digitos_dni = dni[:3]
    # Formar el identificador con el formato pedido
    id_socio = primer_nombre + str(letras_apellido) + digitos_dni
    # Imprimir el identificador del socio
    print(f"ID -> {id_socio}")



