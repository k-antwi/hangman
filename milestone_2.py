import random

word_list = ['apple', 'orange', 'mango', 'grapes', 'plums']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input('Enter a single letter\n')

if guess.isalpha() and len(guess) == 1:
    print('Good guess')
else:
    raise 'Oops! That is not a valid input.'

