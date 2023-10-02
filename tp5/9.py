#9.	Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña
# y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”.
# Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
#Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.
def login(usuario, contraseña, intentos):
    # Verificar si el usuario y la contraseña son correctos
    if usuario == "usuario1" and contraseña == "asdasd":
        return True
    else:
        # Si no son correctos, incrementar el número de intentos en uno
        intentos += 1
        return False

# Inicializar el número de intentos en cero
intentos = 0
# Crear un bucle para pedir el usuario y la contraseña hasta que se haga login o se agoten los intentos
while True:
    # Pedir el usuario y la contraseña por pantalla
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")
    # Intentar hacer login usando la función definida
    if login(usuario, contraseña, intentos):
        # Si se hace login, mostrar un mensaje de éxito y salir del bucle
        print("Login exitoso.")
        break
    else:
        # Si no se hace login, mostrar un mensaje de error y verificar si se agotaron los intentos
        print("Usuario o contraseña incorrectos.")
        if intentos == 3:
            # Si se agotaron los intentos, mostrar un mensaje de bloqueo y salir del bucle
            print("Se ha bloqueado el acceso por exceder el número de intentos.")
            break