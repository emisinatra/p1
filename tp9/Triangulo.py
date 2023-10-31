class Triangulo:
    def __init__(self, lado1=0, lado2=0, lado3=0):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    # Método para imprimir el valor del lado mayor
    def imprimir_lado_mayor(self):
        return max(self.lado1, self.lado2, self.lado3)

    # Método para determinar el tipo de triángulo
    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return 'Equilátero'
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return 'Isósceles'
        else:
            return 'Escaleno'
