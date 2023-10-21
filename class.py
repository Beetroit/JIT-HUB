class Dog:
    def __init__(self):
        self.name = "Fido"
        self.age = 10
        self.breed = "Labrador"
        self.color = "White"
        self.weight = 100
        self.height = 100
        self.legs = 4
        self.eyes = 2
    def __str__(self):
        return f"{self.name} is a {self.breed} dog with {self.legs} legs and {self.eyes} eyes"