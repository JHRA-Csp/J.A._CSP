# Ja, Integers, Floats, and Expressions Notes

# Integer
students = 23
cars = 50
computers = 29
awareness = -12

# Float => numbers with decimals.
pi = 3.1415
temp = -95.7
cost = 1.99
rain = 2.17

#Arithmitic Operators (+ - * / // ** %)
print(f"18/4 is {18/4} or {18//4}The remainder of {18%4}")
print(f"18/5 is {18/5} or {18//5}The remainder of {18%5}")

# order of operations
Grades = [85,66,94,72,88,79,100]
Students = len(Grades)
Average = sum(Grades)/Students

print(f"the Average is {int(Average)}")

# convert the data type
price = float(input("How much did the item cost: "))
tax = 0.0485
sales_tax = price * tax
total = price + sales_tax
print(f"Your total is {total}.")