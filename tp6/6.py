# Ejercicio 6
# Crear dos listas vacías para almacenar los nombres de los alumnos de nivel primario y secundario
primary_names = []
secondary_names = []

# Pedir al usuario que ingrese los nombres de los alumnos de nivel primario hasta que ingrese 'x'
while True:
    # Solicitar un nombre al usuario
    name = input("Ingrese un nombre de alumno de nivel primario ('x' para terminar): ")
    # Si el nombre es 'x', salir del bucle
    if name == 'x':
        break
    # Si no, agregar el nombre a la lista de nivel primario
    else:
        primary_names.append(name)

# Pedir al usuario que ingrese los nombres de los alumnos de nivel secundario hasta que ingrese 'x'
while True:
    # Solicitar un nombre al usuario
    name = input("Ingrese un nombre de alumno de nivel secundario ('x' para terminar): ")
    # Si el nombre es 'x', salir del bucle
    if name == 'x':
        break
    # Si no, agregar el nombre a la lista de nivel secundario
    else:
        secondary_names.append(name)

# Informar los nombres de todos los alumnos de nivel primario y de los de nivel secundario, sin repeticiones
# Crear dos conjuntos con los elementos únicos de cada lista
primary_set = set(primary_names)
secondary_set = set(secondary_names)
# Imprimir los conjuntos, iterando por ellos
print("Los nombres de todos los alumnos de nivel primario, sin repeticiones, son:")
for name in primary_set:
    print(name)
print("Los nombres de todos los alumnos de nivel secundario, sin repeticiones, son:")
for name in secondary_set:
    print(name)

# Informar qué nombres se repiten entre los alumnos de nivel primario y secundario
# Crear un conjunto con la intersección de los dos conjuntos anteriores
repeated_set = primary_set & secondary_set
# Imprimir el conjunto, iterando por él
print("Los nombres que se repiten entre los alumnos de nivel primario y secundario son:")
for name in repeated_set:
    print(name)

# Informar qué nombres de nivel primario no se repiten en los de nivel secundario
# Crear un conjunto con la diferencia entre el conjunto de nivel primario y el conjunto de nivel secundario
not_repeated_set = primary_set - secondary_set
# Imprimir el conjunto, iterando por él
print("Los nombres de nivel primario que no se repiten en los de nivel secundario son:")
for name in not_repeated_set:
    print(name)


