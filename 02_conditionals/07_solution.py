# 7. Coffee Customization.
# Customize a coffee order: "Small","Medium",or "Large" with an option for "Extra Shot" of espresso.

order_size = input("Enter your coffee size: ").strip().lower()
extra_shot = True

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"

print(coffee)