import random
import string
from hangman_words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set() # what the user has guessed
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left")
        print("You have used these letters", " ".join(guessed_letters))
        word_list = [letter if letter in guessed_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))
        
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter is not in the word")
        elif user_letter in guessed_letters:
            print("You have already tried this letter")
        else:
            print("You typed an invalid character")

    if lives > 0:
        print(f"Congratulations, the word was {word}!")
    else:
        print(f"You lost, the word was {word}")

hangman()