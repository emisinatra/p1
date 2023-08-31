#Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).
frase = input("Ingrese una frase: ")
vocales = "aeiou"
vocales_en_frase = []
for c in frase.lower():
    if c in vocales and c not in vocales_en_frase:
        vocales_en_frase.append(c)
print("Las vocales que aparecen en la frase son:")
for v in vocales_en_frase:
    print(v)