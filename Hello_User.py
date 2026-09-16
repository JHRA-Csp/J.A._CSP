# JA, Hello User Activity

while True:
    name = input("Tell me your name: ").strip().capitalize()
    if name .isnumeric():
        print("That is a number, not a name!")
    else:
        break

print(f"Hello {name}!")