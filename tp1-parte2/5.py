'''
a) A = input(nombre, “¿Cuál es tu canción favorita?”)

El problema es que la función input solo acepta un argumento, que es el mensaje que se muestra al usuario.
 No se puede pasar el nombre como un argumento adicional.
La solución es concatenar el nombre con el mensaje usando el operador +, por ejemplo:
'''
nombre = "Juan"
A = input(nombre + ", ¿Cuál es tu canción favorita?")
'''
b) precio = input(“Precio: “) total = precio + (precio * 0.1)

El problema es que la función input devuelve una cadena de texto, no un número. 
Al intentar hacer operaciones aritméticas con una cadena, se produce un error de tipo.
La solución es convertir la cadena a un número usando la función float o int, 
dependiendo del tipo de dato que se quiera. Por ejemplo:
'''
precio = float(input("Precio: "))
total = precio + (precio * 0.1)
'''
c) edad = int(input(“Edad: “)) print(tu edad es, edad)

El problema es que la función print necesita paréntesis para encerrar los argumentos que se quieren mostrar. 
Además, si se quiere mostrar una cadena de texto junto con una variable, se debe usar el operador + o una coma para separarlos.
La solución es agregar los paréntesis y usar el operador + o una coma para mostrar la cadena y la variable. Por ejemplo:
'''
edad = int(input("Edad: "))
print("Tu edad es", edad) # Usando una coma
print("Tu edad es " + str(edad)) # Usando el operador +
'''
d) edad = int(input(“Edad: “)) print(“Veamos si tu edad es 18…”, edad=18)

El problema es que al usar el signo igual (=) dentro de la función print, se está asignando un valor a la variable edad,
 no comparándola con otro valor. Para comparar dos valores se debe usar el operador de igualdad (==),
  que devuelve True o False según si son iguales o no.
La solución es usar el operador de igualdad (==) para comparar la variable edad con el valor 18. Por ejemplo:
'''
edad = int(input("Edad: "))
print("Veamos si tu edad es 18...", edad == 18)
