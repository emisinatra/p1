#8.	Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas,
# el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes
# y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
sueldo_base = float(input("Ingrese el sueldo base del vendedor: "))
venta1 = float(input("Ingrese la primera venta: "))
venta2 = float(input("Ingrese la segunda venta: "))
venta3 = float(input("Ingrese la tercera venta: "))
total_ventas = venta1 + venta2 + venta3
comision = total_ventas * 0.1
sueldo_total = sueldo_base + comision
print("El vendedor obtendrá", comision, "por concepto de comisiones")
print("El vendedor recibirá", sueldo_total, "en el mes")