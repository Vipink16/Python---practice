
#* Pattern searching.

# txt = input("Enter a text: ")
# pat = input("Enter the text which you want to search: ")

# pos = txt.find(pat)
# while pos >= 0:
#     print(pos)
#     pos = txt.find(pat, pos+1)

#!#########################################################################################################


#* Reverse a string in python

# s = input("Enter a string: ")

# rev = ""
# for i in s:
#     rev = i + rev
# print(rev)

##################  OR ####################

# s = input("Enter a string: ")
# print(s[::-1])

#!##########################################################################################################

#* Check for palindrome in python.

# s = input("Enter a string: ")

# low = 0
# high = len(s) - 1

# while low < high:
#     if s[low] != s[high]:
#         print("No")
#         break
#     low += 1
#     high -= 1
# else:
#     print("Yes")

#*##############  OR  ##################
# Using slicing 

# s = input("Enter a string: ")

# if s == s[::-1]:
#     print("Yes")
# else:
#     print("No")

#!#########################################################################################################

#* Decimal to binary 

# def decToBinary(n):
#     if n == 0:
#         return "0"
    
#     res = ""
#     while n > 0:
#         res = res + str(n % 2)
#         n = n // 2
    
#     return res[::-1]


# # take input from user
# num = int(input("Enter a decimal number: "))

# # call function
# binary = decToBinary(num)

# # print result
# print("Binary equivalent is:", binary)

### Using built-in function - bin()

# n = 8
# print(bin(n).replace("0b", ""))
# n = 18
# print(bin(n).replace("0b", ""))

# bin(n) converts a decimal number to a binary string, but the result has a prefix "0b" (e.g., 0b1000).
# replace("0b", "") removes the "0b" prefix by replacing it with an empty string, giving a clean binary representation.


#!#########################################################################################################

#* Binary to Decimal

# def binToDec(b):
#     res = 0
#     p = 1
#     for x in reversed(b):
#         res = res + int(x) * p
#         p = p * 2
#     return res

# num = input("Enter binary number:")
# decimal = binToDec(num)
# print("Decimal number is:",decimal)


# Using built-in function int()

# for b in ['100', '101']:
#     print(int(b, 2))