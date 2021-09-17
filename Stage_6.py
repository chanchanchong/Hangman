# Stage 6/8: The value of life

# Description
# The most recent version of the game is not so much fun,
# since we still don't have a way to handle the player's
# victory. The player has 8 attempts decreases after each
# try even if the player guesses correctly.

# In this next version, a player may get a lot of attemps
# because they are limited only by the number of mistakes
# they make. A player can be mistaken 8 times. They win
# when they have guessed all the letters and still have at
# least one try. If the player uses their last try and actually
# guesses the word, then they've won!

# Objectives
# The player starts the game with 8 "lives", which is to sya,
# our player can input a wrong letter 8 times.

# 1. Print That letter doesn't appear in
# the word and reduce the number of remainning
# attempts if the word selected by the program
# doesn't contain this letter.

# 2. Print No improvements and reduce the
# attempts count if the selected word contains this
# letter but the user has already tried guessing it.

# 3. The number of remaining attempts should be
# decreased only if there are no letters to uncover.

# Please, make sure that your program's output formatting
# precisely follows the output formatting in the example.
# Pay attention to the empty lines between tries and at the
# end.

# Examples
# The greater-than symbol followed by a space ( > )
# represents the user input. Note that it's not part of the
# output.

# Example 1

# H A N G M A N

# ------
# Input a letter: > t

# --t---
# Input a letter: > z
# That letter doesn't appear in the word

# --t---
# Input a letter: > t
# No improvements

# --t---
# Input a letter: > y

# -yt---
# Input a letter: > x
# That letter doesn't appear in the word

# -yt---
# Input a letter: > y
# No improvements

# -yt---
# Input a letter: > p

# pyt---
# Input a letter: > p
# No improvements

# pyt---
# Input a letter: > q
# That letter doesn't appear in the word

# pyt---
# Input a letter: > p
# No improvements
# You lost!

# Examples 2

# H A N G M A N

# ----
# Input a letter: > j

# j---
# Input a letter: > i
# That letter doesn't appear in the word

# j---
# Input a letter: > g
# That letter doesn't appear in the word

# j---
# Input a letter: > g
# That letter doesn't appear in the word

# j---
# Input a letter: > g
# That letter doesn't appear in the word

# j---
# Input a letter: > g
# That letter doesn't appear in the word

# j---
# Input a letter: > a

# ja-a
# Input a letter: > v

# java
# You guessed the word!
# You survived!

from random import choice




def main():
    game = Hangman()
    game.start()


if __name__ == '__main__':
    main()
