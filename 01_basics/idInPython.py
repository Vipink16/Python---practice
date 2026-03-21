
# print(id(5))
# a = 10

# print(id(a))
# b = a

# print(id(b))


# x = 4
# print(id(x))
# print(id((int)(x + "GFG")))

# list1 = [10, 20, 30]
# list2 = [30, 10, 20]

# print("list1 + list 2 = : ", list1 + list2)
# print("list1 * 2 = : ", list1 * 2) # same list1 appears 2 times


###############  Set  ######################
#Python set is an unordered collection of multiple items having different datatypes. In Python, sets are mutable, unindexed and do not contain duplicates. The order of elements in a set is not preserved and can change.

# 1- Can store None values.
# 2- Implemented using hash tables internally.
# 3- Do not implement interfaces like Serializable or Cloneable.
# 4- Python sets are not inherently thread-safe; synchronization is needed if used across threads.

# Creating a set
# set1 = {1, 2, 3}

# # Add one item
# set1.add(4)

# # Add multiple items
# set1.update([5, 6])

# print(set1)

##############

# Using Remove Method
# set1 = {1, 2, 3, 4, 5}
# set1.remove(3)
# print(set1)  

# # Attempting to remove an element that does not exist
# try:
#     set1.remove(10)
# except KeyError as e:
#     print("Error:", e)  

# # Using discard() Method
# set1.discard(4)
# print(set1)

# Attempting to discard an element that does not exist
# set1.discard(10)  # No error raised
# print(set1)

'''
s = {10, 20, 30, 40}
s.discard(50)
# s.remove(40)
print(s)
'''

######### using pop() method

# pop() method removes and returns an arbitrary element from the set. This means we don't know which element will be removed. If the set is empty, it raises a KeyError.

# set1 = {1, 2, 3, 4, 5}
# val = set1.pop()
# print(val)
# print(set1)

# Using pop on an empty set
# set1.clear()  # Clear the set to make it empty
# try:
#     set1.pop()
# except KeyError as e:
#     print("Error:", e)

# s1 = {1, 2, 3, 4, 5, 6}
# s2 = {6, 7, 8, 9}
# print(s1 | s2) # it gives the union of s1 and s2
# OR
# s3 = s1.union(s2)
# print(s3)

#### it gives the intersection of s1 and s2
# print(s1 & s2) 
# OR
# s3 = s1.intersection(s2)
# print(s3)

##### to gives the difference two sets, will remove the element of s2 which presents in s1.
# print(s1 - s2)
# OR
# s3 = s1.difference(s2)
# print(s3)


##### Symmetric difference operator
# it gives the elements which presents in both sets but not the common element(intersection)
# s3 = s1.symmetric_difference(s2)
# print(s3)

#### isdisjoint operator
# This operation gives you boolean value, it gives you true if there is no common element among the two sets.

# set1 = {2, 4, 6, 8}
# set2 = {4, 8}
# print(set1.isdisjoint(set2))


#### is subset or not

# s3 = s1.issubset(s2)
# print(s3) 
# OR
# print(s1 <= s2)
# print(s1 < s2)
# # is superset or not
# s3 = s1.issuperset(s2)
# print(s3)
# print(s1 >= s2)
# print(s1 > s2)

### Accessing a set in python

# set1 = set(["Geeks", "For", "Geeks."])

# # Accessing element using For loop
# for i in set1:
#     print(i, end=" ")

# # Checking the element# using in keyword
# print("Geeks" in set1)

# a = {1,2,3}
# b = {4,5,6}
# print(len(a + b))

# a = 10
# print(str(a)) # explicit conversion
