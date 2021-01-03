#!/usr/bin/env python
"""
Een raadspelletje waarbij je een woord moet raden dat in een lijst staat
De lijst mag je kiezen:
ofwel uit een bestand lezen
ofwel zelf een lijst samenstellen in je script
"""


import random


__author__ = "Jens Vansteenvoort"
__email__ = "jens.vansteenvoort@student.kdg.be"
__status__ = "Development"


WORD = ('apple', 'oracle', 'amazon', 'microsoft') #list of words that may be the answer
word = random.choice(WORD) #chooses 1 word random
correct = word
letter_guess = ''
word_guess = ''
store_letter = ''
count = 0
limit = 5

print('Welcome to "Guess the Word Game!"')
print('You have 5 attempts at guessing letters in a word')
print('Let\'s begin!')

#
while count < limit:
    letter_guess = input('Guess a letter: ')

    if letter_guess in word:
        print('yes!')
        store_letter += letter_guess
        count += 1

    if letter_guess not in word:
        print('no!')
        count += 1

print('Now its time to guess. You have guessed',len(store_letter),'letters correctly.')
print('These letters are: ', store_letter)

#code for guess full word
word_guess = input('Guess the whole word: ')
while word_guess:
    if word_guess.lower() == correct:
        print('Congrats!')
        break

    elif word_guess.lower() != correct:
        print('Unlucky! The answer was,', word)
        break

input('Press Enter to leave the program')

if __name__ == '__main__':  # code to execute if called from command-line
    main()
