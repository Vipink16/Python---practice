# a = int(input("Enter value of a: "))
# b = int(input("Enter value of b: "))

# if a > b:
#     print("a is grater")
# elif a < b:
#     print("b is greater")
# else:
#     print("a and b are same")

########################################################################3


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if (a>=b) and (a>=c):
#     print("a is grater than b and c")
# if (b>=a) and (b>=c):
#     print("b is greater than a and c")
# if (c>=a) and (c>=b):
#     print("c is greater than a and b")

############################# Leap Year  ################################


# year = int(input("Enter the year: "))

# if year % 4 == 0 and year % 100 != 0:
#     print("Leap Year")
# elif year % 400 == 0:
#     print("Leap Year")
# else:
#     print("Not a leap year")


# import sys
# print("""Please select operation:
#       1. Add
#       2. Subtract
#       3. Multiply""")

# choice = int(input("Select operation from 1, 2 and 3: "))
# if choice not in (1,2,3):
#     print("Invalid Choice")
#     sys.exit()

##########################################################################

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# if choice == 1:
#     res = a + b
# elif choice == 2:
#     res = a - b
# else:
#     res = a * b
# print("Result is ",res)

class Solution:
    def calculate(self, a: int, b: int, operator: int) -> None:
        # code here
        if operator == 1:
            print(a + b)
        elif operator == 2:
            print(a - b)
        elif operator == 3:
            print(a * b)
        else:
            print("Invalid Input")
