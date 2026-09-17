# JA, Your Budget Code

while True:
    try:
        income=float(input("What is your monthly icome: "))
        break
    except:
        print("Please write your actually monthly income: ")


while True:
     try:
        rent=float(input("What is your monthly Rent/Morgage: "))
        break
     except:
         print("Please write your actually monthly Rent: ")

while True:
     try:
        Utilities=float(input("What is your monthly utilities price: "))
        break
     except:
         print("Please write your actually monthly utilities price: ")

while True:
     try:
        Groceries=float(input("What is your monthly groceries price: "))
        break
     except:
         print("Please write your actually monthly groceries price: ")

while True:
     try:
        transportation=float(input("What is your monthly transportation price: "))
        break
     except:
         print("Please write your actually monthly transportation price: ")


print(f"Your monthly Rent/Morgage is ${rent:.2f}and the percentage of your income is {int(rent/income*100)}%")
print(f"Your monthly utilities price is ${Utilities:.2f}and the percentage of your income is {int(Utilities/income*100)}%")
print(f"Your monthly groceries price is ${Groceries:.2f}and the percentage of your income is {int(Groceries/income*100)}%")
print(f"Your monthly transportation price is ${transportation:.2f} and the percentage of your income is {int(transportation/income*100)}%")
