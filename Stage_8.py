
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
        self.menu = 'Type "play" to play the game, "exit" to quit: '
        self.input = None

    def start(self):
        print(self.starting_message)
        self.menu_screen()

    def menu_screen(self):
        while True:
            self.input = input(self.menu)
            if self.input == "play":
                self.guessing_game()
            elif self.input == "exit":
                quit()
            else:
                continue


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
