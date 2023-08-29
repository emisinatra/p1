#15.	Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
# Escribir un algoritmo que determine la hora de llegada a la ciudad B.
HH = int(input("Ingrese la hora de partida: "))
MM = int(input("Ingrese los minutos de partida: "))
SS = int(input("Ingrese los segundos de partida: "))
T = int(input("Ingrese el tiempo de viaje en segundos: "))
segundos = HH * 3600 + MM * 60 + SS
segundos += T
HH = segundos // 3600
MM = (segundos % 3600) // 60
SS = (segundos % 3600) % 60
print("La hora de llegada a la ciudad B es", HH, "horas,", MM, "minutos y", SS, "segundos")
