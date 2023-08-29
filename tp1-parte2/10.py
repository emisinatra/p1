#10.	Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
#•	    55% del promedio de sus tres calificaciones parciales.
#•	    30% de la calificación del examen final.
#•	    15% de la calificación de un trabajo final.


parcial1 = float(input("Ingrese la primera calificación parcial: "))
parcial2 = float(input("Ingrese la segunda calificación parcial: "))
parcial3 = float(input("Ingrese la tercera calificación parcial: "))
promedio_parciales = (parcial1 + parcial2 + parcial3) / 3
examen_final = float(input("Ingrese la calificación del examen final: "))
trabajo_final = float(input("Ingrese la calificación del trabajo final: "))
calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.3) + (trabajo_final * 0.15)
print("La calificación final en la materia de Algoritmos es", calificacion_final)
