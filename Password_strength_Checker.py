# JA, Pass word strenght checker

Password = input("What do you want your password to be: ")
Characters = False
Uppercase = False
Lowercase = False
Number = False
Symbol = False

len(Password)

if len(Password) < 8:
    print("You should add more characters for a stronger password")
    print("FAILED")
if len(Password) >= 8:
    print("Your password is a good length")
    Characters = True

if Password.islower():
    print("You should add more uppercase characters for an even stronger password")
    print("FAILED, resart program to try again")
if Password.isupper():
    print("Your password has enough capitals")
    Uppercase = True