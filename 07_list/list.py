l = [10, 20, 30, 40, 50]

# # to add new value in list at last index
# l.append(30)
print(l)

# to insert a new item in list at a specific index l.insert(index, item)
# l.insert(1, 15)
# print(l)

# print(15 in l) # to check if item is present in list or not

# print(l.count(30)) # to check number of occurrence  of item.

# print(l.index(30)) #to check index number,only for first occurrence

# print(l.index(30,4,7)) #

# # remove item from the list, but if that item is not present in list the it will raise valueerror
# l.remove(20)
# print(l)

# print(l.pop()) # removes the last item from the list, print only popped item.
# print(l)

# print(l.pop(2)) # remove the item from list given index.
# print(l)

# del l[1] # deletes the item from index 1.
# print(l)

# del l[0:2] # deletes the items from index 0 to 1.
# print(l)

# print(max(l)) # gives the maximum item from the list.

# print(min(l)) # gives the minimum item from the list.

# print(sum(l)) # gives the sum of all items of list.

# l.reverse() # reverse all the items of the list.
# print(l)

# l.sort() # sort all items in increasing order.
# print(l)

#! Python List Slicing

# Python list slicing is fundamental concept that let us easily access specific elements in a list.

# list_name[start : stop : step]

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Get elements from index 1 to 4 (excluded)
# print(a[1:4])