# JA, CSP hangman activty

import random
with open("./HangMan/HMlist.txt","r+") as file:
    #print(file.read())
    txt = file.read()

x = txt.splitlines()
print(type(x))
randindex = random.choice(x)
secret_word = randindex.strip().capitalize()
print(secret_word)

print("Insructions: First you guess a letter if that letter is in the secret word, if not the 'man' will start to get hung, you get six guesses. ")
Guess1
Guess1 = input("What is your first guess: ").strip().upper()

if len(Guess1) != 1 or not Guess1.isalpha():
    print("Please enter a single valid letter.")
    Guess1 = input("Please guess a valid letter: ").strip().upper()

guessed_letters = []
guessed_letters.append(Guess1)

display_word = []
for letter in secret_word:
    if letter in guessed_letters:
      display_word.append(letter)
    else:
      display_word.append("_")

print("\nWord:", " ".join(display_word))

if Guess1 in secret_word:
  print(f"Nice! {Guess1} is in the word.")
else:
  print(f"Sorry, {Guess1} is not in the word.")

#Guess2
Guess2 = input("What is your 2nd guess: ").strip().upper()

if len(Guess2) != 1 or not Guess2.isalpha():
  print("Please enter a single valid letter.")
  Guess2 = input("Please guess a valid letter: ").strip().capitalize()

if Guess2 in guessed_letters:
  print(f"You already guessed '{Guess2}'.")
else:

  guessed_letters.append(Guess2)

  if Guess2 in secret_word:
    print(f"Nice! {Guess2} is in the word.")
  else:
    print(f"Sorry, {Guess2} is not in the word.")

display_word = []
for letter in secret_word:
  if letter in guessed_letters:
    display_word.append(letter)
  else:
    display_word.append("_")

#Guess3
print("\nWord:", " ".join(display_word))
print("Guessed letters:", ", ".join(sorted(guessed_letters)))

Guess3 = input("What is your 3rd guess: ").strip().upper()

if len(Guess3) != 1 or not Guess3.isalpha():
  print("Please enter a single valid letter.")
  Guess3 = input("Please guess a valid letter: ").strip().upper()

if Guess3 in guessed_letters:
  print(f"You already guessed '{Guess3}'!")
else:
  guessed_letters.append(Guess3)

  if Guess3 in secret_word:
    print(f"Nice! {Guess3} is in the word.")
  else:
    print(f"Sorry, {Guess3} is not in the word.")

display_word = []
for letter in secret_word:
  if letter in guessed_letters:
    display_word.append(letter)
  else:
    display_word.append("_")

print("\nWord:", " ".join(display_word))
print("Guessed letters:", ", ".join(sorted(guessed_letters)))

#Guess4
Guess4 = input("What is your 4th guess: ").strip().upper()

if len(Guess4) != 1 or not Guess4.isalpha():
  print("Please enter a single valid letter.")
  Guess4 = input("Please guess a valid letter: ").strip().upper()

if Guess4 in guessed_letters:
  print(f"You already guessed '{Guess4}'!")
else:
  guessed_letters.append(Guess4)

  if Guess4 in secret_word:
    print(f"Nice! {Guess4} is in the word.")
  else:
    print(f"Sorry, {Guess4} is not in the word.")

display_word = []
for letter in secret_word:
  if letter in guessed_letters:
    display_word.append(letter)
  else:
    display_word.append("_")

print("\nWord:", " ".join(display_word))
print("Guessed letters:", ", ".join(sorted(guessed_letters)))

#guess5
Guess5 = input("What is your 5th guess: ").strip().upper()

if len(Guess5) != 1 or not Guess5.isalpha():
  print("Please enter a single valid letter.")
  Guess5 = input("Please guess a valid letter: ").strip().upper()

if Guess5 in guessed_letters:
  print(f"You already guessed '{Guess5}'!")
else:
  guessed_letters.append(Guess5)

  if Guess5 in secret_word:
    print(f"Nice! {Guess5} is in the word.")
  else:
    print(f"Sorry, {Guess5} is not in the word.")

display_word = []
for letter in secret_word:
  if letter in guessed_letters:
    display_word.append(letter)
  else:
    display_word.append("_")

print("\nWord:", " ".join(display_word))
print("Guessed letters:", ", ".join(sorted(guessed_letters)))

#Guess6
Guess6 = input("What is your final guess: ").strip().upper()

if len(Guess6) != 1 or not Guess6.isalpha():
  print("Please enter a single valid letter.")
  Guess6 = input("Please guess a valid letter: ").strip().upper()

if Guess6 in guessed_letters:
  print(f"You already guessed '{Guess6}'!")
else:
  guessed_letters.append(Guess6)

  if Guess6 in secret_word:
    print(f"Nice! {Guess6} is in the word.")
  else:
    print(f"Sorry, {Guess6} is not in the word.")

display_word = []
for letter in secret_word:
  if letter in guessed_letters:
    display_word.append(letter)
  else:
    display_word.append("_")

print("\nWord:", " ".join(display_word))
print("Guessed letters:", ", ".join(sorted(guessed_letters)))

if "_" not in display_word:
  print(f"\nCongratulations! You guessed the word: {secret_word}")
else:
  print(f"\nGame Over! You ran out of guesses. The secret word was: {secret_word}")

# insrtuctions
# stats
# keep track of guessed letters
# Win Loss outputs
# update stats
# display letters guessed in a list
# integer that needs