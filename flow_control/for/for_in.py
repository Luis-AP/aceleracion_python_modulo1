dias = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado")
# la lista `dias` solo nos sirve para ir mostrando el día que solicitamos
tareas_terminadas = []  # lista en donde se van a guardar las tareas terminadas

print("Ingrese la cantidad de tareas terminadas por cada día de la semana")
for dia in dias:
    cantidad = int(input(f"Ingrese la cantidad de tareas terminadas del día {dia}: "))
    tareas_terminadas.append(cantidad)

print(tareas_terminadas)  # mostramos la lista armada
print("La cantidad total de tareas terminadas en la semana es:", sum(tareas_terminadas))
