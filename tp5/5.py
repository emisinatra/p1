#5.	Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima.
# Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día
# y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.

def temperatura_media(maxima, minima):
    # Calcular la temperatura media como el promedio de la máxima y la mínima
    media = (maxima + minima) / 2
    return media

# Pedir el número de días que se van a introducir
n = int(input("Ingrese el número de días: "))
# Crear un bucle para pedir la temperatura máxima y mínima de cada día y mostrar la media
for i in range(n):
    # Pedir la temperatura máxima y mínima del día i+1
    maxima = float(input(f"Ingrese la temperatura máxima del día {i+1}: "))
    minima = float(input(f"Ingrese la temperatura mínima del día {i+1}: "))
    # Calcular la temperatura media usando la función definida
    media = temperatura_media(maxima, minima)
    # Mostrar la temperatura media del día i+1
    print(f"La temperatura media del día {i+1} es: {media}")