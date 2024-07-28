import random

def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]

def get_word(category):
    word_dict = {
        "programming": [("python", ["A popular programming language", "This language is known for its simplicity", "It is named after a type of snake"]),
                        ("javascript", ["A language often used for interactive web pages", "It was originally named LiveScript", "This language shares its name with a type of coffee"]),
                        ("java", ["A high-level programming language developed by Sun Microsystems", "It is named after a type of coffee", "Used for building platform-independent applications"]),
                        ("html", ["A markup language used for creating web pages", "It stands for HyperText Markup Language", "Used in combination with CSS and JavaScript"]),
                        ("css", ["A style sheet language used for describing the presentation of a document", "It stands for Cascading Style Sheets", "Used alongside HTML and JavaScript"])],
        "animals": [("elephant", ["The largest land animal", "Has large ears and a trunk", "Known for its memory"]),
                    ("giraffe", ["The tallest land animal", "Has a long neck", "Spots on its coat help with camouflage"]),
                    ("kangaroo", ["A marsupial from Australia", "It has strong hind legs for hopping", "Known for carrying its young in a pouch"]),
                    ("penguin", ["A flightless bird that lives in the Southern Hemisphere", "Known for its tuxedo-like appearance", "Waddles when it walks"]),
                    ("lion", ["The king of the jungle", "Known for its mane", "A large wild cat found in Africa"])],
        "fruits": [("banana", ["A long curved fruit", "It has a peel that is yellow when ripe", "Monkeys are often associated with this fruit"]),
                   ("apple", ["A round fruit that can be red, green, or yellow", "Often associated with the phrase 'an apple a day'", "This fruit is commonly used to make cider"]),
                   ("mango", ["A tropical stone fruit", "It is known for its sweet and juicy flesh", "Often referred to as the 'king of fruits'"]),
                   ("grape", ["A small, round fruit that comes in clusters", "Used to make wine", "Can be red, green, or black"]),
                   ("kiwi", ["A small, brown, fuzzy fruit", "Its flesh is bright green", "Known for its unique taste and seeds"])],
        "countries": [("france", ["Known for the Eiffel Tower", "Famous for its wine and cuisine", "The capital city is Paris"]),
                      ("japan", ["An island nation in Asia", "Known for its technology and culture", "The capital city is Tokyo"]),
                      ("brazil", ["The largest country in South America", "Famous for the Amazon Rainforest", "The capital city is Brasília"]),
                      ("australia", ["Known for its unique wildlife", "The capital city is Canberra", "Famous for the Great Barrier Reef"]),
                      ("canada", ["The second largest country in the world", "Known for its maple syrup", "The capital city is Ottawa"])],
    }
    return random.choice(word_dict[category])

def provide_hint(word, hints_used):
    hints = {
        "python": ["A popular programming language", "This language is known for its simplicity", "It is named after a type of snake"],
        "javascript": ["A language often used for interactive web pages", "It was originally named LiveScript", "This language shares its name with a type of coffee"],
        "java": ["A high-level programming language developed by Sun Microsystems", "It is named after a type of coffee", "Used for building platform-independent applications"],
        "html": ["A markup language used for creating web pages", "It stands for HyperText Markup Language", "Used in combination with CSS and JavaScript"],
        "css": ["A style sheet language used for describing the presentation of a document", "It stands for Cascading Style Sheets", "Used alongside HTML and JavaScript"],
        "elephant": ["The largest land animal", "Has large ears and a trunk", "Known for its memory"],
        "giraffe": ["The tallest land animal", "Has a long neck", "Spots on its coat help with camouflage"],
        "kangaroo": ["A marsupial from Australia", "It has strong hind legs for hopping", "Known for carrying its young in a pouch"],
        "penguin": ["A flightless bird that lives in the Southern Hemisphere", "Known for its tuxedo-like appearance", "Waddles when it walks"],
        "lion": ["The king of the jungle", "Known for its mane", "A large wild cat found in Africa"],
        "banana": ["A long curved fruit", "It has a peel that is yellow when ripe", "Monkeys are often associated with this fruit"],
        "apple": ["A round fruit that can be red, green, or yellow", "Often associated with the phrase 'an apple a day'", "This fruit is commonly used to make cider"],
        "mango": ["A tropical stone fruit", "It is known for its sweet and juicy flesh", "Often referred to as the 'king of fruits'"],
        "grape": ["A small, round fruit that comes in clusters", "Used to make wine", "Can be red, green, or black"],
        "kiwi": ["A small, brown, fuzzy fruit", "Its flesh is bright green", "Known for its unique taste and seeds"],
        "france": ["Known for the Eiffel Tower", "Famous for its wine and cuisine", "The capital city is Paris"],
        "japan": ["An island nation in Asia", "Known for its technology and culture", "The capital city is Tokyo"],
        "brazil": ["The largest country in South America", "Famous for the Amazon Rainforest", "The capital city is Brasília"],
        "australia": ["Known for its unique wildlife", "The capital city is Canberra", "Famous for the Great Barrier Reef"],
        "canada": ["The second largest country in the world", "Known for its maple syrup", "The capital city is Ottawa"]
    }
    word_hints = hints[word]
    if hints_used < len(word_hints):
        return word_hints[hints_used]
    return "No more hints available."

def play():
    categories = ["programming", "animals", "fruits", "countries"]

    # Display welcome message and prompt for category
    print("Welcome to Hangman!\n")
    print("Choose a category: ", ", ".join(categories), "\n")
    category = input("Enter category: ").lower()

    # Validate category input
    while category not in categories:
        category = input("Invalid category. Please choose from programming, animals, fruits, countries: ").lower()

    # Fetch a random word and its hints from the chosen category
    choice = get_word(category)
    word = choice[0]
    hints = choice[1]
    word_completion = "_ " * len(word)
    guessed = False
    guessed_letters = []
    tries = 6
    hint_used = 0
    score = 0

    # Start the game
    print("Let's play Hangman!\n")
    print("Hint: " + hints[0], "\n")
    print(display_hangman(tries), "\n")
    print(word_completion, "\n")

    # Main game loop
    while not guessed and tries > 0:
        print(f"Chances left: {tries}\n")
        guess = input("Please guess a letter or word (or type 'hint' for an extra hint): ").lower()

        if guess == "hint":
            if hint_used < len(hints):
                print("Hint: " + provide_hint(word, hint_used), "\n")
                hint_used += 1
                tries -= 1
                # Display current game state after using a hint
                print(display_hangman(tries), "\n")
                print(word_completion, "\n")
            else:
                print("No more hints available.\n")
            continue  # Skip to the next iteration

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess, "\n")
            elif guess not in word:
                print(guess, "is not in the word.\n")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!\n")
                guessed_letters.append(guess)
                word_as_list = list(word_completion.replace(" ", ""))
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = " ".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess == word:
                guessed = True
            else:
                print(guess, "is not the word.\n")
                tries -= 1
        else:
            print("Invalid input.\n")

        # Display current game state if the game is still ongoing
        if not guessed and tries > 0:
            print(display_hangman(tries), "\n")
            print(word_completion, "\n")

    # End of game conditions
    if guessed:
        print("Congratulations! You guessed the word!\n")
        score += 10
    elif tries == 0:
        print(display_hangman(0), "\n")  # Display the full hangman
        print("Sorry, you ran out of tries. The word was " + word + ".\n")
        score -= 5

    print("Your score: " + str(score), "\n")

    # Prompt for replay
    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay == "yes":
        play()
    else:
        print("Thanks for playing! Goodbye!\n")

if __name__ == "__main__":
    play()
