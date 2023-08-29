#18.	Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante.
# A ese valor, sumarle un 6.2% en concepto de servicio y un 10% de propina.
# Imprimir en pantalla el monto final a pagar.
cena = float(input("Ingrese el costo de la cena: "))
final = cena + (cena * 0.062) + (cena * 0.1)
monto_final = cena + (cena * 0.062) + (cena * 0.1)
print("El monto final a pagar es", monto_final)
