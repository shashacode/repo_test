''' play hangman game'''
name = input(" insert name ")

print("Yo ! let's play" + name)

import random

words_list = ['man','woman','table','goats','cow','human','living','cost','gold']

guessed_word = []
chosen_word = random.choice(words_list)
length_word = len(chosen_word)


trials = 5
print(guessed_word)
def game(guessed_word):
    for guessed_word in chosen_word:
        print(guessed_word)
        guessed_word.append('_')

game(guessed_word)
print("word has", length_word, "number of characters")
print(guessed_word)
