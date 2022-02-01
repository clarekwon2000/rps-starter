from itertools import repeat
from random import choice
import os
from turtle import goto

# WELCOME PLAYER 

player_name = os.getenv("PLAYER_NAME", default = "Player One")
print("Welcome 'player_name'. Let's Play Rock, paper, scissors!")

# ASK FOR USER INPUT 
u = input("Please choose one of: 'rock', 'paper', 'scissors':")
print("USER CHOSE:",u)

# VALIDATIONS 
u = u.lower()

if u != 'rock' and u != 'paper' and u != 'scissors':
    print("Invalid choice: Please select again.")
    exit()
    
# COMPUTER CHOICE 

c = ['rock', 'paper', 'scissors']
computer_action = choice(c)
print("THE COMPUTER CHOSE:",computer_action)

# DETERMINE THE WINNER 
# DISPLAYING RESULTS

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

print("Thanks for playing. Please play again!")