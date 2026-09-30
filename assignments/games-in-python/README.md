# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a Python Hangman game where players guess letters to uncover a hidden word before running out of attempts. This assignment helps you practice loops, conditionals, strings, and user input.

## 📝 Tasks

### 🛠️ Setup the Game

#### Description
Create a program that chooses a secret word from a list and shows the player how many letters are hidden at the start of the game.

#### Requirements
Completed program should:

- Store a list of words and choose one at random
- Display underscores or blanks for each letter in the secret word
- Prompt the player to enter a single letter guess
- Check whether the guess is in the word and update the display
- Keep track of incorrect guesses and remaining attempts

### 🛠️ Add Game Logic and End Conditions

#### Description
Finish the gameplay flow so the player can keep guessing until the word is solved or the attempts run out, and the program clearly announces the result.

#### Requirements
Completed program should:

- Continue accepting guesses until the word is complete or attempts are exhausted
- Prevent duplicate guesses and show a helpful message if a letter is repeated
- Display the correctly guessed letters in the correct positions
- Show a win message when the full word is guessed
- Show a lose message with the secret word when the player runs out of attempts
