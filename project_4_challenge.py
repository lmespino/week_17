# # PYTHON DAY 4 CHALLENGE ~~~ Devin, Oscar, Lance

# import random

# name = input("What is your name?: ")
# print(f"Well {name}, I've thought of a number between 1-100 and you have only eight tries to guess it. What number do you think it is?")

# secret_num = random.randint(1,100)
# guess = input("Enter a number between 1-100: ")
# number_of_guesses = 0

# def run_once(f):
#     def wrapper(*args, **kwargs):
#         if not wrapper.has_run:
#             wrapper.has_run = True
#             return f(*args, **kwargs)
#     wrapper.has_run = False
#     return wrapper

# while number_of_guesses < 8:
#     if int(guess) == secret_num:
#         print("You guessed correctly.")
#     elif int(guess) < 1 or guess > 100:
#         print("You have chosen a number that is out of play.")
#         run_once(number_of_guesses += 1)
#     elif int(guess) > secret_num:
#         print("The number entered is greater than the secret number.")
#         number_of_guesses += 1
#         continue
#     elif int(guess) < secret_num:
#         print("The number entered is less than the secret number.")
#         continue

# import random

# # Prompting user to give their name to be used in a sentece asking the user to input random numbers
# name = input("What is your name?: ")
# print(f"Well {name}, I've thought of a number between 1-100 and you have only eight tries to guess it. What number do you think it is?")

# secret_num = random.randint(1, 100)
# number_of_guesses = 0  
# max_guesses = 8

# while number_of_guesses < max_guesses:
#      guess = int(input(f"Attempt {number_of_guesses + 1}: What number do you think it is? "))

# if guess < 1 or guess > 100:
#     print("The number is out of bounds! Please choose a number between 1 and 100.")
# elif guess < secret_num:
#     print("Your guess is too low!")
# elif guess > secret_num:
#     print("Your guess is too high!")
# else:
#     print(f"Congratulations, {name}! You guessed the number correctly!")

# number_of_guesses += 1
    
# # This lets the user know that they have used up all of their guesses
# if number_of_guesses == max_guesses:
#         print(f"Sorry, {name}, you've used all {max_guesses} tries. The secret number was {secret_num}.")

import random

def guess_number_game():
    # Ask for the user's name
    user_name = input("What is your name? ")
    # Text prompt
    print(f"Well {user_name}, I've thought of a number between 1 and 100 and you have only eight tries to guess it. What number do you think it is?")
   
    # The secret number is chosen randomly between 1 and 100
    secret_number = random.randint(1, 100)
    # Attempts
    attempts = 8
   
    # Loop for the user's attempts
    for attempt in range(1, attempts + 1):
        # Ask the user to input their guess
        guess = int(input(f"Attempt {attempt}: "))
       
        # Check if the guess is out of bounds
        if guess < 1 or guess > 100:
            print("You've chosen a number out of play! Please choose a number between 1 and 100.")
        # Check if the guess is too low
        elif guess < secret_number:
            print("Wrong answer! You've chosen a lower number than the secret number.")
        # Check if the guess is too high
        elif guess > secret_number:
            print("Wrong answer! You've chosen a higher number than the secret number.")
        # If the guess is correct
        else:
            print(f"Congratulations, {user_name}! You've guessed the secret number {secret_number} in {attempt} tries!")
            break
    else:
        # If all 8 attempts are used and the user hasn't guessed the number
        print(f"Sorry, {user_name}, you've used all {attempts} tries. The secret number was {secret_number}.")

# Run the game
guess_number_game()