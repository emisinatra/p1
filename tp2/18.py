#18-	Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
#La jornada de trabajo mínima es de 48 horas. Calcular, dadas las horas trabajadas, si trabajó horas extras y mostrar esta cantidad.
#Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las horas laborales comunes.
horas = int(input("Ingrese el total de horas trabajadas en el mes: "))
salario = float(input("Ingrese el salario por hora: "))
if horas > 48:
    extras = horas - 48
    print("Usted trabajó", extras, "horas extras")
else:
    extras = 0
    print("Usted no trabajó horas extras")
salario_total = (horas - extras) * salario + extras * salario * 1.1
print("Su salario total es", salario_total)
