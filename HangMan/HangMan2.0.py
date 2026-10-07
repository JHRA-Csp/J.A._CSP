# JA HangMan project

import random

wins = 0
losses = 0

try:
  with open("./HangMan/Stats.txt", "r") as file:
    lines = file.readlines()
    if len(lines) >= 2:
      wins = int(lines[0].strip())
      losses = int(lines[1].strip())
except FileNotFoundError:
  wins = 0
  losses = 0

print(f"Loaded Stats -> Wins: {wins}, Losses: {losses}")

with open("./HangMan/HMlist.txt", "r") as file:
  txt = file.read()

x = txt.splitlines()

print("Instructions: First you guess a letter. If that letter is in the secret word, you get closer to winning. If not, the 'man' will start to get hung. You get six guesses.")

while True:
  randindex = random.choice(x)
  secret_word = randindex.strip().upper()

  # Reset round variables
  guessed_letters = []
  guesses_left = 6

  while guesses_left > 0:
    display_word = []

    for letter in secret_word:
      if letter in guessed_letters:
        display_word.append(letter)
      else:
        display_word.append("_")

    print("\nWord:", " ".join(display_word))
    print("Guessed letters:", ", ".join(sorted(guessed_letters)))
    print("Guesses left:", guesses_left)

    guess = input("Guess a letter: ").strip().upper()

    if len(guess) != 1 or not guess.isalpha():
      print("Please enter a single valid letter.")
      continue

    if guess in guessed_letters:
      print(f"You already guessed '{guess}'!")
      continue

    guessed_letters.append(guess)

    if guess in secret_word:
      print(f"Nice! {guess} is in the word.")
    else:
      print(f"Sorry, {guess} is not in the word.")
      guesses_left -= 1

    display_word = []
    for letter in secret_word:
      if letter in guessed_letters:
        display_word.append(letter)
      else:
        display_word.append("_")

    if "_" not in display_word:
      print("\nWord:", " ".join(display_word))
      print(f"\nCongratulations! You guessed the word: {secret_word}")
      wins += 1
      break

  else:
    print(f"\nGame Over! The secret word was: {secret_word}")
    losses += 1

  with open("./HangMan/Stats.txt", "w") as file:
    file.write(f"{wins}\n{losses}\n")

  print(f"Updated Stats — Wins: {wins}, Losses: {losses}")

  play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
  if play_again != "y":
    print("Thanks for playing!")
    break