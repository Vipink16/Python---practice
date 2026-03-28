# 7: Validate Input.
# Keep asking the user for input until they enter a number between 1 and 10.

while True:
    number = int(input("Enter a number b/w 1 and 10: "))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Failed!,Please enter a valid number")