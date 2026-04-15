# Move all negatives to one side.

def moveNeg(l):
    neg = []
    pos = []
    for x in l:
        if x < 0:
            neg.append(x)
        else:
            pos.append(x)
    return neg + pos
            

l = [1, -2, 3, -4, 5]
print(moveNeg(l))