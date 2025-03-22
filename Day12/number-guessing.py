import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
gameOn = True
attempts = 0

def easy_mode():
    global attempts
    attempts = 10

def hard_mode():
    global attempts
    attempts = 5


if difficulty == 'easy':
    easy_mode()
else:
    hard_mode()

while gameOn:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess > number:
        print("Too high.")
        attempts -= 1
    elif guess == number:
        print(f"You got it! The answer was {number}.")
        print("Guess again.")
        gameOn = False
        break
    else:
        print("Too low.")
        attempts -= 1

    if attempts == 0:
        print(f"You lost! The answer was {number}.")
        gameOn = False



