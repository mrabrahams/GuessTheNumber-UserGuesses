# # learning how use the random library for a guessing game with the user guessing the computers selection.

import random

def guess (x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low!")
        elif guess > random_number:
            print("Sorry, guess again. Too high!")

    print(f"Yay, congratulations you have guessed the random number {random_number} correctly!")

guess(100)
