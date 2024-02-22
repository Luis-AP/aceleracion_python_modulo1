# ingresa y almacena la cantidad de tareas terminadas por un empleado para cada día de la semana
dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado"]
# la lista `dias` solo nos sirve para ir mostrando el día que solicitamos
tareas_terminadas = []  # lista en donde se van a guardar las tareas terminadas
i = 0
print("Ingrese la cantidad de tareas terminadas por cada día de la semana")
while i < len(dias):
    cantidad = int(
        input(f"Ingrese la cantidad de tareas terminadas del día {dias[i]}: ")
    )
    tareas_terminadas.append(cantidad)
    i += 1

print(tareas_terminadas)  # mostramos la lista armada
print("La cantidad total de tareas terminadas en la semana es:", sum(tareas_terminadas))
