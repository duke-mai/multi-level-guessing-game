#!/usr/bin/python3

#
# File:         options.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         15-Jul-2021
# Description:  Determines game modes and the 'try_again' option.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#


# ------------------------------- Module Imports ------------------------------
"""
The first module contains the main part of the game, which is processing
the guess and validate user input.
The second module is the introduction to the game, where the user is asked
to choose a mode to play.
"""
from game_body import guessing as game
import welcome


# ---------------------------- Function Definitions ---------------------------
def easy():
    print('You are to guess a number between 1 and 10 in no more than 6 attempts.')
    game(10, 6)


def medium():
    print('You are to guess a number between 1 and 20 in no more than 4 attempts.')
    game(20, 4)


def hard():
    print('You are to guess a number between 1 and 50 in no more than 3 attempts.')
    game(50, 3)


def try_again():
    print()
    again = input('Do you want to play again? [Y/n] ')
    print()
    if again.lower() in ['y', 'yes']:
        welcome.start_game()
    elif again.lower() in ['n', 'no']:
        print('Thanks for playing the game!')
    else:
        print('INVALID VALUE!')
        try_again()
