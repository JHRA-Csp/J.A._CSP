# JA. Loops Notes
import random

count = 1
 
while count <= 10:
    print (count)
    count += 1

ducks = 1
goose = random.randint(1,11)

while True:
    if ducks == goose:
        break
    print("Duck. . . .")
    ducks += 1
print("GOOSE!")

# complex data type = holds other data in it
siblings = ["Tyler","kenyan","Mykel"]
print(siblings[2])
siblings.append("Tyler, Mariana")
siblings.insert(3, "Jack")
print(siblings)
siblings.pop(3) #<- if no number the last number gets deleted
# 
for siblings in siblings:
    print (siblings)


# FOR Loops
for num in range(1,25):
    if num % 15 == 0:
       print("FizzBuzz")
    elif num % 3 == 0:
       print("Fizz")
    elif num % 5 == 0:
       print("Buzz")
    else:
       print(num)
