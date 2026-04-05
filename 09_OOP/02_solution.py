# 2.Class method and self.
# Add a method to the car that displays the full name of the car(brand and model).

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

my_car = Car("Toyota", "Fortuner")
print(my_car.full_name())