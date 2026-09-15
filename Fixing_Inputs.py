# JA, Fixing User Inputs

while True:
    colour = input("Tell me a colour that is only one word: ").strip().lower()
    if colour .isnumeric():
        print("That is a number not a colour.")
    elif " " in colour:
        print ("I said one word")
    else:
        break

print(f"We painted the walls {colour}!")