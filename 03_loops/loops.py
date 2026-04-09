# n = int(input("Enter the value of n: "))

# i = 1
# while i <= 10:
#     print(i * n)
#     i += 1

# n = int(input("Enter the value of n: "))
# m = int(input("Enter the value of m: "))

# i = 1
# while i <= m:
#     print(i * n)
#     i += 1


# Using for loop

# n = int(input("Enter the value of n: "))

# for i in range(1, 11):
#     print(i * n)


# n = int(input("Enter the value of n: "))
# m = int(input("Enter the value of m: "))

# for i in range(1 , m+1):
#     print(i * n)

# break in python

# n = int(input("Enter the value of n: "))
# x = 2
# while x <= n:
#     if n % x == 0:
#         print(x)
#     break


# n = int(input("Enter the value of n: "))
# for x in range(2, n+1):
#     if n % x == 0:
#         print(x)
#         break


# n = int(input("Enter the value of n: "))
# x = 2

# while x <= n:
#     if n % x == 0:
#         print(n," is divisible by ",x)
#         break
#     x = x + 1

# this loop will print num from i to n
# n = int(input("Enter the value of n: "))
# i = 1
# while i <= 100:
#     if i == n:
#         break
#     print(i)
#     i = i + 1
# print(i)

# continue in python

# l = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# for x in l:
#     if x % 2 == 0:
#         continue
#     print(x)


# i = 0
# while i <= 5:
#     if i == 3:
#         i = i + 1
#         continue
#     print(i, i * i)
#     i = i + 1


# l = [10, 16, 17, 18, 9, 15, 21, 13]
# for x in l:
#     if x % 5 == 0:
#         continue
#     if x % 7 == 0:
#         break
#     print(x)

# print("Bye")



# for i in range(1, 1 * 10+1, 1):
#     print(i, end=" ")
# print()
# for i in range(2, 2 * 10+1, 2):
#     print(i, end=" ")
# print()
# for i in range(3, 3 * 10 + 1, 3):
#     print(i, end=" ")
# print()

################################################

# short and best way to print the table of 1 to 10

# for i in range(1, 11):
#     for j in range(i, i * 10 + 1, i):
#         print(j, end=" ")
#     print()

################################################

# for i in range(1, 3):
#     j = 1
#     while j < 3:
#         print(i , j)
#         j = j + 1
#     print("GFG")

################################################

# ll = [[10, 20, 30], [40, 50, 60,], [70, 80]]  # List of list

# for l in ll:
#     for x in l:
#         print(x, end=" ")
#     print()

###################################################################################################

###############################  Pattern  ####################################

####################################################################################################
# square pattern

# n = int(input())

# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()

############## right angle triangle #########################

# n = int(input())

# for i in range(n):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()


##################  Hollow square pattern #########

# n = int(input())

# for i in range(n):
#     row = ""
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             row += "* "
#         else:
#             row += "  "
#     print(row.rstrip())

######################## inverted right triangle #############################


# n = int(input())

# for i in range(n):
#     for j in range(n - i):
#         print("* ",end="")
#     print()

############################## Pyramid pattern ###############################

# n = int(input())

# for i in range(n):
#     for j in range(n-i-1):
#         print("  ", end="")
#     for k in range(2*i+1):
#         print("* ", end="")
#     print()

#############################  Count of digits in number  #################################

# x = int(input())

# res = 0
# while x > 0:
#     x = x // 10
#     res += 1
# print("Count of digits in x is ",res)

####################################################################################################

###################################### Factorial  #######################################

######################################################################################################

# n = int(input("Enter a number: "))

# fact = 1
# for i in range(1, n + 1):
#     fact *= i

# print("Factorial:", fact)

# import math
# n = int(input("Enter a number "))
# fact = math.factorial(n)
# print(f"factorial of {n} is {fact}")


##################################  GCD  ##########################################

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))

# small = min(a,b)
# for i in range(1, small + 1):
#     if(a % i == 0 and b % i == 0):
#         gcd = i
# print("GCD is ",gcd)

# import math
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# gcd = math.gcd(a,b)
# print(f"GCD of {a} and {b} is {gcd}")

###################################  LCM  ############################################

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))

