# Password Strength Checker.
# Check if a password is "weak", "Medium", or "Strong".Criteria: <6 chars(Weak), 6-10 chars(Medium), >10 chars(Strong).

password = input("Enter your password: ").strip()

if len(password) <6 :
    strength = "Weak"
elif len(password) <=10:
    strength = "Medium"
else:
    strength = "Strong"

print("Your password strength is:",strength)
exit()