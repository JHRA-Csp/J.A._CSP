# JA - Number Guessing Game

import random

secret_num = random.randint(1, 100)

max_tries = 6
guesses_used = 0

print("I'm thinking of a number between 1 and 100. You have 6 tries to guess it!")

while guesses_used < max_tries:
    guesses_used = guesses_used + 1
    
    guess_input = input(f"Guess #{guesses_used}: ")
    player_guess = int(guess_input)
    
    if player_guess < secret_num:
        print("Too low!")
    elif player_guess > secret_num:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {guesses_used} tries!")
        break

if player_guess != secret_num:
    print(f"You're out of guesses! The number was {secret_num}.")