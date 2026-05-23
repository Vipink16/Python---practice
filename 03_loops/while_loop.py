
###* 1: Print all the numbers from 1 to 10 using while loop.

# i = 1
# while i <= 10:
#     print(i, end=" ")
#     i += 1

#########################################################################################################!

###* 2: Print number from 10 down to 1 in reverse order.

# i = 10
# while i >= 1:
#     print(i, end=" ")
#     i -= 1

#########################################################################################################!

###* 3: Print all even numbers between 1 and 100.

# i = 2
# while i <= 100:
#     print(i)
#     i += 2

###*  OR  ###


# i = 1
# while i <= 100:
#     if i % 2 == 0:
#         print(i)
#     i += 1

############################################################################################################!

###* 4: Print all odd numbers between 1 and 100.

# i = 1
# while i <= 100:
#     if i % 2 != 0:
#         print(i)
#     i += 1

############################################################################################################!

###* 5: print the multiplication table of given number.

# n = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(n * i)
#     i += 1

# n = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(n, "x", i, "=", n * i)
#     i += 1

############################################################################################################!

###* 6: Calculate and print the sum of first n natural numbers.

# n = int(input("Enter the number: "))
# i = 1
# sum = 0
# while i <= n:
#     sum = sum + i
#     i += 1

# print(f"Sum of natural number till {n} is ",sum)

############################################################################################################!

###* 7: Calculate the sum of all even number from 1 up to n.

# n = int(input("Enter a number: "))

# i = 1
# sum = 0

# while i <= n:
#     if i % 2 == 0:
#         sum += i
#     i += 1
# print("Sum of even number is: ",sum)

###########################################################################################################!

###* 8: Calculate the sum of all odd number from 1 up to n.

# n  = int(input("Enter the number: "))

# i = 1
# sum = 0

# while i <= n:
#     if i % 2 != 0:
#         sum += i
#     i += 1
# print("Sum of odd number: ",sum)

###########################################################################################################!

###* 9: Calculate and print the factorial of given number.

# n = int(input("Enter a number: "))

# fact = 1
# i = 1
# while i <= n:
#     fact = fact * i
#     i += 1
# print(f"Factorial of {n} is ",fact)

##########################################################################################################!

###* 10: Find and print the product of all digits of given numbers.

# n = int(input("Enter a number: "))

# product = 1

# while n > 0:
#     digit = n % 10
#     product = product * digit
#     n = n // 10

# print("Product digits is ",product)

##########################################################################################################!

####* 11:  Count and print the total number of digits in a given number.

# n = int(input("Enter a number: "))

# count = 0
# while n > 0 :
#     n = n // 10
#     count += 1
# print("number of digits is ",count)

##########################################################################################################!

###* 12: Reverse the given number and print the reversed value.

# n = int(input("Enter the a number: "))

# reversed = 0
# while n > 0:
#     digit = n % 10
#     reversed = reversed * 10 + digit
#     n = n // 10
# print(reversed)

#########################################################################################################!

###* 13: Check whether the number is a palindrome.

# n = int(input("Enter a number: "))

# original = n
# reversed = 0

# while n > 0:
#     digit = n % 10
#     reversed = reversed * 10 + digit
#     n = n // 10

# if original == reversed:
#     print("It is a palindrome.")
# else:
#     print("It is not a palindrome.")

#########################################################################################################!

###* 14: Find and print the sum of digits of the given number.

# n = int(input("Enter a number: "))

# i = 1
# sum = 0

# while i <= n:
#     digit = n % 10
#     sum = sum + digit
#     n = n // 10

# print("sum of digits is:",sum)

########################################################################################################!

###* 15: Check whether the given number is an armstrong or not.

# n = int(input("Enter a number: "))

# original = n
# temp = n
# count = 0
# sum = 0

# while temp > 0:
#     temp = temp // 10
#     count +=1

# temp = n
# while temp > 0:
#     digit = temp % 10
#     sum = sum + (digit ** count)
#     temp = temp // 10

# if original == sum:
#     print("Is armstrong")
# else:
#     print("Not a armstrong")

#########*  OR ###########*

# n = int(input("Enter a number: "))

# count = len(str(n)) # count the number of digits

# temp = n # temporary variable to keep original value
# sum = 0

# while temp > 0:
#     digit = temp % 10
#     sum = sum + (digit ** count)
#     temp = temp // 10

