import random
number_to_guess = random.randint(1, 100)
print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
guess = int(input("Enter your guess: "))
while guess != number_to_guess:
    if guess < number_to_guess:
        print("Your guess is too low. Guess again.")
    elif guess > number_to_guess:
        print("Your guess is too high. Guess again.")
    guess = int(input("Enter your guess: "))
print("Congratulations! You guessed the number correctly!")
