
####! Question- 1:
"""
Ek abstract class banao Animal naam se

Ek abstract method: sound()

Phir:

Dog class → "Bark"
Cat class → "Meow"
"""


# from abc import ABC, abstractmethod

# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         return "Bark"
    
# class Cat(Animal):
#     def sound(self):
#         return "Meow"

# d = Dog()
# print(d.sound())
# c = Cat()
# print(c.sound())

###! Question - 2 :

"""
Ek class Shape banao

Abstract method: area()

Phir:

Square → side = 4 → area print karo

👉 Expected:

Area of square: 16
"""
# from abc import ABC, abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side * self.side

# a = Square(4)
# print("Area of square:", a.area())



###!  Question - 3:

"""
Ek abstract class Payment banao

method: pay(amount)

Child classes:

UPI → "Paid {amount} using UPI"
Card → "Paid {amount} using Card"

👉 Call both
"""

# from abc import ABC, abstractmethod

# class Payment(ABC):
#     @abstractmethod
#     def pay(self):
#         pass

# class UPI(Payment):
#     def pay(self, amount):
#         return f"Paid {amount} using UPI"

# class Card(Payment):
#     def pay(self, amount):
#         return f"Paid {amount} using Card"
    
# u = UPI()
# print(u.pay(500))
# c = Card()
# print(c.pay(1000))

####! Question- 4:
"""
Ek class BankAccount banao:

Requirements:
private variable → __balance
methods:
deposit(amount)
show_balance()

👉 Rule:

Balance ko direct access nahi karna (abstraction)
"""

# class BankBalance:
#     def __init__(self):
#         self.__balance = 0

#     def deposit(self, amount):
#         self.__balance += amount
    
#     def show_balance(self):
#         print("Balance:", self.__balance)

# b = BankBalance()

# b.show_balance() # 0
# b.deposit(500)
# b.show_balance() # 500


####! Question- 5:
"""
Ek abstract class Employee banao:

Method:
calculate_salary()
Child classes:
FullTime → fixed salary = 50000
PartTime → salary = hours * rate
"""

# from abc import ABC, abstractmethod

# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         pass

# class FullTime(Employee):
#     def calculate_salary(self):
#         return 50000
    
# class PartTime(Employee):
#     def __init__(self, hour, rate):
#         self.hour = hour
#         self.rate = rate
        
#     def calculate_salary(self):
#         return self.hour * self.rate
    
# f = FullTime()
# print("FullTime salary:", f.calculate_salary())
# p = PartTime(2, 1500)
# print("PartTime salary:", p.calculate_salary())


####! Question - 6

"""
Your task is to create a Person class in Python that demonstrates encapsulation. This class should have two "private" attributes:

name (String) with a default value of "Geeks".
age (int) with a default value of 10.
The class should provide public methods to access and modify these private attributes:

Getter Methods: get_name() and get_age()
Setter Methods: set_name(name) and set_age(age)


"""
# class Person:
#     def __init__(self):
#         self.__name = "Geeks"
#         self.__age = 10
    
#     # getter    
#     def get_name(self):
#         return self.__name
        
#     def get_age(self):
#         return self.__age
    
#     # setter    
#     def set_name(self, name):
#         self.__name = name
        
#     def set_age(self, age):
#         self.__age = age
        
# person = Person()

# print(person.get_name(), end=" ")

# person.set_name("John")
# person.set_age(21)

# print(person.get_name(), person.get_age())

######! Question - 7

"""
Class Name: Shape (Abstract Class)
Attributes: color (String)
Constructor: Shape(c) -> assign value of c to color attribute
Methods: get_color() -> returns value of color
         get_area() -> abstract method with float return type

Class Name: Square (extends Shape)
Attributes: side (float)
Constructor: Square(c, side) -> calls super(c) to initialize the color and assigns the value to side.
Methods: get_area() -> returns the area of the square (side * side).
"""

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def __init__(self, c):
#         self.color = c
    
#     def get_color(self):
#         return self.color
    
#     def get_area(self):
#         pass
        
# class Square(Shape):
#     def __init__(self, c, side):
#         super().__init__(c)
#         self.side = side
        
#     def get_area(self):
#         return self.side * self.side
        
# color = "Red"
# side = 0.5
# obj = Square(color, side)

# print(obj.get_color(), obj.get_area())