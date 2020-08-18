# #declare filename and open file for reading
# file_name = "wordlist.txt"
# file = open(file_name, "r")

# #read file and split into individual words
# data = file.read().split('\n')

# #import the random module for random value selections
# import random

# #select a random choice from the list of words read fom file
# selected_word = random.choice(data)
# length_word = len(selected_word)

# print("I have selected a word with", length_word, "characters")

# #create a placeholder to hold successfully guessed characters
# guessed_chars_list = []


# #declare the max num of turns possible
# turns = 5

# #while loop is declared with turns to limit num of turns a user has
# while turns:

# #collect guessed word from user
#     guessed_char = input("please guess a char : ")

# #check if character guessed by user is in the word that has been selected by comp

#     if guessed_char in selected_word:
#         #if char is guessed right then add the char to the list of successfully guessed char
#         guessed_chars_list.append(guessed_char)
#     else:
#         #if char is guessed wrong then reduce num of turns
#         turns -= 1

#     for character in selected_word:

#         #print character if it has been guessed correctly
#         if character in guessed_chars_list:
#             print(character, end = "")
#         else:
#             #print dash if it was guessed wrong
#             print("-", end = "")

#     print()
#     #print num of remaining turns left
#     print(f"You have {turns} tries left...!!!")
#     #check if all charcters of the selected word have been guessed correctly and if so end program
#     if set(guessed_chars_list) == set(selected_word):
#         print('congratulations')
#         break


#using functions
import random

selected_word = ''
guessed_chars_list = []

def get_random_text():

    file_name = "wordlist.txt"
    file = open(file_name, "r")
    data = file.read().split('\n')
    selected_word = random.choice(data)

    return selected_word

def check_guess(guessed_char):
    global selected_word
    global guessed_chars_list

    if guessed_char in selected_word:
        guessed_chars_list.append(guessed_char)
        return True
    else:
        return False

def display():
    global selected_word
    global guessed_chars_list

    for character in selected_word:
        if character in guessed_chars_list:
            print(character, end = "")
        else:
            print("_", end = "")
    print()

def check_if_guess_complete():
    global guessed_chars_list
    global selected_word

    if set(guessed_chars_list) == set(selected_word):
        print("congrst!!!")
        return True 
    else:
        return False
