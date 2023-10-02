#10.Escribir una función que aplique un descuento a un precio. Esta función tiene que recibir un diccionario
# con los precios y porcentajes del carrito de compra, aplicar los descuentos a los productos del carrito
# y devolver el precio final de la compra.
def descuento(carrito):
    # Inicializar el precio final en cero
    precio_final = 0
    # Recorrer cada producto y su porcentaje en el diccionario del carrito
    for producto, porcentaje in carrito.items():
        # Calcular el precio con descuento como el precio original menos el porcentaje
        precio_con_descuento = producto - producto * porcentaje / 100
        # Sumar el precio con descuento al precio final
        precio_final += precio_con_descuento
    # Devolver el precio final
    return precio_final

# Crear un diccionario con los precios y porcentajes del carrito de compra
carrito = {100: 10, 50: 20, 30: 5}
# Calcular el precio final usando la función definida
precio_final = descuento(carrito)
# Mostrar el precio final con dos decimales
print(f"El precio final de la compra es: {precio_final:.2f}")