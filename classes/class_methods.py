class cls:
    def __init__(self, name, year):
        self.name = name
        self.year = year
    def __str__(self):
        return f"I'm {self.name}, I was born in {year}"
name = input()
year = input()
c1 = cls(name, year)
print(c1)


