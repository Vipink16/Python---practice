# 9: List Uniqueness Checker.
# Check if all elements in list are unique.If duplicate is found, exit the loop and print the duplicate.

items = ["apple", "Banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate: ", item)
        break
    unique_item.add(item)