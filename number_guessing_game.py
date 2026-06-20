import random

while True:
    print("\n===================================")
    print("WELCOME TO THE NUMBER GUESSING GAME  ")
    print("===================================")
    number = random.randint(1, 10)
    print("I Choose a number between 1 -10")

    while True:
        guess = int(input("Guess a number between 1 -10: "))
        if guess == number:
            print("You guessed right!")
            print("===Thanks for playing . Goodbye!===\n")
            break
        elif guess < number:
            print("Your guess is higher than the number.")
        else:
            print("Your guess is lower than the number.")

    if input("Do you want to play again? (y/n): ") != "y":
        break
