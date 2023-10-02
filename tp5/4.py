#4.	Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro.
# Crea una función que reciba los dos números, y devuelve si el primero es múltiplo del segundo.
def es_multiplo(a, b):
    # Verificar si a es múltiplo de b, es decir, si el resto de la división es cero
    if a % b == 0:
        return True
    else:
        return False

# Pedir dos números enteros por pantalla y verificar si alguno es múltiplo del otro
a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese otro número entero: "))
if es_multiplo(a, b):
    print(f"{a} es múltiplo de {b}.")
elif es_multiplo(b, a):
    print(f"{b} es múltiplo de {a}.")
else:
    print(f"Ninguno de los dos números es múltiplo del otro.")