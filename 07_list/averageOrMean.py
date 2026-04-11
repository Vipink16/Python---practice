
#! Average or Mean of a List

# def average(l):
#     sum = 0
#     for x in l:
#         sum = sum + x
#     n = len(l)
#     return sum / n

# l = [10, 20, 30, 40]
# print(average(l))

####*  OR    ####

def mean(l1):
    return sum(l1)/len(l1)

l1 = [10, 20, 30, 40, 50]
print(mean(l1))