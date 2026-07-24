import random
import time

choices = ["rock", "paper", "scissors"]

def play_rps():
    print("Rock, Paper, Scissors!")
    print("")

    user = input("Choose rock, paper, or scissors: ").lower()

    if user not in choices:
        print("Invalid choice!")
        return
        
    print("")
    print("Thinking...")
    time.sleep(1.25)
    print("")

    computer = random.choice(choices)

    print(f"You chose: {user}")
    print(f"My-AI chose: {computer}")
    print("")

    if user == computer:
        print("It's a tie!")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You win!")

    else:
        print("I win!")
