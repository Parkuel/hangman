import random

def choose_word():
    '''Return a random word'''
    words = ['vilnius', 'klaipeda', 'kaunas', 'utena', 'visaginis', 'ukmerge', 'jonava', 'trakai', 'alytus', 'luoke']
    return random.choice(words)

def display_word(word, guessed_letters):
    # Display the guessed word and empty spaces
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def draw_hangman(attempts):
    stages = [  # Final stage: Head, body, both arms, and both legs
                '''
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |     / \\
                   -
                ''',
                # Head, body, both arms, and one leg
                '''
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |     /
                   -
                ''',
                # Head, body, both arms
                '''
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |
                   -
                ''',
                # Head, body, one arm
                '''
                   --------
                   |      |
                   |      O
                   |     /|
                   |
                   -
                ''',
                # Head and body
                '''
                   --------
                   |      |
                   |      O
                   |
                   |
                   -
                ''',
                # Head
                '''
                   --------
                   |      |
                   |      
                   |
                   |
                   -
                ''',
                # Initial empty stage
                '''
                   --------
                   |      |
                   |      
                   |
                   |
                   -
                '''
    ]
    return stages[attempts]

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        # Check if the guess is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        # Add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)

        # Check if the guess is correct
        if guess in word_to_guess:
            print("Correct!")
        else:
            print("Incorrect!")
            attempts -= 1
            print("Attempts left:", attempts)

        # Display the hangman and the word with guessed letters
        print(draw_hangman(attempts))
        print(display_word(word_to_guess, guessed_letters))

        # Check if the word has been guessed
        if '_' not in display_word(word_to_guess, guessed_letters):
            print("Congratulations! You guessed the word:", word_to_guess)
            break

    if attempts == 0:
        print("Sorry, you ran out of attempts. The word was:", word_to_guess)

hangman()
