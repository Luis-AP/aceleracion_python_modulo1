age = int(input("Ingrese su edad: "))

if 1 <= age < 12:
    print("Eres un niño")
elif 12 <= age < 18:
    print("Eres un adolescente")
elif 18 <= age < 25:
    print("Eres un adulto joven")
elif 25 <= age < 65:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")

archivo1 = "Luis"
archivo2 = "Ana"
archivo3 = "Juan"
archivo4 = "Pedro"


if archivo1 != archivo2 != archivo3 != archivo4:
    print("Todos los archivos son distintos. [en cadena]")
