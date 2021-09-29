#
# File:         welcome.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         15/7/2021
# Description:  Introduce the user to the game, asking them to choose level.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#

"""
This module contains the user choice of easy, medium, and hard mode.
It also asks whether the user want to play the game again.
"""

import game_options as option


def start_the_game():
    print(
        'Welcome to the game "Guess My Number"!',
        'Choose a level:',
        '1. Easy',
        '2. Medium',
        '3. Hard',
        sep = '\n',
    )

    level = int(input('Pick a number: '))

    if level == 1:
        option.easy()
        option.try_again()
    elif level == 2:
        option.medium()
        option.try_again()
    elif level == 3:
        option.hard()
        option.try_again()
    else:
        print('INVALID VALUE!\n')
        welcome()
