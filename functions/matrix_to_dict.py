def matrix_to_dict(matrix):
    dictionary = {}

    if (
        matrix and len(matrix) > 1
    ):  # Asegurarse de que hay más de una fila (encabezados + al menos 1 fila de datos)
        header = matrix[0][
            1:
        ]  # Excluir el "id" del encabezado para obtener solo los nombres de las columnas
        for row in matrix[1:]:  # Ignorar la fila del encabezado
            main_key = row[0]  # El identificador del usuario es el primer elemento
            values = row[1:]  # El resto de la fila son los valores
            inner_dict = dict(
                zip(header, values)
            )  # Crear un diccionario interno con encabezados como claves
            dictionary[main_key] = inner_dict
    return dictionary


# Usando la matriz de ejemplo generada por dict_to_matrix
matrix_example = [
    ["id", "nombre", "edad", "email"],
    ["usuario1", "Juan", 30, "juan@gmail.com"],
    ["usuario2", "Ana", 25, "ana@hotmail.com"],
    ["usuario3", "Pedro", 40, "pedro@gmail.com"],
]

# Convertir la matriz de nuevo a un diccionario
converted_dict = matrix_to_dict(matrix_example)

for key, value in converted_dict.items():
    print(f"{key}: {value}")
