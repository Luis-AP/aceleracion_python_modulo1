numero = int(input("Ingrese un número: "))
if numero > 0:
    # En este punto ya sabemos que el número es positivo
    if numero % 2 == 0:
        print("El número ingresado es positivo y par.")
    else:
        print("El número ingresado es positivo e impar.")
else:
    print("El número ingresado no es positivo.")
