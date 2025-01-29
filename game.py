import random

def main():
    # Get the level from the user
    while True:
        try:
            level = int(input("Level: "))  # User inputs the range
            if level > 0:
                break
        except ValueError:
            print("Please enter a valid positive integer.")

    # Generate a random number between 1 and the level
    y = random.randint(1, level)

    # Start the guessing game
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < y:
                print("Too small!")
            elif guess > y:
                print("Too large!")
            else:
                print("Just right!")
                break  # Exit the loop if the guess is correct
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
