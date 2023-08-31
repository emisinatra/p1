#23-	Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.
##24-	Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
total = 0
while True:
    monto = float(input("Ingrese el monto de la compra (0 para terminar): "))
    if monto == 0:
        break
    elif monto < 0:
        print("Error: el monto debe ser positivo")
    else:
        total += monto
if total > 1000:
    descuento = total * 0.1
    total -= descuento
    print(f"Se le aplica un descuento de {descuento:.2f}")
print(f"El total a pagar es {total:.2f}")
