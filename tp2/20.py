#20-	Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio de cuatro (4) notas,
# es mayor o igual a 6; caso contrario saldrá desaprobado.
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
nota4 = float(input("Ingrese la cuarta nota: "))
promedio = (nota1 + nota2 + nota3 + nota4) / 4
if promedio >= 6:
    print("El alumno aprueba con un promedio de", promedio)
else:
    print("El alumno reprueba con un promedio de", promedio)
