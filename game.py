from random import choice
import os
from dotenv import load_dotenv

def determine_winner (u,computer_action):
    hold_winner = ""
    if u == computer_action:
        print(f"Both players selected {u}. It's a tie!")
        hold_winner = None
    elif u == "rock": 
        if computer_action == "scissors" :
            print ("Rock beats Scissors. You win!")
            hold_winner = "rock"
        else:
            print ("Paper beats Rock. You lose!")
            hold_winner = "paper"
    elif u == "paper": 
        if computer_action == "rock":
            print (f"Paper beats Rock! You win!")
            hold_winner = "paper"
        else:
            print (f"Scissors beats Paper! You lose!") 
            hold_winner = "scissors"
    elif u == "scissors": 
        if computer_action == "paper":
            print (f"Scissors beats Paper! You win!")
            hold_winner = "scissors"
        else:
            print (f"Rock beats Scissors! You lose!") 
            hold_winner = "rock"
    return hold_winner

if __name__ == "__main__":

# WELCOME PLAYER 

    load_dotenv()
    player_name = os.getenv("PLAYER_NAME", default = "Player One")
    print("Welcome", player_name, "Let's Play Rock, paper, scissors!")

# ASK FOR USER INPUT 
    u = input("Please choose one of: 'rock', 'paper', 'scissors':")
    print(player_name,"CHOSE:",u)

# VALIDATIONS 
    u = u.lower()

    if u != 'rock' and u != 'paper' and u != 'scissors':
        print("Invalid choice: Please try again.")
        exit()
        
# COMPUTER CHOICE 

    c = ['rock', 'paper', 'scissors']
    computer_action = choice(c)
    print("COMPUTER CHOSE:",computer_action)

# DETERMINE THE WINNER 
# DISPLAYING RESULTS

    determine_winner(u,computer_action)         

# END GAME

    print(f"Thanks for playing {player_name}. Please play again!")

