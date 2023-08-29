#1.	Calcular el perímetro y área de un rectángulo dada su base y su altura.
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))
perimetro = 2 * (base + altura)
area = base * altura
print("El perímetro del rectángulo es", perimetro)
print("El área del rectángulo es", area)