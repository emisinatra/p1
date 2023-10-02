#2.	Escribir una función que, dado un string, retorne la longitud de la última palabra.
# Se considera que las palabras están separadas por uno o más espacios.
# También podría haber espacios al principio o al final del string pasado por parámetro.
def longitud_ultima_palabra(texto):
  # Eliminar los espacios al principio y al final del texto
  texto = texto.strip()
  # Separar el texto por los espacios
  palabras = texto.split()
  # Si el texto está vacío, devolver 0
  if len(palabras) == 0:
    return 0
  # Si no, devolver la longitud de la última palabra
  ultima_palabra = palabras[-1]
  return len(ultima_palabra)


# Pedir un texto por pantalla y mostrar la longitud de la última palabra
texto = input("Ingrese un texto: ")
longitud = longitud_ultima_palabra(texto)
print(f"La longitud de la última palabra es: {longitud}")
