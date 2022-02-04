#!/usr/bin/python3

#
# File:         operations.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         15-Jul-2021
# Description:  Determines the operation of the game,
#               effectively the CPU of the game.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#

# ------------------------------- Module Import -------------------------------
import random


# ---------------------------- Function Definitions ---------------------------
def guessing(GUESS_RANGE, guess_limit):
    # Set the initial values.
    ATTEMPTS_ALLOWED = guess_limit
    rnd = random.randint(1, GUESS_RANGE)
    guess = int(input('What is your guess? '))
    done = False

    # Validate the inputted guess.
    guess = validate_input(guess, GUESS_RANGE)

    # Now we have a valid guess.
    while guess_limit > 0 and not done:
        guess_limit -= 1                     # Take one guess = lose one chance
        if guess_limit > 0:
            if guess < rnd:
                print(f'It should be higher than {guess}.')
            elif guess > rnd:
                print(f'It should be lower than {guess}.')
            else:
                attempts_taken = ATTEMPTS_ALLOWED - guess_limit
                print(f'You nailed it! And it only took you {attempts_taken} attempts.')
                done = True
            if guess_limit > 0 and not done:
                print(f'You still have {guess_limit} chances left.\n')
                guess = int(input('Try a new guess: '))
                # Another input validation loop.
                guess = validate_input(guess, GUESS_RANGE)
        elif guess_limit == 0 and not done:                 # Last chance to guess
            if guess == rnd:
                print(f'You nailed it! However, it took you all the {ATTEMPTS_ALLOWED} attempts.')
            else:
                print(
                    f'GAME OVER! It took you more than {ATTEMPTS_ALLOWED} attempts. '
                    f'The correct number is {rnd}.'
                )


def validate_input(guess, GUESS_RANGE):
    while not 1 <= guess <= GUESS_RANGE:
        print('ERROR! Your guess is out of range!\n')
        guess = int(input('Try Again. What is your guess? '))
    return guess
