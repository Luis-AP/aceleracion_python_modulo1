user = (
    "LUIS AuGUSTo",
    "PAraDA",
    32132131,
    "http://github.com/Luis-AP",
    "LUIS@GMAIL.COM",
    25,
)

# firstname = user[0]
# lastname = user[1]
# email = user[2]
# age = user[3]

# Unpacking
firstname, lastname, *_, age = user

print(firstname, lastname, age)
