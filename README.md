Hangman Game

Welcome to the Hangman game! This is a simple command-line game where you can guess words from different categories with the help of hints. The goal is to guess the word before the hangman is fully drawn.

Features

Categories: The game includes multiple categories: Programming, Animals, Fruits, and Countries.
Hints: Each word comes with three hints that can be used to assist in guessing.
ASCII Art: The game visually represents the hangman with ASCII art that updates with each wrong guess.
Score System: Your score increases by 10 points for a correct guess and decreases by 5 points if you lose.

Code Overview

display_hangman(tries)
This function returns the current state of the hangman as ASCII art based on the number of tries left.

get_word(category)
This function selects a random word and its hints from the specified category. The categories include Programming, Animals, Fruits, and Countries.

provide_hint(word, hints_used)
This function returns the next hint for the word based on the number of hints already used.

play()
This is the main function that runs the game. It handles:

Prompting the user to choose a category
Displaying the initial state of the game
Managing the main game loop where the player guesses letters or words
Displaying hints and updating the game state
Ending the game with a win or loss message
Asking the player if they want to play again

How to Play

Choose a Category:
When you start the game, you will be prompted to choose a category from the available options.
Guess the Word:
You will be given a word to guess, represented by underscores. You can guess one letter at a time or try to guess the entire word.
Hints:
You can use hints to help you guess the word. Each hint costs one chance.
Tries: 
You have 6 chances to guess the word. Each incorrect guess reduces the number of tries left.
Win/Lose: 
If you guess the word correctly, you win! If you run out of tries before guessing the word, you lose.
