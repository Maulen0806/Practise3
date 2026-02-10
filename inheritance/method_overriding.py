class animal:
    def __init__(self, name):
        self.name = name
class dog(animal):
    def speak(self):
        return "Woof-woof"
class cat(animal):
    def __init__(self, name, color):
        super().__init__(name)  
        self.color = color  
    def speak(self):  
        return "Meow"
i1 = dog("Aktos")
i2 = cat("Murkabai", "Grey")
i3 = cat("Tigra", "Orange")
print(i1.speak())
print(i2.speak())
print(i3.color)
