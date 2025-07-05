class Animals:
    pass

class Pet(Animals):
    pass

class Dog(Pet):
    def bark(self):
        print("Bow Bow")

a = Dog()
a.bark()