# if n == sum:
#     print(f"{n} is an armstrong")
# else:
#     print(f"{n} is not an armstrong")

######################################################################################################!

###* 16: Check whether the given number is a perfect number.
"""
A perfect number is a positive integer that is equal to the sum of its proper positive divisors (excluding the number itself). For example, 6 is perfect because its divisors 1,2,3 sum to 6 (1+2+3=6). The first few perfect numbers are 6, 28, 496, and 8128.
"""
# n = int(input("Enter a number: "))

# i = 1
# sum = 0

# while i < n:
#     if n % i == 0:
#         sum = sum + i
#     i += 1

# if sum == n:
#     print(f"{n} is a perfect number.")
# else:
#     print(f"{n} is not a perfect number.")

#######################################################################################################!

###* 17: Print all prime numbers between 1 to 100.


# n = 2

# while n <= 100:
#     i = 2
#     is_prime = True

#     while i < n:
#         if n % i == 0:
#             is_prime = False
#             break
#         i += 1
    
#     if is_prime:
#         print(n)
#     n += 1

######################################################################################################!

###* 18: Check whether the given number is prime number.

# n = int(input())

# if n <= 1:
#     is_prime = False
# else:
#     i = 2
#     is_prime = True

#     while i <= int(n**0.5):
#         if n % i == 0:
#             is_prime = False
#             break
#         i += 1
# if is_prime:
#     print("Yes")
# else:
#     print("No")

########################################################################################################!

###* 19: Print the fibonacci series up to n terms.

# n = int(input())

# a = 0
# b = 1
# count = 0

# while count < n:
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c
#     count += 1

########################################################################################################!

###* 20: find and print the sum of the fibonacci series up to n terms.

# n = int(input("enter a number: "))

# a = 0
# b = 1
# count = 0
# sum = 0

# while count < n:
#     sum += a
#     c = a + b
#     a = b
#     b = c
#     count += 1
# print(sum)

#########################################################################################################!

###* 21: Print the square of the each number from 1 to n.

# n = int(input("Enter a number: "))

# i = 1
# while i <= n:
#     print(i * i, end=" ")
#     i += 1


#########################################################################################################!

###* 22: Print the cube of each number from 1 to n.

# n = int(input("Enter a number: "))

# i = 1
# while i <= n:
#     print(i * i * i, end=" ")
#     i += 1

#########################################################################################################!

###* 23: Print the all number between a and b that are divisible by 7.

# n = int(input("Enter a number: "))

# i = 1
# while i <= n:
#     if i % 7 == 0:
#         print(i,end=" ")
#     i += 1

#########################################################################################################!

###* 24: Print all factors of given number.

# n = int(input("Enter a number: "))

# i = 1
# while i <= n:
#     if n % i == 0:
#         print(i, end=" ")
#     i += 1

#########################################################################################################!

###* 25: Find and print the sum of all factors of given number.

# n = int(input("Enter a number: "))

# i = 1
# sum = 0

# while i <= n:
#     if n % i == 0:
#         sum += i
#     i += 1

# print(sum)


#########################################################################################################!

###* 26: Find the HCF(Highest Common Number) of two given number.

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# small = min(a, b)
# i = 1
# hcf = 1 # Initialize hcf, If there is no hcf found.

# while i <= small:
#     if (a % i == 0 and b % i == 0):
#         hcf = i
#     i += 1
# print(f"HCF of {a} and {b} is: ",hcf)
    
#########################################################################################################!

###* 27: Find the LCM(Least Common Multiple) of given two numbers.

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# res = max(a, b)
# while(res <= a*b):
#     if (res % a == 0 and res % b == 0):
#         break
#     res += 1

# print(f"LCM of {a} and {b} is:",res)


#########################################################################################################!

###* 28: Find the smallest digit in given number.

# n = int(input("Enter a number: "))

# smallest = 9

# while n > 0:
#     digit = n % 10

#     if digit < smallest:
#         smallest = digit

#     n = n // 10

# print("Smallest digit is ",smallest)


#########################################################################################################!

###* 29: Find the largest digit in given number.

# n = int(input("Enter a number: "))

# largest = 0

# while n > 0:
#     digit = n % 10

#     if digit > largest:
#         largest = digit
    
#     n = n // 10

# print("Largest digit is:",largest)


#########################################################################################################!

#############################################!  END  #####################################################!