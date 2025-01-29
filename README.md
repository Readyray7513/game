# Number Guessing Game

## Overview
`guessing_game.py` is a simple interactive game where the user guesses a randomly generated number within a specified range. The user sets an upper limit for the range, and the program generates a number between 1 and that limit. The user is given feedback on each guess, telling them whether the guess is too small, too large, or correct. The game continues until the user guesses the correct number.

## Features
- The user inputs a positive integer to set the upper limit of the guessing range.
- A random number is generated between 1 and the user's selected limit.
- Feedback is given after each guess (too small, too large, or correct).
- The game continues until the user guesses the correct number.

## Example Usage
```
$ python guessing_game.py
Level: 10
Guess: 5
Too small!
Guess: 8
Too large!
Guess: 7
Just right!
```

## How to Run
1. Run the program by executing:
   ```
   python guessing_game.py
   ```
2. Input a positive integer to set the range for the random number.
3. Make guesses, and receive feedback on each attempt.
4. The game ends when the user correctly guesses the number.

## Notes
- The range for the random number is between 1 and the level the user sets.
- The program ensures valid inputs by prompting the user to enter a valid integer.
