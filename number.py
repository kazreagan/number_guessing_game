import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < number:
        print("Too Low")

    elif guess > number:
        print("Too high")

    else:
        print("Congratulations: You got it right!")
        break