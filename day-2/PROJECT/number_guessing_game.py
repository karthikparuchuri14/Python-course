import random

number = random.randint(1, 100)

print("Welcome to python number guessing game")

while True:
    guess = int(input("Guess a random number between 1 and 100: "))

    if guess == number:
        print("correct!")
        break
    else:
        print("not correct!")