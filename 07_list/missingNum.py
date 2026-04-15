# Numbers from 1 to n are given, one is missing.

# def missingNum(arr):
#     n = len(arr) + 1

#     for i in range(1, n + 1):
#         if i not in arr:
#             return i

# l = [1, 2, 4, 5]
# print(missingNum(l))

#! Using AP formula

def missingNumber(l):
    n = len(l) + 1

    total = n * (n + 1) // 2
    actual = sum(l)

    return total - actual
l = [1, 2, 4, 5]
print(missingNumber(l))