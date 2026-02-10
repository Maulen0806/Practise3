class cls1():
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name
    def me(self):
        print(f"I'm {surname} {name}")
class cls2(cls1):
    def __init__(self, surname, name):
        super().__init__(surname, name)
class cls3(cls2):
    def __init__(self, surname, name):
        super().__init__(surname, name)
name = input()
surname = input()
c1 = cls3(surname, name)
c1.me()
