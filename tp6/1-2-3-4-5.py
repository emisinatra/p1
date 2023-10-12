# Crear una lista vacía para almacenar los números
numbers = []

# Pedir al usuario que ingrese números hasta que ingrese 0
while True:
    # Solicitar un número al usuario
    num = int(input("Ingrese un número (0 para terminar): "))
    # Si el número es 0, salir del bucle
    if num == 0:
        break
    # Si no, agregar el número a la lista
    else:
        numbers.append(num)

# Mostrar la lista de números
print("La lista de números es:", numbers)

# Pedir al usuario que ingrese otro número para eliminar su primera ocurrencia de la lista
num_to_delete = int(input("Ingrese un número para eliminar su primera ocurrencia de la lista: "))
# Si el número está en la lista, eliminarlo y mostrar un mensaje
if num_to_delete in numbers:
    numbers.remove(num_to_delete)
    print("Se eliminó el número", num_to_delete, "de la lista.")
# Si no, mostrar un mensaje de que no es posible eliminar
else:
    print("No se puede eliminar el número", num_to_delete, "porque no está en la lista.")

# Imprimir la sumatoria de todos los números de la lista
print("La sumatoria de todos los números de la lista es:", sum(numbers))

# Pedir al usuario otro número para crear una nueva lista con los elementos menores que ese número
num_to_compare = int(input("Ingrese otro número para crear una nueva lista con los elementos menores que ese número: "))
# Crear una nueva lista vacía para almacenar los elementos menores
new_list = []
# Iterar por la lista original y agregar los elementos menores al nuevo número a la nueva lista
for num in numbers:
    if num < num_to_compare:
        new_list.append(num)
# Imprimir la nueva lista, iterando por ella
print("La nueva lista con los elementos menores que", num_to_compare, "es:")
for num in new_list:
    print(num)

# Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella
# Crear una nueva lista vacía para almacenar las tuplas
tuple_list = []
# Crear un conjunto con los elementos únicos de la lista original
unique_numbers = set(numbers)
# Iterar por el conjunto y crear una tupla con el número y su frecuencia en la lista original, y agregarla a la nueva lista
for num in unique_numbers:
    frequency = numbers.count(num)
    tuple_list.append((num, frequency))
# Imprimir la nueva lista, iterando por ella
print("La nueva lista con las tuplas es:")
for tup in tuple_list:
    print(tup)
