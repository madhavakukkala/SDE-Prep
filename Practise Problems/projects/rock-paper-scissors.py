import random


options = ("rock", "paper", "scissors")



isplaying = True

while isplaying:

    player = None
    computer = random.choice(options)
    
    while player not in options:
        player = input(f"Enter a choice (rock , paper, scissors) : ") 
        
    if player == computer:
        print("Its a Tie")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("you lose")
        isplaying = False


    if input("Play again? (y/n)").lower() == "y":
        playing = False

print("Thanks for playing!")