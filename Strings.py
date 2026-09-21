# JA, Strings

name = input("What is your name: ").strip().capitalize()

print(name)

#
sentance = "The quick brown fox jumped over the lazy dog"

print(sentance)
print(sentance.replace("dog", "cat"))
print(len(name)) #<= gets the length of a string
print(f"Your name is {name} that is {len(name)} letters long. Your first initial is {name[0]} I think i will call you {name[0:3]}")

