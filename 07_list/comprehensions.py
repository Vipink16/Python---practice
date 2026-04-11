
##! Using comprehensions in python

# l = [1,2,3,4,5,6,7,8,9]

# l1 = [x for x in range(10) if x % 2 == 0]
# print(l1)

# l2 = [x for x in range(10) if x % 2 != 0]
# print(l2)

##* function to get list that contains all those items  of l that are smaller than x.

# def getSmaller(l, x):
#     return [e for e in l if e < x]
# l = [9, 15, 12, 3, 7, 11]
# x = 10
# print(getSmaller(l, x))

# #! Using List Comprehensions

# def getEvenOdd(l):
#     even = [e for e in l if e % 2 == 0]
#     odd = [e for e in l if e % 2 != 0]
#     return even, odd

# l = [1,2,3,4,5,6,7,8,9]
# even, odd = getEvenOdd(l)
# print(even)
# print(odd)

##! Set comprehensions

# l = [10,20,3,4,10,20,7,3]

# s1 = {x for x in l if x % 2 == 0}
# s2 = {x for x in l if x % 2 != 0}

# print(s1)
# print(s2)

##! Dictionary Comprehensions

# l1 = [1, 3, 5, 2, 4]
# d1 = {x:x ** 3 for x in l1}
# print(d1)

# d2 = {x:f"ID{x}" for x in range(5)} # assign a id to each item
# print(d2)

# l2 = [101, 102, 103]
# l3 = ["Apple", "Orange", "Grapes"]

# d3 = {l2[i]:l3[i] for i in range(len(l2))}
# print(d3)

# # Better way
# d3 = dict(zip(l2, l3))
# print(d3)

##* Inverting a dictionary(key becomes value and value becomes key)

# d1 = {101:"Apple", 102:"Orange", 103:"Grapes"}
# d2 = {v:k for (k,v) in d1.items()}
# print(d2)