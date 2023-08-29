#19-	Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más,
#existe un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; de lo contrario no hay descuento.
cantidad = int(input("Ingrese la cantidad de lápices: "))
if cantidad >= 1000:
    pago = cantidad * 60 * 0.93
else:
    pago = cantidad * 60
print("El pago por los lápices es", pago)
