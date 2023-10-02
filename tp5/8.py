#8.	Diseñar una función que calcule el área y el perímetro de una circunferencia.
# Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.
import math # Importar el módulo math para usar funciones matemáticas

def area_perimetro(radio):
    # Calcular el área de la circunferencia como pi por radio al cuadrado
    area = math.pi * radio ** 2
    # Calcular el perímetro de la circunferencia como 2 por pi por radio
    perimetro = 2 * math.pi * radio
    # Devolver el área y el perímetro como una tupla
    return (area, perimetro)

# Pedir el radio de una circunferencia por pantalla y validar que sea positivo
while True:
    radio = float(input("Ingrese el radio de una circunferencia: "))
    if radio > 0:
        break
    else:
        print("El radio debe ser positivo.")
# Calcular el área y el perímetro usando la función definida
area, perimetro = area_perimetro(radio)
# Mostrar el área y el perímetro con dos decimales
print(f"El área de la circunferencia es: {area:.2f}")
print(f"El perímetro de la circunferencia es: {perimetro:.2f}")