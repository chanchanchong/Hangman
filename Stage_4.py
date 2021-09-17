# Stage 4/8: Help is on the way

# Description
# Now our game has become quite hard, and your
# chances of guessing the word depend on the size
# of the list. When the list has four words, you only
# have a 25% chance to guess correctly. So let's show
# a little mercy to the player and add a hint for them.

# Objectives
# 1. As in the previous stage, you should use the
#    following word list: 'python', 'java',
#    'kotlin', 'javascript'
# 2. Once the computer has chosen a word from
#    the list, show its first 3 letters. Hidden letters
#    should be replaced with hyphens("-").

# Examples
# The greater-than symbol followed by a space ( > )
# represents the user input. Note that it's not part of
# the output.

# Example 1
# H A N G M A N
# Guess the word jav-: > java
# You survived!

# H A N G M A N
# Guess the word pyt---: > pythia
# You lost!

import random

class Hangman:
    def __init__(self):
        self.words = ['python', 'java', 'kotlin', 'javascript']

    def title(self):
        print("H A N G M A N")

    def play(self):
        guess = random.choice(self.words)
        answer = input("Guess the word " + guess[:3] + '-' * (len(guess) - 3) + ": ")
        print("You survived!" if answer == guess else "You lost!")


def main():
    game = Hangman()
    game.title()
    game.play()


if __name__ == '__main__':
    main()
