user_luis = {
    "firstname": "Luis",
    "lastname": "Parada",
    "age": 30,
    "email": ["lap@gmail.com", "luis@gmail.com"],
}

user_2 = {
    "firstname": "Jorge",
    "lastname": "Perez",
    "age": 30,
    "email": ["lap@gmail.com", "luis@gmail.com"],
}

lista = [user_luis, user_2]

print(user_luis)

user_luis["firstname"] = "Luis Augusto"
user_luis["dni"] = 23131223

print(user_luis)

print(user_luis["firstname"])
print(user_luis.get("cuil"))

del user_luis["dni"]

print(user_luis)

# users = {
#     ,
#     "user2": {
#         "name": "Jane",
#         "age": 25,
#         "email": "jane@gmail.com",
#     },
#     "user3": {
#         "name": "Bob",
#         "age": 35,
#         "email": "bob@gmail.com",
#     },
# }
