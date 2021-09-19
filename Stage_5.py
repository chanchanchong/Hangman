# Stage 5/8: Keep trying

# Description
# Let's make the game iterative. Now it's time to make the game
# resemble the classic version of Hangman a bit more. The player
# should now guess letters in the word instead of typing the
# entire word all at once. If the player guesses a letter, it should
# be uncovered in the word. For now, start by building the defeat
# condition and add 8 tries to guess a letter that appears in the
# word. When the player runs out of attempts, the game ends.

# Later we will determine the winning conditions, but in this
# stage, let's just see how well our player guesses the word on
# each attempt.

# Objectives
# Now your game should work as follows:

# 1. A player has exactly 8 tries and enters letters. Nothing
# changes if a player has more tries left but they have
# already guessed the word.
# 2. If the letter doesn't appear in the word, the computer
# takes one try away - even if the user has already
# guessed this letter.
# 3. If the player doesn't have any more attempts, the game
# should end and the program should show a losing
# message. Otherwise, the player can continue to input
# letters.
# 4. Also, the word should be selected from our list:
# 'python', 'java', 'kotlin', 
# 'javascript', so that your program can be testesd
# more reliably.

# Please, make sure that your program's output formatting
# precisely follows the example. Pay attention to the empty lines
# between tries and at the end.

# Examples
# The greater-than symbol followed by a space ( > ) represents
# the user input. Note that it's not part of the output.

# H A N G M A N

# ----------
# Input a letter: > a

# -a-a------
# Input a letter: > i

# -a-a---i--
# Input a letter: > o
# That letter doesn't appear in the word

# -a-a---i--
# Input a letter: > z
# That letter doesn't appear in the word

# -a-a---i--
# Input a letter: > l
# That letter doesn't appear in the word
# 
# -a-a---ip-
# Input a letter: > p
# 
# -a-a---ip-
# Input a letter: > h
# That letter doesn't appear in the word
# 
# -a-a---ip-
# Input a letter: > k
# That letter doesn't appear in the word
# 
# Thanks for playing!
# We'll see how well you did in the next stage
# Example 2
# 
# H A N G M A N
# 
# ----
# Input a letter: > j
# 
# j---
# Input a letter: > i
# That letter doesn't appear in the word
# 
# j---
# Input a letter: > g
# That letter doesn't appear in the word
# 
# j---
# Input a letter: > o
# That letter doesn't appear in the word
# 
# j---
# Input a letter: > a
# 
# ja-a
# Input a letter: > v
# 
# java
# Input a letter: > a
# 
# java
# Input a letter: > j
# 
# Thanks for playing!
# We'll see how well you did in the next stage

from random import choice


class Hangman:
    def __init__(self):
        self.words = ['python', 'java', 'kotlin', 'javascript']
        self.guess_word = choice(self.words)
        self.guess_temp = list('-' * len(self.guess_word))
        self.welcome_message = "H A N G M A N"
        self.winning_message = "You survived!"
        self.losing_message = "You lost!"
        self.not_in_letter_warning = ""
        self.input_message = "Input a letter: "
        self.tries = 8
        self.answer = None
        self.final_message = "\nThanks for playing!\nWe'll see how well you did in the next stage"

    def start(self):
        print(self.welcome_message)
        self.game()

    def game(self):
        while self.tries != 0:
            self.ask_input()
            self.check_input()
        self.result()

    def ask_input(self):
        print(''.join(self.guess_temp))
        self.answer = input(self.input_message)

    def check_input(self):
        if self.answer in self.guess_word:
            for x in range(len(self.guess_word)):
                if self.answer == self.guess_word[x]:
                    self.guess_temp[x] = self.answer
        else:
            print(self.not_in_letter_warning)
        self.tries -= 1

    def result(self):
        # print(self.winning_message if self.answer == self.guess else self.losing_message)
        print(self.final_message)


def main():
    hangman = Hangman()
    hangman.game()


if __name__ == '__main__':
    main()
