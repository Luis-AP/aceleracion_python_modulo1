def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


def mostrar_par(numero):
    resultado = es_par(numero)
    if resultado:
        print("Es par")
    else:
        print("Es impar")
    return resultado
