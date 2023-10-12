# Ejercicio 9
# Importar el módulo random para generar números aleatorios
import random

# Crear una lista con las letras del abecedario
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
           "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
           "U", "V", "W", "X", "Y", "Z"]

# Crear una matriz de 4x4 con cartas aleatorias, cada una con una letra del abecedario
# Cada letra debe aparecer dos veces en la matriz
cards = []
# Crear una lista vacía para almacenar las letras elegidas
chosen_letters = []
# Iterar por cada fila de la matriz
for i in range(4):
    # Crear una lista vacía para almacenar las cartas de la fila i
    row = []
    # Iterar por cada columna de la matriz
    for j in range(4):
        # Elegir una letra aleatoria de la lista de letras
        letter = random.choice(letters)
        # Si la letra ya está en la lista de letras elegidas, significa que ya apareció una vez
        if letter in chosen_letters:
            # Eliminar la letra de la lista de letras para que no aparezca más de dos veces
            letters.remove(letter)
            # Eliminar la letra de la lista de letras elegidas para que no se repita en la misma fila o columna
            chosen_letters.remove(letter)
        # Si no, agregar la letra a la lista de letras elegidas
        else:
            chosen_letters.append(letter)
        # Agregar la carta con la letra a la lista de la fila i
        row.append(letter)
    # Agregar la lista de la fila i a la matriz de cartas
    cards.append(row)

# Crear una matriz de 4x4 con el estado de cada carta, si está boca arriba (True) o boca abajo (False)
# Inicialmente todas las cartas están boca abajo
status = []
# Iterar por cada fila de la matriz
for i in range(4):
    # Crear una lista vacía para almacenar el estado de las cartas de la fila i
    row = []
    # Iterar por cada columna de la matriz
    for j in range(4):
        # Agregar el valor False a la lista de la fila i
        row.append(False)
    # Agregar la lista de la fila i a la matriz de estados
    status.append(row)

# Crear una variable para contar los pares encontrados
pairs = 0

# Crear un bucle para simular el juego hasta que se encuentren todos los pares
while pairs < 8:
    # Mostrar el tablero con las cartas boca arriba o boca abajo según su estado
    print("El tablero es:")
    # Iterar por cada fila de la matriz
    for i in range(4):
        # Crear una cadena vacía para almacenar las cartas de la fila i
        row = ""
        # Iterar por cada columna de la matriz
        for j in range(4):
            # Si el estado de la carta es True, mostrar su letra
            if status[i][j]:
                row += cards[i][j] + " "
            # Si no, mostrar un asterisco
            else:
                row += "* "
        # Imprimir la cadena de la fila i
        print(row)

    # Pedir al usuario que ingrese las coordenadas de dos cartas para voltearlas
    print("Ingrese las coordenadas de dos cartas para voltearlas, separadas por espacios.")
    print("Las coordenadas deben ser números entre 1 y 4, correspondientes a las filas y columnas del tablero.")
    print("Por ejemplo, 1 2 3 4 significa voltear las cartas en las posiciones (1,2) y (3,4).")
    # Crear un bucle para validar el ingreso del usuario
    while True:
        # Solicitar al usuario que ingrese las coordenadas
        coordinates = input("Ingrese las coordenadas: ")
        # Intentar convertir las coordenadas en una lista de cuatro enteros
        try:
            coordinates = list(map(int, coordinates.split()))
            # Verificar que la lista tenga cuatro elementos y que todos estén entre 1 y 4
            if len(coordinates) == 4 and all(1 <= x <= 4 for x in coordinates):
                # Salir del bucle de validación
                break
            # Si no, mostrar un mensaje de error y volver a pedir las coordenadas
            else:
                print("Las coordenadas deben ser cuatro números entre 1 y 4, separados por espacios.")
        # Si ocurre una excepción al convertir las coordenadas, mostrar un mensaje de error y volver a pedir las coordenadas
        except:
            print("Las coordenadas deben ser cuatro números entre 1 y 4, separados por espacios.")

    # Obtener las filas y columnas de las dos cartas elegidas por el usuario, restando uno para ajustar a los índices de las matrices
    row1 = coordinates[0] - 1
    col1 = coordinates[1] - 1
    row2 = coordinates[2] - 1
    col2 = coordinates[3] - 1

    # Cambiar el estado de las dos cartas elegidas a True para voltearlas
    status[row1][col1] = True
    status[row2][col2] = True

    # Mostrar el tablero con las cartas volteadas
    print("El tablero es:")
    # Iterar por cada fila de la matriz
    for i in range(4):
        # Crear una cadena vacía para almacenar las cartas de la fila i
        row = ""
        # Iterar por cada columna de la matriz
        for j in range(4):
            # Si el estado de la carta es True, mostrar su letra
            if status[i][j]:
                row += cards[i][j] + " "
            # Si no, mostrar un asterisco
            else:
                row += "* "
        # Imprimir la cadena de la fila i
        print(row)

    # Verificar si las dos cartas elegidas son iguales
    if cards[row1][col1] == cards[row2][col2]:
        # Mostrar un mensaje de que se encontró un par
        print("¡Encontraste un par!")
        # Incrementar la variable que cuenta los pares en uno
        pairs += 1
    # Si no son iguales
    else:
        # Mostrar un mensaje de que no se encontró un par
        print("No encontraste un par.")
        # Cambiar el estado de las dos cartas elegidas a False para volverlas a boca abajo
        status[row1][col1] = False
        status[row2][col2] = False

# Mostrar un mensaje de que se terminó el juego
print("¡Terminaste el juego!")