import random
from art import *

print("Welcome To The Hangman Game")
hangman_logo()

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra').split()

barrier = "*" * 25

word_to_guess = random.choice(words)
placeholder = "_" * len(word_to_guess)

print(f"Word to guess: {placeholder}")

n = 0
live = 6
correct = []

while True:
    guess_letter = input("Guess a letter: ").lower()

    if guess_letter not in word_to_guess:
        live -= 1
        n += 1

        print(f"You guessed {guess_letter}, that's not in the word. You lose a life.")
        print(hangmanpics[n])
        print(f"{barrier}{live}/6 LIVES LEFT{barrier}")
        if live != 0:
            print(f"Word to guess: {placeholder}")


        if live == 0:
            print(f"{barrier}IT WAS {word_to_guess}! YOU LOSE{barrier}")
            break

    else:
        display = ""

        for letter in word_to_guess:
            if letter == guess_letter:
                display += guess_letter
                correct.append(letter)
            elif letter in correct:
                display += letter
            else:
                display += "_"

        placeholder = display

        print(hangmanpics[n])
        print(f"{barrier}{live}/6 LIVES LEFT{barrier}")
        print(f"Word to guess: {placeholder}")

        if "_" not in placeholder:
            print(f"{barrier}YOU GUESSED IT! THE WORD WAS {word_to_guess}{barrier}")
            break