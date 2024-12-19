import random

def hangman():
    words = ["python", "hangman", "programming", "developer", "challenge"]
    word_to_guess = random.choice(words)
    guessed_word = ["_"] * len(word_to_guess)
    attempts_left = 6
    guessed_letters = set()

    print("Welcome to Hangman!")
    print(f"The word has {len(word_to_guess)} letters: {' '.join(guessed_word)}")

    while attempts_left > 0 and "_" in guessed_word:
        print(f"\nAttempts remaining: {attempts_left}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print("Word to guess: " + " ".join(guessed_word))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("Good guess!")
            for index, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            print("Wrong guess!")
            attempts_left -= 1

    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word_to_guess)
    else:
        print("\nGame over! The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
