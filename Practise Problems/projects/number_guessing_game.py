import random


lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)
guesses = 0

isrunning = True

print("Python Number Guessing Game")

print()
print(f"Select a number between {lowest_num} and {highest_num}")

print(answer)

while isrunning:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low ! Try again")
        elif guess > answer:
            print("Too high ! Try again")
        else:
            print(f"CORRECT! The answer is {answer}")
            print(f"Number of Guesses : {guesses}")
            isrunning = False


    else:
        print("Invalid Guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")



