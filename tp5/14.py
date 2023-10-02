#14.	Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida.
def es_primo(numero):
    # Verificar si el número es menor que dos, en cuyo caso no es primo
    if numero < 2:
        return False
    # Verificar si el número es divisible por algún número entre dos y su raíz cuadrada, en cuyo caso no es primo
    for divisor in range(2, int(math.sqrt(numero)) + 1):
        if numero % divisor == 0:
            return False
    # Si no se cumple ninguna de las condiciones anteriores, el número es primo
    return True

# Pedir un número entero por pantalla y verificar si es primo o no usando la función definida
numero = int(input("Ingrese un número entero: "))
if es_primo(numero):
    print(f"{numero} es primo.")
else:
    print(f"{numero} no es primo.")