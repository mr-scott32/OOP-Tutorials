class Dog:
    def __init__(self, name, breed, woof):
        self.name = name
        self.breed = breed
        self.woof = woof
    
    def bark(self):
        print(f'{self.name} says {self.woof}!')
    