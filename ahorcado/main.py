# importo el modulo random para elegir una palabra al azar
import random

# defino una lista de palabras
words = ["utn", "programacion", "python", "computadora", "internet", "algoritmo", "codigo", "bug", "debug", "variable", "profesora", "aprobar"]

# con random agarro una palabra de la lista
secret_word = random.choice(words)

# esta variable almacena el estado actual de la palabra
hidden_word = "_" * len(secret_word)

# esta variable fija la cantidad de intentos que puede tener el cliente
attempts = 6

# variable de salida incializada
finished = False

# mensaje de inicio de juego
print("Bienvenido al juego del ahorcado. Tenes que adivinar la palabra secreta letra por letra. Tenes 6 intentos antes de perder el juego. Buena suerte!")

# muestro el estado de la palabra (cantidad de letras)
print(hidden_word)

# bucle para correr el juego hasta que el cliente gane o pierda
while not finished:

    # le pido al jugador que ingrese una letra y lo paso a minusculas
    letter = input("Ingresa una letra: ").lower()

    # esta condicion se fija si es una letra valida
    if len(letter) == 1 and letter.isalpha():

        # esta condicion se fija si la letra que ingreso el cliente esta en la palabra
        if letter in secret_word:

            # aca se actualiza la palabra, se va el guion y si la letra esta se remplaza
            hidden_word = "".join([letter if secret_word[i] == letter else hidden_word[i] for i in range(len(secret_word))])

            # mensaje avisando que la adivino
            print("Adivinaste una letra correctamente.")

        else:

            # si pierde le resto un intento
            attempts -= 1

            # mensaje avisando que se equivoco
            print(f"Letra incorrecta, te quedan {attempts} intentos.")

        # vuelvo a mostrar el estado de la palabra
        print(hidden_word)

        # aca me fijo si el jugador adivino la palabra entera
        if "_" not in hidden_word:

            # mensaje avisando que gano
            print("Bien! adivinaste la palabra secreta.")

            # si gano pongo en true la condicion del bucle
            finished = True

        # aca verifico si se quedo sin intentos
        elif attempts == 0:

            # mensaje avisando que perdio y mostrando la palabra
            print(f"Perdiste :(, La palabra secreta era {secret_word}.")

            # si perdio cambio la condicion del bucle
            finished = True

    else:

        # mensaje de que no ingreso una palabra valida
        print("Por favor, ingresa una letra valida.")
