#random is built in function which is imported

import random

print("Word Scramble Game")

words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

# Select random word
selected_word = random.choice(words)

# Convert to list
letters = list(selected_word)

# Shuffle letters
shuffled_letters = random.sample(letters, len(letters))

# Join to form string
scrambled_word = ''.join(shuffled_letters)

while scrambled_word == selected_word:
    shuffled_letters = random.sample(letters, len(letters))
    scrambled_word = ''.join(shuffled_letters)

# Display scrambled word
print("Scrambled word:", scrambled_word)
print("Please guess the correct word")

attempts = 0

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == selected_word:
        print("Its Correct!")
        print("Number of attempts:",attempts)
        break
    else:
        print("Wrong Please try again.")