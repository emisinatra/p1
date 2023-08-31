#19-	Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El programa deberá comprobar que las cantidades ingresadas sean positivas.
objetivo = float(input("Ingrese la cantidad de dinero que quiere ahorrar: "))
ahorrado = 0
while ahorrado < objetivo:
    cantidad = float(input("Ingrese la cantidad que va a ahorrar: "))
    if cantidad > 0:
        ahorrado += cantidad
        print(f"Ha ahorrado {ahorrado:.2f}")
    else:
        print("Error: la cantidad debe ser positiva")
print(f"¡Felicidades! Ha alcanzado su objetivo de {objetivo:.2f}")
