#!/usr/bin/python3
# -*- coding: utf-8 -*-

# =============================================================================
#
#        FILE:  operations.py
#      AUTHOR:  Tan Duc Mai <henryfromvietnam@gmail.com>
#     CREATED:  2021-07-15
# DESCRIPTION:  Determines the operation of the game,
#               effectively the CPU of the game.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#
# =============================================================================

# ------------------------------- Module Import -------------------------------
import random


# ---------------------------- Function Definitions ---------------------------
def guessing(guess_range, guess_limit):
    # Set the initial values.
    attempts_allowed = guess_limit
    rnd = random.randint(1, guess_range)
    guess = int(input('What is your guess? '))
    done = False

    # Validate the inputted guess.
    guess = validate_input(guess, guess_range)

    # Now we have a valid guess.
    while guess_limit > 0 and not done:
        guess_limit -= 1                     # Take one guess = lose one chance
        if guess_limit > 0:
            if guess < rnd:
                print(f'It should be higher than {guess}.')
            elif guess > rnd:
                print(f'It should be lower than {guess}.')
            else:
                attempts_taken = attempts_allowed - guess_limit
                print('You nailed it! And it only took you',
                      attempts_taken, 'attempts.')
                done = True
            if guess_limit > 0 and not done:
                print(f'You still have {guess_limit} chances left.\n')
                guess = int(input('Try a new guess: '))
                # Another input validation loop.
                guess = validate_input(guess, guess_range)
        elif guess_limit == 0 and not done:   # Last chance to guess
            if guess == rnd:
                print('You nailed it! However, it took you all the',
                      attempts_allowed, 'attempts.')
            else:
                print('GAME OVER! It took you more than',
                      attempts_allowed, 'attempts.',
                      'The correct number is', str(rnd) + '.')


def validate_input(guess, guess_range):
    while not 1 <= guess <= guess_range:
        print('ERROR! Your guess is out of range!\n')
        guess = int(input('Try Again. What is your guess? '))
    return guess
