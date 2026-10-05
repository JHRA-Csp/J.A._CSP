# JA, Password Strength Checker Assignment

password = input("What is your password: ")

length = len(password) >= 8
upper = any(x.isupper() for x in password)
lower = any(x.islower() for x in password)
number = any(x.isdigit() for x in password)
symbol = any(x in "!@#$%^&*()_+-=[]{}|;':\",./<>?`~" for x in password)

print("At least 8 characters:", length)
print("Has uppercase:", upper)
print("Has lowercase:", lower)
print("Has a number:", number)
print("Has a symbol:", symbol)

total = 0

if length:
    total += 1
if upper:
    total += 1
if lower:
    total += 1
if number:
    total += 1
if symbol:
    total += 1

if total == 5:
    print("Your password strength is: Strong")
elif total >= 3:
    print("Your password strength is: Medium")
else:
    print("Your password strength is: Weak")

if total < 5:
    print("You are missing:")

    if not length:
        print(" 8 or more characters")
    if not upper:
        print(" an uppercase letter")
    if not lower:
        print(" a lowercase letter")
    if not number:
        print(" a number")
    if not symbol:
        print(" a symbol")