#2: Sum of Even Numbers.
# Calculate the sum of even numbers up to a given number n.

n = int(input("Enter a number: ")) # Get user input
#initialize sum variable
sum_even = 0
# Loop through numbers from 1 to n

for num in range(1, n+1):
    if num % 2 == 0: # check if number is even
        sum_even += num # Add the even number to sum_even

print("Sum of even number from 1 to", n, "is:", sum_even)