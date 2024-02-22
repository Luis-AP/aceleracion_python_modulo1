# Ejemplo de dos funciones con mucho acoplamiento
def get_employee_bonus(employee):
    bonus = 0
    if employee[4] >= 12:
        bonus = employee[3] * 0.25
    elif employee[4] >= 6:
        bonus = employee[3] * 0.10
    return bonus


def print_employee_bonus(employee):
    bonus = get_employee_bonus(employee)
    print(f"El empleado {employee[5]} recibirá un bono de ${bonus:.2f}")


# Ejemplo de dos funciones con poco acoplamiento
def get_employee_bonus(employee):
    bonus = 0
    if employee[4] >= 12:
        bonus = employee[3] * 0.25
    elif employee[4] >= 6:
        bonus = employee[3] * 0.10
    return bonus


def print_employee_bonus(bonus, employee_name):
    print(f"El empleado {employee_name} recibirá un bono de ${bonus:.2f}")
