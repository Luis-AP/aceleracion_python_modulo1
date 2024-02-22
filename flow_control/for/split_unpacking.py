# Contamos con información de un archivo de texto donde cada columna está separada por comas
# Suponemos que el archivo cuenta con 5 columnas:
# - Nombre: cadena de caracteres con dos palabras
# - Apellido: cadena de caracteres con una o dos palabras
# - Email: cadena de caracteres con el formato de un correo electrónico
# - Salario: número real con dos cifras decimales. Este representa el salario mensual de la persona
# - Antigüedad: número entero que representa la cantidad de meses que lleva trabajando la persona

# Vamos a simular el contenido del archivo con una lista de strings

rows = [
    "Juan Emilio, Pérez, juanpe@gmail.com, 150000.14, 10",
    "María Elena, Gómez, mariaelena@hotmail.com, 200000.21, 18",
    "Carlos Alberto, López, carlitos99@hotmail.com, 300000.00, 23",
    "Julian Andrés, Rodríguez, julian@gmail.com, 250000.44, 5",
]

# Queremos obtener una lista de listas donde cada sublista contenga la información de una persona
employees = []
for row in rows:
    # Usamos el método split() para separar la cadena de caracteres por comas
    employee = row.split(",")
    # employee = (
    #     employee[0],
    #     employee[1].strip(),
    #     employee[2].strip(),
    #     float(employee[3]),
    #     int(employee[4]),
    #     ", ".join(employee[1::-1]),
    # )
    # employees.append(employee)

# Se acerca final del año y queremos dar un bono a los empleados
# en función de su antigüedad y salario que tienen

for employee in employees:
    # firstname, lastname, _, salary, seniority = employee

    bonus = 0
    if employee[4] >= 12:
        bonus = employee[3] * 0.25
    elif employee[4] >= 6:
        bonus = employee[3] * 0.10

    print(f"El empleado {employee[5]} recibirá un bono de ${bonus:.2f}")
