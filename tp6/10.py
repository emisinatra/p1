import numpy as np

# Crear una matriz cuadrada
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# a. Diagonal principal
diag_principal = np.diag(matriz)
print("Diagonal principal: ", diag_principal)

# b. Diagonal inversa
diag_inversa = np.diag(np.fliplr(matriz))
print("Diagonal inversa: ", diag_inversa)
