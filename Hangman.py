def hangman(secret_word):
    guessed_letters = ''
    attempts = 6
    hangman_steps = ['____\n|  |\n|  O\n| /|\\\n| / \\\n|', '____\n|  |\n|  O\n| /|\\\n| /\n|', '____\n|  |\n|  O\n| /|\\\n|\n|', '____\n|  |\n|  O\n| /|\n|\n|', '____\n|  |\n|  O\n|  |\n|\n|', '____\n|  |\n|  O\n|\n|\n|', '____\n|  |\n|\n|\n|\n|']

    while attempts > 0:
        failed = 0
        for char in secret_word:
            if char in guessed_letters:
                print(char, end='')
            else:
                print("_", end='')
                failed += 1
        if failed == 0:
            print("\nYou win!")
            break

        guess = input("\nGuess a letter: ")
        guessed_letters += guess

        if guess not in secret_word:
            attempts -= 1
            print(hangman_steps[attempts])
            print("Incorrect guess. You have", attempts, "more attempts.")

        if attempts == 0:
            print("\nYou're hung! The word was:", secret_word)

secret_word = input("Enter a secret word for the game: ")
hangman(secret_word)