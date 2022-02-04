#!/usr/bin/python3

#
# File:         game_body.py
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
def guessing(GUESS_RANGE, GUESS_LIMIT):
    # Set the initial values.
    RANDOM = random.randint(1, GUESS_RANGE)
    GUESS = int(input('What is your guess? '))
    ATTEMPTS_ALLOWED = GUESS_LIMIT
    done = False

    # Validate the inputted guess.
    GUESS = InputValidation(GUESS, GUESS_RANGE)

    # Now we have a valid guess.
    while GUESS_LIMIT > 0 and not done:
        GUESS_LIMIT -= 1                     # Take one guess = lose one chance
        if GUESS_LIMIT > 0:
            if GUESS < RANDOM:
                print(f'It should be higher than {GUESS}.')
            elif GUESS > RANDOM:
                print(f'It should be lower than {GUESS}.')
            else:
                ATTEMPTS_TOOK = ATTEMPTS_ALLOWED - GUESS_LIMIT
                print(f'You nailed it! And it only took you {ATTEMPTS_TOOK} attempts.')
                done = True
            if GUESS_LIMIT > 0 and not done:
                print(f'You still have {GUESS_LIMIT} chances left.\n')
                GUESS = int(input('Try a new guess: '))
                # Another input validation loop.
                GUESS = InputValidation(GUESS, GUESS_RANGE)
        elif GUESS_LIMIT == 0 and not done:                 # Last chance to guess
            if GUESS == RANDOM:
                print(f'You nailed it! However, it took you all the {ATTEMPTS_ALLOWED} attempts.')
            else:
                print(
                    f'GAME OVER! It took you more than {ATTEMPTS_ALLOWED} attempts. '
                    f'The correct number is {RANDOM}.'
                )


def InputValidation(GUESS, GUESS_RANGE):
    while not 1 <= GUESS <= GUESS_RANGE:
        print('TRY AGAIN! Your guess is out of range!\n')
        GUESS = int(input('What is your guess? '))
    return GUESS
