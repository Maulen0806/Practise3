def kwargs_me(**dict):
    for key, value in dict.items():
        print(f"{key}: {value}")
d = {"name": "Maulenali", "age": 19, "hobby": "Videogames, gym"}
print(kwargs_me(**d))
