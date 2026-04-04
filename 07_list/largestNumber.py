# Find the second largest number.

# def secondLargest(arr):
#     unique = list(set(arr))
#     unique.sort()
#     return arr[-2]

# arr = [10, 20, 4, 45, 99]
# print(secondLargest(arr))


def secondLargest(arr):
    first = second = float('-inf') # -inf = for very small number,ensure number in list will be larger.

    for x in arr:
        if x > first:
            second = first
            first = x
        elif x > second and x != first:
            second = x
    return second
arr = [10, 20, 4, 45, 99]
print(secondLargest(arr))