# res = max(a, b)
# while res <= a*b:
#     if (res % a == 0 and res % b == 0):
#         break
#     res += 1
# print(f"LCM of {a} and {b} is {res}")


# using math library

# import math
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# gcd = math.gcd(a,b)
# lcm = (a*b) // gcd
# print(f"LCM of {a} and {b} is {lcm}")

##################################  Check num is Prime or not  ########################################

# Given an integer n check if n is prime or not.

# n = int(input("Enter an integer: "))

# if n <= 1:
#     print("Not Prime")
# else:
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")

##################################  Fibonacci numbers  ######################################

# n = int(input("Enter the number of terms: "))

# if n == 0:
#     print(0)
# elif n == 1:
#     print(1, 1)
# else:
#     print(1, 1, end=" ")
#     a = 1
#     b = 1
#     for i in range(2, n+1):
#         c = a + b
#         print(c, end=" ")
#         a = b
#         b = c


# using while loop
# n = int(input())
# a, b = 0, 1 # a = 1, b = 1
# count = 0
# while count < n:
#     print(a, end=" ")
#     a, b = b, a + b
#     count += 1


############################## to know the index num of fib  #################################

# n = int(input())

# a, b = 0, 1

# for i in range(n):
#     a, b = b, a +b
# print(a, end=" ")


###################################### Next Prime Number ######################################

# def nextPrime(n):
#     # return next prime number
#     num = n + 1 # start checking from the number immediately after n
    
#     while True:
#         is_prime = True # check if 'num' is prime
#         if num < 2:  # prime must be greater than 1
#             is_prime = False
#         else:
#             # check for factors from 2 up to the square root if the num
#             for i in range(2, int(num**0.5) +1):
#                 if num % i == 0:
#                     is_prime = False
#                     break
#             # if no factor were found, num is the next prime 
#             if is_prime:
#                 return num
#             # otherwise, move to the next number
#             num += 1
# n = int(input("Enter a number "))
# result = nextPrime(n)
# print(f"The first prime number greater than {n} is: {result}")

# check for prime 
# n = int(input("Enter a number "))

# if n <= 1:
#     print("No")
# else:
#     # range(x, y) gives number from x to y-1
#     for i in range(2, n):
#         if n % i == 0:
#             print("No")
#             break
#     else:
#         print("Yes")

#####################  All Divisor of a number #############################

# n = int(input("Enter a number: "))

# for i in range(1, n+1):
#     if n % i == 0:
#         print(i)

#### using while loop

# i = 1
# while i <= n:
#     if n % i == 0:
#         print(i)
#     i += 1



##############################  Optimizations of All divisor and prime ##############################

# n = int(input("Enter a number: "))

# x = 1
# while x*x < n:
#     if n % x == 0:
#         print(x)
#         print(n/x)
#     x += 1
# if x*x == n:
#     print(x)

###############################  Optimizations of prime  #################################

# n = int(input("Enter a number: "))

# if n <= 1:
#     print("Not a prime number")
# else:
#     x = 2
#     while x*x < n:
#         if n % x == 0:
#             print("Not a prime number")
#             break
#         x += 1
#     else:
#         print("Prime number")


#################################  Capitalize and count  ####################################

# s = input()

# # Your code here
# caps = s.title()
# word_count = len(s.split())

# print(caps)
# print(word_count)


######################################  MCQ  ################################################3
# x = 0
# while x < 100:
#     x += 2
# print(x)

# ans : 100

# x = "GFG"
# for i in range(x):
#     print(i)

# Ans: error


# i = 1
# while True:
#    if i%7 == 0:
#    	 break    
#    print(i, end=" ")
#    i += 1

# Ans: 1 2 3 4 5 6

# True = False
# while True:
#     print(True)
#     break

# Ans: syntax error, boolean can't assigned


# var = 10
# for i in range(10):
#     for j in range(2,10,1):
#         if var % 2 == 0:
#             continue
#         else:
#             var += 1
# print(var)

# Ans: 10

# for num in range(10, 14):
#    for i in range(2, num):
#          if num%i == 1:
#               print(num)
#               break
         
# Ans:
# 10
# 11
# 12
# 13



            