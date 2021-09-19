# Stage 2/8: Let's play a game

# Description

# At this stage, you will create a real game, though it will
# still be quite simple. There will be two possible outcomes.
# Let's first print a welcome messasge and then ask the
# player to guess the word we set for the game. If our
# player manages to guess the exact word, the game
# reports "win"; otherwise it will "hang" the player.

# Objectives
#  1. Ask the player for a possible word.
#  2. Print "You survived!" if the user guesses the
#     word.
#  3. Print "You lost!" if the user guesses incorrectly.

# By the way, python should be the word the player
# needs to guess to win the game.

# Examples
# The greater-than symbol followed by a space ( > )
# represents the user input. Note that it's not the part of
# the output.

class Hangman:
    def __init__(self):
        self.welcome_message = "H A N G M A N"
        self.winning_message = "You survived!"
        self.losing_message = "You lost!"

    def start(self):
        print(self.welcome_message)
        self.result()

    def result(self):
        print(self.winning_message if input("Guess the word: ") == "python" else self.losing_message)

def main():
    game = Hangman()
    game.start()

if __name__ == '__main__':
    main()