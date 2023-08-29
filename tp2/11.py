#11-	La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
#•	Ingredientes vegetarianos: Pimiento y tofu.
#•	Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
print("Las opciones son:")
print("V) Pizza vegetariana")
print("N) Pizza no vegetariana")
opcion = input("Ingrese la opción elegida (V o N): ")
if opcion == "V":
    print("Los ingredientes disponibles son:")
    print("P) Pimiento")
    print("T) Tofu")
    ingrediente = input("Ingrese el ingrediente elegido (P o T): ")
else:
    print("Los ingredientes disponibles son:")
    print("P) Peperoni")
    print("J) Jamón")
    print("S) Salmón")
    ingrediente = input("Ingrese el ingrediente elegido (P, J o S): ")
if ingrediente == "P":
    if opcion == "V":
        ingrediente = "Pimiento"
    else:
        ingrediente = "Peperoni"
elif ingrediente == "T":
    ingrediente = "Tofu"
elif ingrediente == "J":
    ingrediente = "Jamón"
else:
    ingrediente = "Salmón"
if opcion == "V":
    print("La pizza elegida es vegetariana y lleva los siguientes ingredientes: mozzarella, tomate y " + ingrediente)
else:
    print("La pizza elegida no es vegetariana y lleva los siguientes ingredientes: mozzarella, tomate y " + ingrediente)
