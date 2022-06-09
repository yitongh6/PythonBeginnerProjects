# 1. Generate a random number using random generator
# 2. Ask user to input a number
# 3. Give feedback about > or < or guessed
# 4. Show the attempts tried.

import random

# def a function random by computer
def guessTheNumber(x):
    random_number = random.randint(1, x)
    answer = int()
    attempts = 0

    while answer != random_number:
        answer = int(input(f'\nEnter a number between 1 and {x}: '))
        attempts += 1
        if answer > random_number:
            print("\nThe number you provided is greater than the answer. Please try again.")
        elif answer < random_number:
            print("\nThe number you provided is lesser than the answer. Please try again.")
        else:
            print(f"\nYou are correct. The number is {random_number}.")
        print(f"You guessed {attempts} time(s).")

#uncomment to try
#guessTheNumber(10)

def computer_guessTheNumber():
    our_low = int(input("Enter the lower range of your number: "))
    our_up = int(input("Enter the upper range of your number: "))
    our_key = int(input("Enter the number: "))

    computer_guess = int()

    low = our_low
    high = our_up
    attempts = 0

    while computer_guess != our_key:
        attempts += 1
        computer_guess = random.randint(low, high)
        if computer_guess > our_key:
            high = computer_guess - 1
            print(f'\nThe computer\'s attempt {attempts} is {computer_guess}. It is too high.')
        elif computer_guess < our_key:
            low = computer_guess + 1
            print(f'\nThe computer\'s attempt {attempts} is {computer_guess}. It is too low.')

    print(f'The computer guessed {computer_guess} finally! The computer guessed {attempts} time(s).')

#uncomment to try
#computer_guessTheNumber()

