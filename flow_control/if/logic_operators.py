conditions_accepted = False
if input("¿Acepta las condiciones? (si/no): ") == "si":
    conditions_accepted = True

if not conditions_accepted:
    print("No puede iniciar sesión si no da su conformidad a las condiciones del sitio")
else:
    email = "luis@gmail.com"
    email_input = input("Ingrese su email: ")

    username = "luis"
    username_input = input("Ingrese un nombre de usuario: ")

    password = "miClave"
    password_input = input("Ingrese la contraseña: ")

    if (
        username == username_input or email == email_input
    ) and password == password_input:
        print("Contraseña correcta. Te damos la bienvenida.")
    else:
        print("Credenciales incorrectas.")
