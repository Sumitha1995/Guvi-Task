#random is built in function which is imported

import random

print("\n Guess the Number Game")

#Function selects the random number

number = random.randint(1, 100)

print("Guess a number between 1 and 100")

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low & Please try again.")
    elif guess > number:
        print("Too high & Please try again.")
    else:
        print("🎉 Your guess is correct!")
        print("Number of attempts is:",attempts)
        break
