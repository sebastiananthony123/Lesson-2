import random

secret_number = random.randint(1,100)
attempts = 0
max_attempts = 10

print("✯Welcome to guess the number!☆")
print(f"I'm thinking of a number between 1 and 100!")
print(f"You have {max_attempts} attempts to guess")

while attempts < max_attempts:
    guess_input = input("Enter your guess!: ")

    if guess_input.isdigit():
        guess = int(guess_input)
        attempts += 1

        if guess < 1 or guess >100:
            print(f"Please enter a guess between 1 and 100.")
        elif guess < secret_number:
            print("Too low! Try again!")
        elif guess > secret_number:
            print("Too high! Try again!")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts!✧")
            break
    else:
        print("Please enter a valid integer!")
if attempts == max_attempts:
    print(f"Oh no! You have used all {max_attempts} attempts! The number was {secret_number}:(")
          