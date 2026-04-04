##! Check if a list is sorted or not.

# def isSorted(l):
#     i = 1
#     while i < len(l):
#         if l[i] < l[i-1]:
#             return False
#         i += 1
#     return True

# l = [10, 20, 30]
# if isSorted(l):
#     print("Yes")
# else:
#     print("No")

# #! Using for Loop

# a = [1, 2, 3, 4]
# res = True

# for i in range(len(a) - 1):
#     if a[i] > a[i + 1]:
#         res = False
#         break

# print(res)

# #! Using sorted()

# def isSorted(l):
#     sl = sorted(l)
#     if sl == l:
#         return True
#     else:
#         return False

# l = [10, 20, 5, 30]
# if isSorted(l):
#     print("Yes")
# else:
#     print("No")