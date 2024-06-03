# Lab 2: Hangman

import random

def get_random_word():
    words = ["python", "hangman", "challenge", "terminal", "computer", "programming", "code", "developer", "software", "engineer", "debugging", "syntax", "error", "keyboard", "monitor", "mouse", "screen", "internet", "website", "server", "database", "algorithm", "function", "variable", "loop", "conditional", "statement", "object", "class", "method",]
    return random.choice(words)

#print(get_random_word())

def display_hangman(guesses_left):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           -
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           -
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           -
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           -
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           -
        """,
        """
           ------
           |    |
           |    O
           |
           |
           -
        """,
        """
           ------
           |    |
           |
           |
           |
           -
        """
    ]
    return stages[guesses_left]

def play_game():
    word = get_random_word()
    word_length = len(word)
    guessed_letters = ["_"] * word_length
    guessed_incorrectly = []
    guesses_left = 6
    win = False

    print("Welcome to Hangman!")
    print(f"The word has {word_length} letters.")
    
    while guesses_left > 0 and not win:
        print(display_hangman(guesses_left))
        print("Word: " + " ".join(guessed_letters))
        print(f"Incorrect guesses: {', '.join(guessed_incorrectly)}")
        print(f"Guesses left: {guesses_left}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters or guess in guessed_incorrectly:
            print("You've already guessed that letter. Try again.")
            continue
        
        if guess in word:
            for idx, letter in enumerate(word):
                if letter == guess:
                    guessed_letters[idx] = guess
            if "_" not in guessed_letters:
                win = True
        else:
            guessed_incorrectly.append(guess)
            guesses_left -= 1

    if win:
        print("Congratulations, you've won!")
        print(f"The word was: {word}")
    else:
        print(display_hangman(guesses_left))
        print("Sorry, you've lost.")
        print(f"The word was: {word}")

    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_game()