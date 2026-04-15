# You are given a tuple numbers that contains integers. You need to return a tuple containing doubles of given numbers.
"""
Input: tup = (4, 5, 1, 2, 3, 5)
Output: 8 10 2 4 6 10
Explanation: multiplied numbers by 2.
"""

def doubleTup(numbers):
    res = []
    for x in numbers:
        res.append(x * 2)
    return tuple(res)
numbers = (4, 5, 6, 7, 8)
res = doubleTup(numbers)
print(res)

### OR ###
    # return tuple(x * 2 for in x numbers)
