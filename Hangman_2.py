from hangman_words import word_list
import random


def hangman():
    word = random.choice(word_list)
    word2 = word
    word_check = list(word)

    # CHEATS!
    # print(word)
    # print(word2)
    # print(word_check)

    # You are told how many letters the word has
    length = len(word)
    print(f"The word is {length} letters long!")

    # Starting lives (adjust to suit your difficulty!)
    lives = 6
    # Temp tables to store guessed and correct letters in
    letters_so_far = []
    correct_letters = []

    # As long as you have 1 or more lives, you can play
    while lives > 0:
        # Hides the original word with '___' as word2, which is printed throughout the game
        for x in word:
            if x in correct_letters:
                pass
            else:
                word2 = word2.replace(x, '_')

        # Prints out the hidden word initially, and then any progress you've made in uncovering it during the game
        print(word2)

        # Player is now allowed to guess letters
        guess = str(input("Guess a letter! "))

        # If the player's guess in incorrect
        if guess.upper() not in word:
            letters_so_far.append(guess.upper())

            # Lose 1 life
            lives -= 1

            # Tell player how many lives they have left and what they've guessed so far
            print(f"Nope! {lives} lives left! So far you've guessed {letters_so_far}")

            # If the player runs out of lives, it's game over! You are then told what the word was
            if lives == 0:
                print(f"Game Over! The word was {word}")

        # If the player's guess is correct
        else:
            letters_so_far.append(guess.upper())

            # Add the guess to the correct guesses list
            correct_letters.append(guess.upper())
            print(f"That's a match! So far you've guessed {letters_so_far}")

            # Go through the original, unhidden word (behind the scenes)
            for x in word:
                # If the letter is in the original word, do nothing with that letter
                if x in correct_letters:
                    pass
                # Otherwise, replace all other letters with '_', appearing to "uncover" the hidden letters
                else:
                    word2 = word.replace(x, '_')

            # Win condition, if the two lists match, you win! You're also told what the word is once you win
            if sorted(set(word_check)) == sorted(set(correct_letters)):
                print(f"You win! The word was {word}")
                break


hangman()
