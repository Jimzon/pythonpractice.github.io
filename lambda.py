people = [
    {"name":"Pogi", "surname": "Gwapa"},
    {"name":"Pogiboy", "surname":"Good boy"},
    {"name":"Ate", "surname":"Khaelang"}
]

# def fersons(person):
#     return person["surname"]

people.sort(key=lambda person: person["name"])

print(people)

