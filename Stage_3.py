# Stage 3/8: Make your choice

# Description
# If there is a predefined word, the game isn't replayable.
# You already know the word, so there's no longer any
# challenge. At this stage, let's make the game more
# challenging by choosing a word from a special list with a
# variety of options. This way, our game will have more
# replay value.

# Objectives
# 1. Create the following list of words: 'python',
#    'java', 'kotlin', 'javascript'.
# 2. Program the game to choose a word from the list
#    at random. You can enter more words, but let's
#    stick to these four for now.

# Examples
# The greater-than symbol followed by a space ( > )
# represents the user input. Note that its' not part of the
# output.

# Example 1. The computer randomly chose python from
# the list.

# H A N G M A N
# Guess the word: > python
# You survived!

# Example 2: The computer randomly chose something
# other than python from the list.

# H A N G M A N
# Guess the word: > python
# You lost!

# Example 3: The computer randomly chose something
# other than kotlin from the list.

# H A N G M A N
# Guess the word: > kotlin
# You lost!

from random import choice


class Hangman:
    def __init__(self):
        self.words = ['python', 'java', 'kotlin', 'javascript']
        self.guess = choice(self.words)
        self.welcome_message = " H A N G M A N"
        self.winning_message = "You survived!"
        self.losing_message = "You lost!"

    def start(self):
        print(self.welcome_message)

    def result(self):
        print(self.winning_message if input("Guess the word: ") == guess else self.losing_message)


def main():
    game = Hangman()
    game.title()
    game.play()


if __name__ == '__main__':
    main()
