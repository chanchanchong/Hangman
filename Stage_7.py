# Stage 7/8: Error_

# Description

# Now that we are done with the basics, let's work on perfecting some 
# details.

# In the previous stage, if the user entered the same letter twice, the 
# program reduced the number of remaining attempts regardless of
# whether this was a correct letter or not. This doesn't seem fair to the
# player, does it? They gain no additional information about the
# situation on the field yet the program still reduces their remaining 
# attempts, Let's fix it!

# Objectives
#   1. If the user enters the same letter twice, then the program
#      should output "You've already guessed this letter. This
#      message should also be printed if the user inputs a letter
#      that doesn't appear in the word. The number of attempts
#      shouldn't be decreased in this case.

#   2. Also, you should check to make sure the player entered an
#      English lowercase letter. If not, the program should print
#      Please enter a lowercase English letter.
#   3. You should also check if he player entered exactly one letter. If
#      not, the program should print You should input a
#      single letter. Remember that zero is also not one!
#   4. Note that none of these three errors should reduce the number
#      of remaining attempts!

# Please, make sure that your program's output formatting precisely
# follows the output formatting in the example. Pay attention to the
# empty lines between tries and in the end.

# Examples
# The greater-than symbol followed by a space ( > ) represents the
# user input. Note that it's not part of the output.

# Example 1

# H A N G M A N

# ----------
# Input a letter: > a

# -a-a------
# Input a letter: > i

# -a-a---i--
# Input a letter: > o
# That letter doesn't appear in the word

# Input a letter: > o
# You've already guessed this letter

# -a-a---i--
# Input a letter: > p

# -a-a---ip-
# Input a letter: > p
# You've already guessed this letter

# -a-a---ip-
# Input a letter: > h
# That letter doesn't appear in the word

# -a-a---ip-
# Input a letter: > k
# That letter doesn't appear in the word

# -a-a---ip-
# Input a letter: > a
# You've already guessed this letter

# -a-a---ip-
# Input a letter: > z
# That letter doesn't appear in the word

# -a-a---ipt
# Input a letter: > t

# -a-a---ipt
# Input a letter: > x
# That letter doesn't appear in the word

# -a-a---ipt
# Input a letter: > b
# That letter doesn't appear in the word

# -a-a---ipt
# Input a letter: > d
# That letter doesn't appear in the word

# -a-a---ipt
# Input a letter: > w
# That letter doesn't appear in the word
# You lost!

# Examples 

# H A N G M A N

# ----
# Input a letter: > j

# j---
# Input a letter: > i
# That letter doesn't appear in the word

# j---
# Input a letter: > +
# Please enter a lowercase English letter

# j---
# Input a letter: > A
# Please enter a lowercase English letter

# j---
# Input a letter: > ii
# You should input a single letter

# j---
# Input a letter: > ++
# You should input a single letter

# j---
# Input a letter: >
# You should input a single letter

# j---
# Input a letter: > g
# That letter doesn't appear inthe word

# j---
# Input a letter: > a

# ja-a
# Input a letter: > v
# You guessed the word java!
# You survived!

from random import choice


class Hangman:

    def __init__(self):
        self.words = ['java', 'python', 'kotlin', 'javascript']
        self.guessed_letters = []
        self.tries = 8
        self.correct_word = 'javascript'
        self.guess_word = list('-' * len(self.correct_word))
        self.starting_message = "H A N G M A N"
        self.losing_message = "You lost!"
        self.winning_message = "You survived!"
        self.not_in_letter = "That letter doesn't appear in the word"
        self.already_guess = "You've already guessed this letter"
        self.errormessage_not_lowercase = "Please enter a lowercase English letter"
        self.errormessage_not_single_letter = "You should input a single letter"

    def start(self):
        print(self.starting_message)
        self.guessing_game()

    def guessing_game(self):
        while self.tries != 0:
            if '-' not in self.guess_word:
                break
            self.ask_letter()
        self.result()

    def ask_letter(self):
        print()
        print(''.join(self.guess_word))
        answer = input("Input a letter: ")
        self.check_letter(answer)
        self.guessed_letters.append(answer)

    def check_letter(self, guess):
        if len(guess) != 1:
            print(self.errormessage_not_single_letter)
            return
        if guess in self.guessed_letters:
            print(self.already_guess)
            return
        if not guess.isalpha() or guess.isupper():
            print(self.errormessage_not_lowercase)
            return
        if guess in self.correct_word:
            for i in range(len(self.correct_word)):
                if guess == self.correct_word[i]:
                    self.guess_word[i] = guess

        else:
            print(self.not_in_letter)
            self.tries -= 1

    def result(self):
        print(self.losing_message if self.tries == 0 else self.winning_message)


def main():
    game = Hangman()
    game.start()


if __name__ == '__main__':
    main()
