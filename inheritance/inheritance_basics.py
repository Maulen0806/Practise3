class cls1():
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name
    def me(self):
        print(f"I'm {self.surname} {self.name}")
class cls2(cls1):
    pass
name = input()
surname = input()
c1 = cls2(surname, name)
c1.me()
