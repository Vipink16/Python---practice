"""
Object Oriented Programming empowers developers to build modular, maintainable and scalable applications. OOP is a way of organizing code that uses objects and classes to represent real-world entities and their behavior. In OOP, object has attributes thing that has specific data and can perform certain actions using methods.

* Organizes code into classes and objects.
* Supports encapsulation to group data and methods together.
* Enables inheritance for reusability and hierarchy.
* Allows polymorphism for flexible method implementation.
* Improves modularity, scalability and maintainability.
"""

#! Creating Object

# class Dog:
#     species = "Canine" # class attribute

#     def __init__(self, name, age):
#         self.name = name  # Instance attribute
#         self.age = age   # Instance attribute

# # creating an object for dog class.
# dog1 = Dog("Buddy", 3)

# print(dog1.name)
# print(dog1.age)
# print(dog1.species)


"""
#! Four Pillars of OOP

The Four Pillars of Object-Oriented Programming (OOP) form the foundation for designing structured, reusable, and maintainable software.

* 1. Inheritance
Inheritance allows a class (child class) to acquire properties and methods of another class (parent class). It supports hierarchical classification and promotes code reuse.

* 2. Polymorphism
Polymorphism means "same operation, different behavior." It allows functions or methods with the same name to work differently depending on the type of object they are acting upon.

* 3. Encapsulation
Encapsulation is the bundling of data (attributes) and methods (functions) within a class, restricting access to some components to control interactions. A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.

* 4. Data Abstraction 
Abstraction hides the internal implementation details while exposing only the necessary functionality. It helps focus on "what to do" rather than "how to do it."
"""

#! __str__() Method

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} is {self.age} years old."
# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Charlie", 5)

# print(dog1)  
# print(dog2)

"""
#! Class Variables

A class variable is a variable that belongs to the class itself rather than to any specific object. All instances of the class share the same copy of this variable.

* Defined inside the class but outside all methods
* Accessed using the class name or an object
* Memory is allocated only once
"""

# class student:
#     school = "ABC School" # Class Variable

# s1 = student()
# s2 = student()

# print(s1.school)
# print(s2.school)

"""
school is a class variable
Both s1 and s2 share the same value
The variable belongs to the class, not to individual objects
"""

"""
#! Instance Variables

Instance variables are variables that belong to a specific object. Each object maintains its own copy of these variables.

* Defined inside methods (usually __init__())
* Unique for each object
* Changes affect only that particular object
"""

# class student:
#     def __init__(self, name): # Instance Variable
#         self.name = name

# s1 = student("Emily")
# s2 = student("Jake")

# print(s1.name)
# print(s2.name)

"""
name is an instance variable
Each object has its own value
Changing one object's value does not affect the other
"""

#! Class variable vs Instance variable

# This example demonstrates how class variables are shared and instance variables remain separate.

# class CSStudent:
#     stream = "CSE"

#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll

# a = CSStudent('Rose', 1)
# b = CSStudent('Jack', 2)

# print(a.stream)
# print(b.stream)
# print(a.name)
# print(b.name)


#! Access Modifiers: Public, Private

# Public Access Modifiers

# class student:
#     def __init__(self, name, age):
#         self.studentName = name
#         self.studentAge = age
    
#     def displayAge(self):
#         print("Age:", self.studentAge)

# obj = student("Jay", 20)

# print("Name:", obj.studentName)
# obj.displayAge()

"""
studentName and studentAge are public variables, so they can be accessed directly from outside the class (obj.studentName).
displayAge() is a public method, so it can be called normally using obj.displayAge().
In Python, class members are public by default, so both the variables and the methods will appear when you check dir(obj).
"""

"""
#! Protected Access Modifier

* A member is considered protected if its name starts with a single underscore (_).
* Convention only: It suggests that the member should not be accessed outside the class except by subclasses.
* Still, Python allows direct access if explicitly called.
"""

# class Student:
#     def __init__(self, name, roll, branch):
#         self._name = name
#         self._roll= roll
#         self._branch = branch
    
#     def _displayRollAndBranch(self):
#         print("Roll:", self._roll)
#         print("Branch:", self._branch)
    
# class Geek(Student):
#     def displayDetails(self):
#         print("Name:", self._name)
#         self._displayRollAndBranch()

# obj = Geek("R2J", 123, "IT")
# obj.displayDetails()

"""
_name, _roll, and _branch are protected members, meant to be used within the class and subclasses.
_displayRollAndBranch() is a protected method, accessed by the subclass Geek.
Python allows direct access (e.g., obj._name), but by convention, it's avoided.
"""

#! Private Access Modifier

"""
* A member is private if its name starts with double underscores (__).
* Python does not enforce strict privacy — instead, it uses Name Mangling.
* The interpreter renames __var to _ClassName__var internally.

#! Note: A name like __age__ (double underscores at both start and end) is not private. It is treated as a special 'dunder' name in Python and name mangling does not apply to it.
"""

class Geek:
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch
    
    def __displayDetails(self):
        print("Name:", self.__name)
        print("Roll:", self.__roll)
        print("Branch:", self.__branch)

    def accessPrivateFunction(self):
        self.__displayDetails()

obj = Geek("R2J", 1234, "CSE")
obj.accessPrivateFunction()
print(obj._Geek__name)

"""
__name, __roll, __branch: private variables
__displayDetails(): private method
Direct access from outside will raise AttributeError
Access allowed inside the class or via name mangling (obj._Geek__name)
"""

#! Using all access modifiers

class Super:
    publicData = "Public Data Member"
    _protectedData = "Protected Data Member"
    __privateData = "Private Data Member"

    def accessPrivateMembers(self):
        print("Accessing inside class:", self.__privateData)


class Sub(Super):
    def accessProtectedMembers(self):
        print("Accessing inside subclass:", self._protectedData)

obj = Sub()

print(obj.publicData)
print(obj._protectedData)
obj.accessPrivateMembers()
print(obj._Super__privateData)

"""
* publicData is accessed directly using obj.publicData.
* _protectedData is accessed using obj._protectedData (allowed but discouraged by convention).
* __privateData is accessed inside the class using self.__privateData.
* Outside the class, private data is accessed using name mangling: obj._Super__privateData.
"""