import random

from sklearn.metrics import adjusted_mutual_info_score
from word import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word

def hangman():
    word = get_valid_word(words).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    # getting the user input
    while len(word_letters) >0 and lives > 0:

        print( 'You have still ', str(lives), ' and you have used these letters ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("current word: ", ' '.join(word_list))

        user_letter = input('Enter one letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
            
        elif user_letter in used_letters:
            print(' You used this letter already. Please use another letter! ')
        
        else:
            print("you used an invalid character. Please try again")
    
    print(word)
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('final word ', ' '.join(word_list))


    
hangman()