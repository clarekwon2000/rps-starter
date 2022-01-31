# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md

from random import choice
import os

# WELCOME PLAYER 

while True: 
    player_name = os.getenv("PLAYER_NAME", default = "Player One")
    print("Welcome 'player_name'. Let's Play Rock, paper, scissors!")

# ASK FOR USER INPUT 
    u = input("Please choose one of: 'rock', 'paper', 'scissors':")
    print("USER CHOSE:",u)

# VALIDATIONS 
    u = u.lower()

    if u != 'rock' and u != 'paper' and u != 'scissors':
        print("Invalid choice: Please select again.")

# COMPUTER CHOICE 

    c = ['rock', 'paper', 'scissors']
    computer_action = choice(c)
    print("THE COMPUTER CHOSE:",computer_action)

# DETERMINE THE WINNER 
# FINAL RESULTS

    if u == computer_action:
        print(f"Both players selected {u}. It's a tie!")
    elif u == "rock": 
        if computer_action == "scissors" :
            print ("Rock beats Scissors. You win!")
        else:
            print ("Paper beats Rock. You lose!")
    elif u == "paper": 
        if computer_action == "rock":
            print ("Paper beats Rock! You win!")
        else:
            print ("Scissors beats Paper! You lose!") 
    elif u == "scissors": 
        if computer_action == "paper":
            print ("Scissors beats Paper! You win!")
        else:
            print ("Rock beats Scissors! You lose!")           

# END GAME

    play_again = input("Thanks for playing. Play again? (y/n):")
    if play_again.lower() != "y":
        play_again = "yes"
        play_again != "y"
        True
        play_again == "n"
        False
    
        break