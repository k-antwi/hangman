import random
from typing import List
from numbers import Number

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.word = None
        self.word_guessed = None
        self.num_letters = 0
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for l in self.word]
        self.num_letters = len(self.word)
        print(self.word)
        
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            # self.word_guessed = [l if guess == l else '_' for l in self.word]
            for idx, l in enumerate(self.word):
                if guess == l:
                    self.word_guessed[idx] = l
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while self.num_lives > 0:
            guess = input('Guess a letter\n')
            if guess.isalpha() == False or len(guess) > 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

    def play_game(self):    
        while self.num_lives == 5:
            self.ask_for_input()
            if self.num_lives == 0:
                print("You lost!")
                break
            if self.num_letters > 0:
                self.ask_for_input()
            if self.num_lives > 0 and self.num_letters <= 0:
                print('Congratulations. You won the game!')

word_list = ['apple', 'orange', 'mango', 'grapes', 'plums']
game = Hangman(word_list)
game.play_game()