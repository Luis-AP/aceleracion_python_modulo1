# Se tiene un cupo limitado de inscripciones a un curso.
# Se pide que el usuario ingrese su nombre, apellido, email

# Se define el cupo máximo de inscripciones
max_inscriptions = 3

inscriptions = 0

while inscriptions < max_inscriptions:
    first_name = input("Ingrese su nombre: ")
    last_name = input("Ingrese su apellido: ")
    email = input("Ingrese su email: ")

    # Se incrementa el contador de inscripciones
    inscriptions += 1
    print(
        f"Gracias {first_name} {last_name} por inscribirte al curso, te hemos enviado un email de confirmación a {email}"
    )
    # Guardar los datos de la inscripción
    # ...
    # ...

print("Se acabaron los cupos")
