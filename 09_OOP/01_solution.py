# 1. Basic class and model.
#! Problem: Create a car class with attribute like brand and model.Then create an instance of the class.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Fortuner")
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Mahindra", "Scorpio")
print(my_new_car.brand)
print(my_new_car.model)