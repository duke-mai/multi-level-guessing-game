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
The game_options module contains the user choice of easy, medium, and hard mode.
It also asks whether the user want to play the game again.
The time.sleep() function gives break between each set of message.
"""

import game_options as option
from time import sleep


def start_the_game():
    print('Hello, Welcome to the Number Guessing Game!')
    name = input('I\'m Henry! What\'s Your Name? ')
    sleep(1)
    
    print(f'Okay, {name}. Let\'s Begin The Guessing Game!')
    print('Choose a level:',
          '1. Easy',
          '2. Medium',
          '3. Hard',
          sep = '\n',
    )
    sleep(1)
    level = int(input('Pick a number: '))
    print()
    sleep(1)
    
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
        print('INVALID VALUE! Please try again.\n')
        start_the_game()
