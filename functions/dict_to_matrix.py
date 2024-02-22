def dict_to_matrix(dictionary):
    matrix = []

    if dictionary:
        for main_key in dictionary:
            user_keys = dictionary[main_key].keys()
            headers = ["id"] + list(user_keys)
            break  # Rompemos después de obtener el primer sub-diccionario

        matrix.append(headers)

        # Llenamos la lista con los datos de cada usuario
        for main_key, inner_dict in dictionary.items():
            user_data = inner_dict.values()
            row = [main_key] + list(user_data)
            matrix.append(row)
    else:
        matrix.append([[]])

    return matrix


users = {
    "usuario1": {"nombre": "Juan", "edad": 30, "email": "juan@gmail.com"},
    "usuario2": {"nombre": "Ana", "edad": 25, "email": "ana@hotmail.com"},
    "usuario3": {"nombre": "Pedro", "edad": 40, "email": "pedro@gmail.com"},
}

user_matrix = dict_to_matrix(users)

for row in user_matrix:
    print(row)
