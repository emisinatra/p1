# defino la funcion is_mutant que recibe como parametro "la secuencia de adn"
def is_mutant(adn):
    # inicializo un contador
    sequence_count = 0
    # aca me fijo cada celda de la matriz
    for i in range(len(adn)):
        for j in range(len(adn[0])):
            # verifico horizontalmente
            if j + 3 < len(adn[0]) and adn[i][j] == adn[i][j + 1] == adn[i][j + 2] == adn[i][j + 3]:
                sequence_count += 1
                print(f"Secuencia encontrada en la fila {i+1}, desde la columna {j+1} hasta la columna {j+4}")
            # aca verticalmente
            if i + 3 < len(adn) and adn[i][j] == adn[i + 1][j] == adn[i + 2][j] == adn[i + 3][j]:
                sequence_count += 1
                print(f"Secuencia encontrada en la columna {j+1}, desde la fila {i+1} hasta la fila {i+4}")
            # y aca en diagonal
            if i + 3 < len(adn) and j + 3 < len(adn[0]) and adn[i][j] == adn[i + 1][j + 1] == adn[i + 2][j + 2] == adn[i + 3][j + 3]:
                sequence_count += 1
                print(f"Secuencia encontrada en diagonal desde la fila {i+1}, columna {j+1} hasta la fila {i+4}, columna {j+4}")
            # aca si encuentra mas de una secuencia devuelve true
            if sequence_count > 1:
                return True
    # y si no devuelve false
    return False

# aca pido por pantalla que se ingresen las filas de la matriz
dna = []
print("Ingrese las filas de la matriz de ADN (6x6):")
for _ in range(6):
    while True:
        row = input()
        # aca me fijo q la celda solo tenga 6 caracteres y solo las letras 'A', 'T', 'C' y 'G'
        if len(row) == 6 and all(char in 'ATCG' for char in row):
            dna.append(row)
            break
        else:
            print("Entrada inválida. Por favor, ingrese una fila de ADN válida.")

# y aca uso la funcion y imprimo el resultado
if is_mutant(dna):
    print("La secuencia de ADN es mutante.")
else:
    print("La secuencia de ADN no es mutante.")
