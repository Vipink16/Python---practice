# 3: Multiplication Table Printer.
# Print the multiplication table for a given number up to 10, but skip fifth iteration.

num = int(input("Enter the number: "))

for i in range(1, 11):
    if i == 5: # to skip the fifth iteration
        continue # keyword used to skip
        print(num, 'x', i, '=', num * i)