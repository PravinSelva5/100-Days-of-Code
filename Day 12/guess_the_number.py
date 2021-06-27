# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

GAME_ON = True


def attempts(difficulty):
    """Defines the number of attempts the user has to guess"""
    if difficulty == 'easy':
        attempts = 5
    else:
        attempts = 10
    
    return attempts

def game_play(chances):
    number = random.randint(1,100)
    for _ in range(chances):
        print(f"You have {chances} attempts remaining to guess the number.")
        guess = int(input("Make a guess:")
)
        if guess == number: 
            print("You win!")
        elif guess > number:
            print("Too high.\nGuess again.")
        else:
            print("Too low.\nGuess again.")
        chances -= 1

        if chances == 0:
            print("You lose.")

while GAME_ON:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    chances = attempts(difficulty)
    game_play(chances)


    GAME_ON = False

