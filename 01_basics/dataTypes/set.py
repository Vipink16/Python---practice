'''
Let's implement some methods through a question. The task is to perform given queries in the Set as given below:
a. i element: Add element i to the set.
b. r element: Remove element r from set.
c. s: Find sum of elements in set.


Docstring for 01_basics.dataTypes.set
Input: st = [6, 7, 81, 2, 1], i = 3, r = 6
Output: 
1 2 3 6 7 81
1 2 3 7 81 
94
Explanation: After adding 3 set becomes [1, 2, 3, 6, 7, 81], after removing 6 set becomes [1, 2, 3, 7, 81]  and sum of set is 94.
'''



#User function Template for python3
st = {int(x) for x in input().split()}
i = int(input())
r = int(input())

########### Write your code below ###############
# Insert i in set
st.add(i)
print(st)
########### Write your code above ###############

# Printing the set
# for i in sorted(st):
#     print (i, end=' ')
# print()

########### Write your code below ###############
# Remove r from set

########### Write your code above ###############

# Printing the set
# for i in sorted(st):
#     print (i, end=' ')
# print()

########### Write your code below ###############
sum = # Sum of set elements
########### Write your code above ###############

# Print sum of set
# print(sum)