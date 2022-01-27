from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, chosen_number, turns):
    """Check answer against guess. Returns the number of turns remaining."""
    if guess > chosen_number:
        print("Too high.")
        return turns - 1
    elif guess < chosen_number:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The number was {chosen_number}.")


def set_difficulty():
    difficulty_level = input("Choose a difficulty. Type 'easy or 'hard': ")
    if difficulty_level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    chosen_number = random.randint(1, 101)
    #print(f"Pssst, the correct answer is {chosen_number}")

    turns = set_difficulty()

    guess = 0
    while guess != chosen_number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, chosen_number, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != chosen_number:
            print("Guess again.")


game()
