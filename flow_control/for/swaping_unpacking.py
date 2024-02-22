# Ejemplo de swap de variables con unpacking

num1 = 10
num2 = 20

print(f"num1: {num1}, num2: {num2}")
# Cambiamos el valor de las variables

# aux = num1
# num1 = num2
# num2 = aux

# print(f"num1: {num1}, num2: {num2}")

num1, num2 = (num2, num1)

print(f"num1: {num1}, num2: {num2}")
