def agregar(elem, lista=None):
    if lista is None:
        lista = []
    lista.append(elem)
    return lista


lista = agregar("Luis")

print(lista)

lista = agregar("Susana")

print(lista)

lista2 = agregar("Jorge")
print(lista2)

lista3 = agregar("Ana", [])
print(lista3)
