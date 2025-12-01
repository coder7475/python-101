class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        return "Engine started"

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)  # Call the constructor of the base class
        self.doors = doors

    def start_engine(self):
        base_message = super().start_engine()  # Call the method from the base class
        return f"{base_message} - Car engine roars!"

# Example usage:
my_car = Car("Toyota", "Corolla", 4)
print(my_car.start_engine())  # Output: Engine started - Car engine roars!