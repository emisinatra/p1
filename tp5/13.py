#13.	Escribir una función que calcule el módulo de un vector.
import math # Importar el módulo math para usar funciones matemáticas

def modulo(vector):
    # Inicializar la suma de los cuadrados en cero
    suma_cuadrados = 0
    # Recorrer cada componente del vector
    for componente in vector:
        # Elevar al cuadrado la componente y sumarla a la suma de los cuadrados
        suma_cuadrados += componente ** 2
    # Calcular la raíz cuadrada de la suma de los cuadrados como el módulo del vector
    modulo = math.sqrt(suma_cuadrados)
    # Devolver el módulo del vector
    return modulo

# Crear un vector de ejemplo con tres componentes
vector = [3, 4, 5]
# Calcular el módulo del vector usando la función definida
modulo = modulo(vector)
# Mostrar el módulo del vector con dos decimales
print(f"El módulo del vector es: {modulo:.2f}")
