'''function to fetch words.'''
import random

wordslist = "wordlist.txt"

def get_random_word(min_word_length):
    "get a random word from the wordlist using no extra memory"
    words = []
    with open (wordslist, 'r') as f:
        for word in f :
            if '('or')' in word:
                continue
            word = word.strip().lower()
            if len(word) < min_word_length:
                continue  # Skip the word because it is too short.
            words.append(word)
    return random.choice(words)
