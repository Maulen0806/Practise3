class cls:
    animal = "Wild animal"
    def __init__(self, name):
        self.name = name
name = input()
c1 = cls(name)
print(c1.name)
print(c1.animal)
del cls.animal
print(c1.animal)
