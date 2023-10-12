# Ejercicio 8
# Crear un arreglo de dos dimensiones con el cuadro de goles
goals = [[0, 2, 1, 3, 2, 1, 0, 2, 1, 2],
         [1, 0, 2, 1, 3, 2, 1, 0, 2, 3],
         [2, 1, 0, 2, 1, 3, 2, 1, 0, 2],
         [0, 2, 1, 0, 2, 1, 3, 2, 1, 0],
         [1, 0, 2, 1, 0, 2, 1, 3, 2, 1],
         [2, 1, 0, 2, 1, 0, 2, 1, 3, 2],
         [3, 2, 1, 0, 2, 1, 0 ,2 ,1 ,3],
         [1 ,3 ,2 ,1 ,0 ,2 ,1 ,0 ,2 ,1],
         [2 ,1 ,3 ,2 ,1 ,0 ,2 ,1 ,0 ,2],
         [1 ,0 ,1 ,3 ,2 ,1 ,0 ,2 ,1 ,0]]

# Crear cuatro listas vacías para almacenar la cantidad de triunfos (wins), empates (draws), derrotas (losses) y puntos (points) de cada equipo
wins = []
draws = []
losses = []
points = []

# Iterar por cada fila del arreglo de goles
for i in range(len(goals)):
    # Inicializar las variables que cuentan los triunfos (w), empates (d), derrotas (l) y puntos (p) de cada equipo en cero
    w = d = l = p = 0
    # Iterar por cada columna del arreglo de goles
    for j in range(len(goals[i])):
        # Si el elemento de la fila i y la columna j es mayor que el elemento de la fila j y la columna i,
        # significa que el equipo i ganó al equipo j
        if goals[i][j] > goals[j][i]:
            # Incrementar los triunfos y los puntos del equipo i en uno y tres respectivamente
            w += 1
            p += 3
        # Si el elemento de la fila i y la columna j es igual al elemento de la fila j y la columna i,
        # significa que el equipo i empató con el equipo j
        elif goals[i][j] == goals[j][i]:
            # Incrementar los empates y los puntos del equipo i en uno y uno respectivamente
            d += 1
            p += 1
        # Si no se cumple ninguna de las condiciones anteriores,
        # significa que el equipo i perdió con el equipo j
        else:
            # Incrementar las derrotas del equipo i en uno
            l += 1
    # Agregar los valores de los triunfos (w), empates (d), derrotas (l) y puntos (p) del equipo i a las listas correspondientes
    wins.append(w)
    draws.append(d)
    losses.append(l)
    points.append(p)

# Crear una lista vacía para almacenar la diferencia entre el total de goles marcados y el total de goles recibidos (goal_difference) de cada equipo
goal_difference = []

# Iterar por cada fila del arreglo de goles
for i in range(len(goals)):
    # Inicializar la variable que cuenta los goles marcados (scored) y los goles recibidos (conceded) de cada equipo en cero
    scored = conceded = 0
    # Iterar por cada columna del arreglo de goles
    for j in range(len(goals[i])):
        # Sumar el elemento de la fila i y la columna j a los goles marcados del equipo i
        scored += goals[i][j]
        # Sumar el elemento de la fila j y la columna i a los goles recibidos del equipo i
        conceded += goals[j][i]
    # Calcular la diferencia entre los goles marcados y los goles recibidos del equipo i y agregarla a la lista correspondiente
    goal_difference.append(scored - conceded)

# Mostrar para cada equipo la cantidad de triunfos (wins), empates (draws), derrotas (losses), la diferencia de goles (goal_difference) y la cantidad de puntos (points)
# Iterar por cada equipo
for i in range(len(goals)):
    # Imprimir los datos del equipo i + 1
    print("El equipo", i + 1, "tiene:")
    print("Triunfos:", wins[i])
    print("Empates:", draws[i])
    print("Derrotas:", losses[i])
    print("Diferencia de goles:", goal_difference[i])
    print("Puntos:", points[i])
