# Polymorphism
class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")  

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Example usage:
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Output: Woof! Meow!

# Operator Overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
print(v1 + v2)  # (6, 8)
