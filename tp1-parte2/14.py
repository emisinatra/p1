#14.	Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables
# y muestre cuanto valen al final las dos variables.
A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))
aux = A
A = B
B = aux
print("Al final, A vale", A, "y B vale", B)

