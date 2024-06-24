"""
File: hangman.py
Name: Catherine Tsai
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program plays the Hangman game. Players will need to guess the correct word by inputting
    a letter (case-insensitive) at once, given 7 guess chances.
    """
    word = random_word()
    print('The word looks like this: ' + '-'*(len(word)))
    print('You have ' + str(N_TURNS) + ' wrong guesses left.')
    guess_left = N_TURNS
    correct_letters = ''

    while guess_left > 0:
        your_guess = str(input('Your guess: ')).upper()
        if your_guess in word:
            print('You are correct!')
            print('The word looks like: ')
            if correct_letters == word:
                print('You are correct!')
                print('You win!!')
                print('The answer is: ' + word)
                return
        else:
            guess_left = guess_left - 1
            if guess_left == 0:
                print('There is no ' + your_guess + ' in the word.')
                print('You are completely hung :(')
                print('The answer is: ' + word)
                return
            print('There is no ' + your_guess + ' in the word.')
            print('You have ' + str(guess_left) + ' wrong guesses left.')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
