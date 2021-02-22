from hangman_words import word_list
import random


def hangman():
    # Pick a random word from the imported word_list
    word = random.choice(word_list)
    word_comp = word

    # check the word is chosen successfully
    print(word)

    # Letters in word are replaced with '_'
    # And you are told how many letters the word has
    length = len(word)
    hidden = '_'*length
    print(f"The word is {length} letters long!")
    print(hidden)

    # Start guessing letters
    # If a letter is correct, it is revealed in hidden, and hidden is returned with the letters that are known
    # If it is wrong, the lives counter goes down by 1
    # In both cases, the player can guess again
    # The game ends when either all letters are found
    # Or the lives counter equals 0

    lives = 6
    letters_so_far = []
    correct_letters = []
    incorrect_letters = []

    while lives != 0:
#        for char in word:
#            if char not in correct_letters:
#                hidden = word.replace(char, '_')

        guess = str(input(f"Guess a letter! "))
        if guess.upper() not in word:
            letters_so_far.append(guess.upper())
            incorrect_letters.append(guess.upper())
            lives -= 1
            print(f"Nope! {lives} lives left!")
            print(f"So far you've guessed {letters_so_far}\n"
                  f"The word is made from {correct_letters}\n"
                  f"{incorrect_letters} is not in the word")
            if lives == 0:
                print("Game Over!")
            continue
        else:
            letters_so_far.append(guess.upper())
            correct_letters.append(guess.upper())
            print("Yeah!")
            word_comp = word_comp.replace(guess.upper(), '_')
            # print(word_comp)
            print(f"So far you've guessed {letters_so_far}\n"
                  f"The word is made from {correct_letters}\n"
                  f"{incorrect_letters} is not in the word")
            if word_comp == hidden:
                print(f"Congrats, you win! The word was {word}")
                break

# if a letter is correct, can you replace parameter word with underscore EXCEPT for the letters in correct_letters?
# for char in word if char not in correct_letters word.replace(char, '_')
# define hidden within for loop?
# hidden = word.replace(char, '_')
# test out in fresh python document

hangman()
