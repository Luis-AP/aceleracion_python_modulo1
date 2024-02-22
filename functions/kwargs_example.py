def dict_to_matrix(**kwargs):
    matrix = []

    # Aseguramos que el diccionario no esté vacío para proceder
    if kwargs:
        for main_key in kwargs:
            header = ["id"] + list(kwargs[main_key].keys())
            break  # Rompemos después de obtener el primer sub-diccionario

        matrix.append(header)

        # Llenamos la lista con los datos de cada usuario
        for main_key, inner_dict in kwargs.items():
            row = [main_key] + list(inner_dict.values())
            matrix.append(row)
    else:
        matrix.append(["id"])  # Encabezado vacío si no hay datos

    return matrix


user_matrix = dict_to_matrix(
    juancito={"nombre": "Juan", "edad": 30, "email": "juan@gmail.com"},
    ana={"nombre": "Ana", "edad": 25, "email": "ana@hotmail.com"},
    carlitos={"nombre": "Carlos Santana", "edad": 40, "email": "carlitos@gmail.com"},
)

for row in user_matrix:
    print(row)
