#12-	Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
contador = 0
for c in frase:
    if c == letra:
        contador += 1
print(f"La letra {letra} aparece {contador} veces en la frase")