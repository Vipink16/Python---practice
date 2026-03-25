# check if given integer is positive even or odd, negative even or odd

n = int(input("Enter a num: "))

if n > 0:
    print("Positive", end=" ")
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
elif n < 0:
    print("Negative", end=" ")
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Number is zero")
